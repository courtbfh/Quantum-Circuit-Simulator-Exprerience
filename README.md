

# Quantum Circuit Simulator

#### Video Demo: 

## Overview

The Quantum Circuit Simulator is a Python-based tool designed to simulate and visualize quantum circuits. It provides functionalities for creating qubits, applying quantum gates, and analyzing the results of quantum operations. This project serves as an educational resource for those interested in quantum computing, offering a hands-on approach to understanding fundamental quantum concepts.

## Features

- **Qubit Creation**: Initialize qubits in various states including computational basis states (`'0'`, `'1'`) and superposition states (`'+'`, `'-'`).
- **Quantum Gate Operations**: Apply a range of quantum gates to qubits including:
  - **Hadamard Gate (H)**: Creates superpositions of basis states.
  - **Pauli X Gate (X)**: Performs a bit-flip operation.
  - **Pauli Z Gate (Z)**: Applies a phase flip operation.
  - **Phase S Gate (S)**: Applies a phase shift of π/2.
  - **Phase T Gate (T)**: Applies a phase shift of π/4.
- **Controlled-NOT (CNOT) Gate**: Simulate the CNOT gate, which flips the state of a target qubit based on the state of a control qubit.
- **State Probability Calculation**: Compute and visualize the probabilities of various quantum states after applying gates.
- **Visualization**:
  - **Histogram**: Display a histogram of state probabilities.
  - **Circuit Diagram**: Illustrate the quantum circuit including applied gates.
  - **Bloch Sphere**: Visualize the state of a single qubit on the Bloch sphere.

## Installation

To get started with the Quantum Circuit Simulator, follow these steps:

1. **Clone the Repository**: Clone the repository to your local machine.
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**: Install the required Python packages listed in `requirements.txt`.
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Simulator**: Execute the `project.py` script to start the simulation.
   ```bash
   python project.py
   ```

2. **Provide Input**:
   - **Initial States**: Enter the initial states of the qubits when prompted (e.g., `0`, `+`, `1`, `-`).
   - **Gate Sequence**: Enter the sequence of quantum gates to apply. Use formats such as `0 H` for applying the Hadamard gate to qubit 0, or `CNOT 0 1` for applying a CNOT gate with qubit 0 as the control and qubit 1 as the target.
   - **PDF File Name**: Specify the name of the PDF file to save the results.

3. **View Results**: The simulation results, including visualizations and probabilities, will be saved in the specified PDF file.

## Key Files

- **`project.py`**: The main script containing the core functionalities:
  - **Qubit Creation**: `create_qubit(state)`.
  - **Gate Application**: `apply_gate(qubit, gate)`.
  - **Circuit Simulation**: `simulate_circuit(initial_states, gates_sequence)`.
  - **CNOT Gate Application**: `apply_cnot(qubits, control, target)`.
  - **Probability Calculation**: `calculate_probabilities(qubits)`.
  - **Visualization**: Functions to plot histograms, circuit diagrams, and Bloch sphere representations.

- **`requirements.txt`**: Lists the required Python packages and their versions:
  ```plaintext
  numpy>=1.23.1
  matplotlib>=3.4.3
  pyfiglet>=0.8.post1
  ```

- **`README.md`**: This documentation file, providing an overview of the project, usage instructions, and explanations of features and files.

## Design Choices

- **Qubit Representation**: Qubits are represented as vectors in a two-dimensional Hilbert space, which simplifies the implementation of quantum operations and aligns with standard quantum computing principles.
- **Gate Definitions**: Quantum gates are defined using matrices and applied through matrix multiplication, ensuring accuracy in quantum state transformations.
- **CNOT Gate**: The CNOT gate is implemented by constructing a four-dimensional state vector and applying a CNOT matrix, accurately reflecting quantum entanglement effects.
- **Visualization Techniques**: Utilized `matplotlib` for plotting histograms and circuit diagrams, and `mpl_toolkits.mplot3d` for visualizing qubit states on the Bloch sphere. These tools facilitate a clear understanding of quantum states and operations.

## Examples

### Example 1: Simple Circuit

- **Initial States**: `['0', '1']`
- **Gates Sequence**: `[(0, 'H'), ('CNOT', 0, 1)]`

This example initializes two qubits, applies a Hadamard gate to the first qubit, and then applies a CNOT gate with the first qubit as control and the second qubit as target. The final states of the qubits and the probability distribution will be saved to a PDF.

### Example 2: Superposition and Entanglement

- **Initial States**: `['+', '0']`
- **Gates Sequence**: `[(0, 'H'), ('CNOT', 0, 1)]`

Here, the first qubit is initialized in a superposition state, and the second qubit is initialized in the state `0`. Applying the Hadamard gate followed by the CNOT gate demonstrates the creation of an entangled state. The results will be visualized in the PDF output.

## Thanks

A big thank you to the CS50P course and its incredible team for their guidance and support. This project would not have come to fruition without the comprehensive learning and hands-on experience provided by the course. I am grateful for the expertise and encouragement from the instructors and staff, which played a key role in the development and completion of this project. Your contributions have been immensely valuable and appreciated.

## Contributions

Contributions to this project are welcome! If you have suggestions for improvements or additional features, please open an issue or submit a pull request.


## Contact

For any questions or feedback, please reach out to [nextstepdeveloppe@gmail.com](mailto:nextstepdeveloppe@gmail.com).

---

Thank you for using the Quantum Circuit Simulator. We hope you find it a useful tool for exploring and understanding quantum computing concepts!

```

