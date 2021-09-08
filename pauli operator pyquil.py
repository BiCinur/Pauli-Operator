from pyquil import Program, WavefunctionSimulator
from pyquil.quilatom import Parameter, quil_sin, quil_cos
from pyquil.quilbase import DefGate
from pyquil.paulis import ID, sX, sY, sZ
from pyquil.paulis import exponential_map
import numpy as np
wavefunction_simulator = WavefunctionSimulator()


# Pauli term takes an operator "X", "Y", "Z", or "I"; a qubit to act on, and
# an optional coefficient.
a = 0.5 * ID()
b = -0.75 * sX(0) * sY(1) * sZ(3)
c = (5-2j) * sZ(1) * sX(2)
# Construct a sum of Pauli terms.
sigma = a + b + c
print(f"sigma = {sigma}")

sigma_cubed = sigma * sigma * sigma
print(f"Simplified: {sigma_cubed}\n")
# Produce Quil code to compute exp[iX]
H = -1.0 * sX(0)
print(f"Quil to compute exp[iX] on qubit 0:\n"
       f"{exponential_map(H)(1.0)}")
