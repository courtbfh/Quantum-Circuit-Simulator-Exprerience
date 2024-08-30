# Qubits and quantum algorithms simulator
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.patches as patches
from mpl_toolkits.mplot3d import Axes3D
from pyfiglet import Figlet

def create_qubit(state='0'):
    """Create a qubit in the specified state ('0' or '1') or in a superposition state"""
    if state == "0":
        return np.array([1, 0])  # State |0>
    elif state == "1":
        return np.array([0, 1])  # State |1>
    elif state == "+":
        return np.array(
            [1 / np.sqrt(2), 1 / np.sqrt(2)]
        )  # Superposition state (|0> + |1> / sqrt(2))
    elif state == "-":
        return np.array(
            [1 / np.sqrt(2), -1 / np.sqrt(2)]
        )  # Superposition state (|0> - |1> / sqrt(2))
    else:
        raise ValueError("Unknown state: Use '0', '1', '+', or '-'")

def apply_gate(qubit, gate):
    """Apply a quantum gate to the qubit"""
    # Define the basic quantum gates
    gates = {
        "H": np.array(
            [[1 / np.sqrt(2), 1 / np.sqrt(2)], [1 / np.sqrt(2), -1 / np.sqrt(2)]]
        ),  # Hadamard
        "X": np.array([[0, 1], [1, 0]]),  # Pauli X (NOT Quantum)
        "Z": np.array([[1, 0], [0, -1]]),  # Pauli Z
        "S": np.array([[1, 0], [0, 1j]]),  # Phase S
        "T": np.array([[1, 0], [0, np.exp(1j * np.pi / 4)]]),  # Phase T
    }

    if gate not in gates:
        raise ValueError('Unknown gate: Use "H", "X", "Z", "S", or "T"')

    return np.dot(gates[gate], qubit)

def simulate_circuit(initial_states, gates_sequence):
    qubits = [create_qubit(state) for state in initial_states]
    print(f"Initial state of Qubits: {qubits}")

    for operation in gates_sequence:
        if len(operation) == 2:
            qubit_idx, gate = operation
            qubits[qubit_idx] = apply_gate(qubits[qubit_idx], gate)
            print(f"State of qubit {qubit_idx} after applying the gate '{gate}': {qubits[qubit_idx]}")
        elif len(operation) == 3 and operation[0] == 'CNOT':
            control, target = operation[1], operation[2]
            qubits = apply_cnot(qubits, control, target)
            print(f"State of qubits after the CNOT gate (qubit {control} -> qubit {target}): {qubits}")
        else:
            raise ValueError("Unknown or unsupported gate")

    return qubits

def apply_cnot(qubits, control, target):
    """CNOT matrix for two qubits"""
    if len(qubits) < 2:
        raise ValueError("CNOT requires at least 2 qubits")

    # Convert qubits into four-dimensional state vectors
    state_vector = np.kron(qubits[control], qubits[target])

    cnot_matrix = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0]
    ])

    # Apply the CNOT gate
    new_state_vector = np.dot(cnot_matrix, state_vector)

    # Split the resulting vector back into two qubits
    qubits[control] = new_state_vector[:2]
    qubits[target] = new_state_vector[2:]

    return qubits

"""PART FOR VISUALIZATION"""

def calculate_probabilities(qubits):
    """Calculate the probabilities of each state after applying gates"""
    if len(qubits) == 1:
        state_vector = qubits[0]
    else:
        state_vector = qubits[0]
        for qubit in qubits[1:]:
            state_vector = np.kron(state_vector, qubit)

    probabilities = np.abs(state_vector) ** 2  # Square of amplitude to get probabilities
    return probabilities

def plot_histogram_to_pdf(probabilities, num_qubits, pdf):
    """Save the complete histogram of probabilities into a single PDF page."""
    fig, ax = plt.subplots()
    states = [f"|{bin(i)[2:].zfill(num_qubits)}>" for i in range(2**num_qubits)]

    # Plot the probabilities for all states
    bars = ax.bar(states, probabilities)
    ax.set_xlabel('States')
    ax.set_ylabel('Probabilities')
    ax.set_title('Histogram of Quantum State Probabilities')

    # Save the current figure to the PDF
    pdf.savefig(fig)
    plt.close(fig)  # Close the figure to free memory

def draw_circuit(gates_sequence, num_qubits, pdf):
    """Draw a basic Quantum circuit"""

    fig, ax = plt.subplots(figsize=(10, num_qubits))
    ax.set_xlim(0, len(gates_sequence) + 1)
    ax.set_ylim(-1, num_qubits)

    # Draw qubit lines
    for i in range(num_qubits):
        ax.hlines(y=i, xmin=0, xmax=len(gates_sequence) + 1, color='black')
        ax.text(-0.5, i, f'q{i}', fontsize=12, va='center')

    # Place gates
    for idx, operation in enumerate(gates_sequence, 1):
        if len(operation) == 2:  # One qubit operation
            qubit_idx, gate = operation
            ax.text(idx, qubit_idx, gate, fontsize=12, va='center', ha='center', bbox=dict(boxstyle="circle,pad=0.3", fc="lightblue", ec="black"))
            """ax.setTitle("Circuit Draw")"""
        elif len(operation) == 3 and operation[0] == 'CNOT':  # CNOT Gate
            control, target = operation[1], operation[2]
            ax.text(idx, control, '•', fontsize=18, va='center', ha='center')
            ax.vlines(x=idx, ymin=min(control, target), ymax=max(control, target), color='black')
            ax.text(idx, target, 'X', fontsize=12, va='center', ha='center', bbox=dict(boxstyle="circle,pad=0.3", fc="lightblue", ec="black"))

        ax.axis('off')
        pdf.savefig(fig)
        plt.close(fig)  # Close the figure to free memory

def plot_bloch_vector(qubit, pdf):
    """ Display the state of a qubit on the Bloch sphere """
    theta = 2 * np.arccos(qubit[0])
    phi = np.angle(qubit[1])

    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.quiver(0, 0, 0, x, y, z, color='blue', linewidth=3)

    # Draw the sphere
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones(np.size(u)), np.cos(v))

    ax.plot_surface(x, y, z, color='lightgrey', alpha=0.3)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Bloch Sphere')

    pdf.savefig(fig)
    plt.close(fig)  # Close the figure to free memory

def main():
    figlet = Figlet()
    figlet.setFont(font="doom")
    print(figlet.renderText("Quantum Simulator"))

    # Ask the user to enter the initial states of the qubits
    initial_states = input("Enter the initial states of the qubits (e.g., 0, +, 1, -) separated by commas: ").split(',')
    initial_states = [state.strip() for state in initial_states]  # Remove whitespace

    # Validate the initial states
    for state in initial_states:
        if state not in ['0', '1', '+', '-']:
            raise ValueError("Unknown state: Use '0', '1', '+', or '-'")

    # Ask the user to enter the sequence of gates to apply
    gates_sequence = []
    while True:
        gate_input = input("Enter a quantum gate to apply (e.g., 0 H, 1 X, CNOT 0 1), or 'done' to finish: ").strip()
        if gate_input.lower() == 'done':
            break
        parts = gate_input.replace(',', '').split()
        if len(parts) == 2:
            try:
                qubit_idx = int(parts[0])
                gate = parts[1]
                gates_sequence.append((qubit_idx, gate))
            except ValueError:
                print("Invalid input, please try again.")
        elif len(parts) == 3 and parts[0].upper() == 'CNOT':
            try:
                control_qubit = int(parts[1])
                target_qubit = int(parts[2])
                gates_sequence.append(('CNOT', control_qubit, target_qubit))
            except ValueError:
                print("Invalid input, please try again.")
        else:
            print("Invalid input, please try again.")

    # Ask the user to enter the PDF file name
    pdf_filename = input("Enter the PDF file name to save the results (default: quantum_simulation_results.pdf): ").strip()
    if not pdf_filename:
        pdf_filename = "quantum_simulation_results.pdf"

    # Simulate the circuit with the user inputs
    final_qubits = simulate_circuit(initial_states, gates_sequence)
    num_qubits = len(initial_states)
    probabilities = calculate_probabilities(final_qubits)

    # Convert the final states to ket notation for display
    print("Final state after applying all gates:")
    for qubit in final_qubits:
        if np.array_equal(qubit, np.array([1, 0])):
            print("|0>")
        elif np.array_equal(qubit, np.array([0, 1])):
            print("|1>")
        elif np.array_equal(qubit, np.array([1/np.sqrt(2), 1/np.sqrt(2)])):
            print("|+>")
        elif np.array_equal(qubit, np.array([1/np.sqrt(2), -1/np.sqrt(2)])):
            print("|->")
        else:
            print("Unknown state:", qubit)

    # Generate and save the plots and numerical values in a PDF file
    with PdfPages(pdf_filename) as pdf:
        plot_histogram_to_pdf(probabilities, num_qubits, pdf)
        draw_circuit(gates_sequence, num_qubits, pdf)
        for qubit in final_qubits:
            plot_bloch_vector(qubit, pdf)

        # Add the numerical values of the probabilities in the PDF
        fig, ax = plt.subplots()
        ax.axis('off')
        text_str = "Probabilities of states:\n"
        states = [f"|{bin(i)[2:].zfill(num_qubits)}>" for i in range(2**num_qubits)]
        for state, prob in zip(states, probabilities):
            text_str += f"{state}: {prob:.4f}\n"

        ax.text(0.5, 0.5, text_str, transform=ax.transAxes, fontsize=12, verticalalignment='center', horizontalalignment='center')
        pdf.savefig(fig)
        plt.close(fig)

    print(f"Simulation complete. The results have been saved in '{pdf_filename}'.")


# Call the main function
if __name__ == "__main__":
    main()
