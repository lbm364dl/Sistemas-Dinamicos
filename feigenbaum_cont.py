import matplotlib.pyplot as plt

# Este programa era demasiado lento en Python, requiere muchas iteraciones para una correcta visualización
# Lee y hace plot de los datos obtenidos en el programa feigenbaum_cont.cpp (ver dicho programa)

with open('feigenbaum_cont.dat') as f:
    dat = [list(map(float, line.split())) for line in f.read().splitlines()]
    param, mx = zip(*dat)
    plt.plot(param, mx, 'x', color = 'red', markersize = 0.015)
    plt.show()
