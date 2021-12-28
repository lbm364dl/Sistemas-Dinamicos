import numpy as np
from math import exp

PI = np.pi

def fEjemplo(v):
    x, y = v
    return np.array([
        -5*x*x + 26*x*y -21*y*y + 31*x + 42*y,
        3*x*x + 10*x*y -13*y*y -8*x -31*y
    ])

def f(v):
    x, y = v
    return np.array([
        -x - y*y,
        y + x*x
    ])
    
A, B, C = 0.2, 0.2, 9
def fRossler(v):
    x, y, z = v
    return np.array([
        -y - z,
        x + A * y,
        B + z * (x - C)
    ])

def dfRossler(v):
    x, y, z = v
    return np.array([
        [0, -1, -1],
        [1, A, 0],
        [z, 0, x-C]
    ])

sigma, rho, beta = 10, 28, 8/3
def fLorenz(v):
    x, y, z = v
    return np.array([
        sigma * (y - x),
        x * (rho - z) - y,
        x * y - beta * z
    ])

def dfLorenz(v):
    x, y, z = v
    return np.array([
        [-sigma, sigma, 0],
        [rho - z, -1, -x],
        [y, x, -beta]
    ])

K = 1.1
def fStandard(v):
    nx = v[0] + K * np.sin(v[1])
    ny = v[0] + K * np.sin(v[1]) + v[1]
    if nx > PI: nx -= 2*PI
    elif nx < -PI: nx += 2*PI
    if ny > 2*PI: ny -= 2*PI
    elif ny < 0: ny += 2*PI
    return np.array([nx, ny])

def dfStandard(v):
    return np.array([
        [1, K*np.cos(v[1])],
        [1, 1 + K*np.cos(v[1])]
    ])

c1 = 0.38
c2 = 5.8
def fIkeda(v):
    x, y = v
    tn = c1 - c2/(1 + x*x + y*y)
    cost = np.cos(tn)
    sint = np.sin(tn)
    return np.array([
        1 + x * cost - y * sint,
        x * sint + y * cost
    ])

def dfIkeda(v):
    x, y = v
    nx, ny = fIkeda(v)
    aux = 1 + x*x + y*y
    tn = c1 - c2/aux
    aux = 2*c2/(aux * aux)
    cost = np.cos(tn)
    sint = np.sin(tn)
    return np.array([
        [cost - aux * x * ny, -sint - aux * y * ny],
        [sint + aux * x * (nx-1), cost + aux * y * (nx-1)]
    ])

# pasar parámetro opcional, para los diagramas de Feigenbaum
mu = 3.855
def fLogistic(x, par = mu):
    return par * x * (1 - x)

def dfLogistic(x):
    return mu * (1 - 2*x)

alpha = 4.8
def fGauss(x, beta, par = alpha):
    return exp(-par*x*x) + beta

def dfGauss(x):
    return -2*alpha*x * exp(-alpha*x*x)
