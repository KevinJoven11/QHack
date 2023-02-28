# WORK IN PROGRESS
# Imports
import pennylane as qml
import strawberryfields as sf
from strawberryfields.ops import *
from pennylane import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as sc

# Constants
W_b = 1 # 2*np.pi*12.44*1e+10
ALPHA = 1.716

# input: time in miliseconds
# k is number of iterations
# def evolution_op(t,k):
#     const = t*W_b
#     for i in range(0,k):
#         Rgate(const) | 0
#         Dgate(1j*const*ALPHA*np.sqrt(sc.hbar/2)) | 0

t = 0.05

prog = sf.Program(2)
with prog.context as q:
    Dgate(ALPHA) | q[1]
    # if imaginary component: Rgate(-np.pi/2) | q[0]
    # evolution_op(2,20) | q[0]
    for i in range(0,20):
        Rgate(t*W_b) | q[1]
        Dgate(1j*t*W_b*ALPHA*np.sqrt(sc.hbar/2)) | q[1]

    # Measurment
    MeasureX | q[1]


eng = sf.Engine('gaussian', backend_options={"cutoff_dim": 10})
results = []
for i in range(0,100):
    results.append(eng.run(prog).samples[0][0])

plt.hist(results, bins=20)
plt.show()
