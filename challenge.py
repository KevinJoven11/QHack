# WORK IN PROGRESS
# Imports
import pennylane as qml
import strawberryfields as sf
from strawberryfields.ops import *
from pennylane import numpy as np
import matplotlib.pyplot as plt

# Constants
W_b = 1 # 2*np.pi*12.44*1e+10
ALPHA = 1.716

# input: time in miliseconds
# k is number of iterations
def evolution_op(t,k):
    const = t*w_b
    for j in range(0,k):
        Rgate(const) | 0
        Dgate(i*const*ALPHA*np.sqrt(np.hbar/2)) | 0 # i is the imaginary unit


prog = sf.Program(1)
with prog.context as q:
    Dgate(ALPHA) | q[1]
    # if imaginary component: Rgate(-np.pi/2) | q[0]
    evolution_op(2,3) | q[0]
