import numpy as np
import matplotlib.pyplot as plt

# x_range, y_range ventana donde poner campo vectorial
# x_range: [x0, x1]
# y_range: [y0, y1]
# cx, cy coordenadas de puntos críticos
# dx, dy número de flechas a visualizar en el campo vectorial
def plot_vec_field(x_range, y_range, cx, cy, dx, dy, func):
    xs, ys = [], []
    vx, vy = [], []

    for xi in np.linspace(*x_range, dx):
        for yi in np.linspace(*y_range, dy):
            # dirección vector
            ff = func(np.array([xi, yi]))
            ff /= np.linalg.norm(ff)
            xs.append(xi)
            ys.append(yi)
            vx.append(ff[0])
            vy.append(ff[1])

    plt.plot(cx, cy, 'o', label = 'puntos críticos')
    plt.quiver(xs, ys, vx, vy)
