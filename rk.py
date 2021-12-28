import numpy as np
import matplotlib.pyplot as plt

# runge-kutta cuarto orden
def it(v, h, func):
    k1 = func(v)
    k2 = func(v + h * k1 / 2)
    k3 = func(v + h * k2 / 2)
    k4 = func(v + h * k3)
    return v + h * (k1 + 2*(k2 + k3) + k4) / 6

# dato cerca de punto crítico c, dirección vdir
# sgn -1 para sentido opuesto de vdir
# h paso
def initial(vdir, c, sgn, h):
    return c + sgn * h * vdir

# solución particular con v vector valor inicial
# coords : ejes sobre los que proyectar
# se pueden proyectar también en 3d sistemas de dim > 3
def plot(v, its, h, func, trans = 0, color = 'k', label = '', plot3d = False, coords = []):
    if plot3d:
        plt.subplot(projection = '3d')
        if len(coords) != 3:
            coords = [0, 1, 2]
    elif len(coords) != 2:
            coords = [0, 1]

    # transitorio
    for i in range(trans):
        v = it(v, h, func)

    l = [v]
    for i in range(its):
        v = it(v, h, func)
        l.append(v)

    # coge sólo los ejes seleccionados
    cs = [coord for i, coord in enumerate(list(zip(*l))) if i in coords]

    plt.plot(*cs, color = color, label = label)

# guardar iteraciones de rk en un fichero si se desea
def to_file(v, its, h, func):
    with open('rk.dat', 'w') as f:
        for i in range(its):
            f.write(f"{h * i} {' '.join(map(str, v))}\n")
            v = it(v, h, func)

