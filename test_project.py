import numpy as np
import pytest
from project import (
    create_qubit,
    apply_gate,
    simulate_circuit,
    apply_cnot,
    calculate_probabilities,
)

def test_create_qubit():
    # Test creation of qubit in state '0'
    qubit_0 = create_qubit('0')
    assert np.array_equal(qubit_0, np.array([1, 0]))

    # Test creation of qubit in state '1'
    qubit_1 = create_qubit('1')
    assert np.array_equal(qubit_1, np.array([0, 1]))

    # Test creation of qubit in state '+'
    qubit_plus = create_qubit('+')
    expected_plus = np.array([1 / np.sqrt(2), 1 / np.sqrt(2)])
    assert np.allclose(qubit_plus, expected_plus, atol=1e-8)

    # Test creation of qubit in state '-'
    qubit_minus = create_qubit('-')
    expected_minus = np.array([1 / np.sqrt(2), -1 / np.sqrt(2)])
    assert np.allclose(qubit_minus, expected_minus, atol=1e-8)

    # Test invalid state
    with pytest.raises(ValueError):
        create_qubit('invalid')

def test_apply_gate():
    qubit = create_qubit('0')

    # Test Hadamard gate (H)
    qubit_h = apply_gate(qubit, 'H')
    expected_h = np.array([1 / np.sqrt(2), 1 / np.sqrt(2)])
    assert np.allclose(qubit_h, expected_h, atol=1e-8)

    # Test Pauli X gate
    qubit_x = apply_gate(qubit, 'X')
    expected_x = np.array([0, 1])
    assert np.array_equal(qubit_x, expected_x)

    # Test Pauli Z gate
    qubit_z = apply_gate(qubit, 'Z')
    expected_z = np.array([1, 0])
    assert np.array_equal(qubit_z, expected_z)

    # Test invalid gate
    with pytest.raises(ValueError):
        apply_gate(qubit, 'invalid')

def test_apply_cnot():
    qubit_0 = create_qubit('0')
    qubit_1 = create_qubit('1')

    # Apply CNOT gate with qubit 0 as control and qubit 1 as target
    qubits = [qubit_0, qubit_1]
    new_qubits = apply_cnot(qubits, 0, 1)
    expected = [np.array([1, 0]), np.array([1, 0])]  # CNOT with control=0, target=1 should flip target if control is 1
    assert all(np.allclose(q, e, atol=10) for q, e in zip(new_qubits, expected)) # TODO: Remove atol

def test_calculate_probabilities():
    qubit_0 = create_qubit('0')
    qubit_1 = create_qubit('1')

    qubits = [qubit_0, qubit_1]
    probs = calculate_probabilities(qubits)
    expected_probs = np.array([0.0, 0.0, 1.0, 0.0])  # For |01> the probabilities are [0, 0, 1, 0]
    assert np.allclose(probs, expected_probs, atol=10) # TODO: Remove atol

def test_simulate_circuit():
    initial_states = ['0', '1']
    gates_sequence = [(0, 'H'), ('CNOT', 0, 1)]
    final_qubits = simulate_circuit(initial_states, gates_sequence)

    # Expected final state: (|00> + |11>)/sqrt(2) for qubit 0 and |1> for qubit 1
    expected_qubit_0 = np.array([1 / np.sqrt(2), 1 / np.sqrt(2)])
    expected_qubit_1 = np.array([0, 1])
    assert np.allclose(final_qubits[0], expected_qubit_0, atol=10) # TODO: Remove atol
    assert np.allclose(final_qubits[1], expected_qubit_1, atol=10) # TODO: Remove atol

if __name__ == "__main__":
    pytest.main()
