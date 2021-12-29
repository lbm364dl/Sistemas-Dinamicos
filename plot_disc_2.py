import matplotlib.pyplot as plt
import numpy as np
import eqs

def plot(x, its, func, style = 'x-', color = 'k', markersize = 5, linewidth = 1):
    l = [x]
    for i in range(its):
        x = func(x)
        l.append(x)

    x, y = zip(*l)
    plt.plot(x, y, style, color = color, markersize = markersize, linewidth = linewidth)

def plot_random(its, n, x1, x2, y1, y2, func, markersize = 1, style = 'x-', linewidth = 1):
    # genera n datos iniciales aleatorios
    c = [np.array([np.random.uniform(x1, x2), np.random.uniform(y1, y2)]) for i in range(n)]
    colors = ['blue', 'red', 'green', 'yellow', 'lime']
    for j, c0 in enumerate(c):
        # plot de iteración de cada dato inicial, cambiando colores para mejor visualización
        plot(c0, its, func, style = style, color = colors[j % len(colors)], markersize = markersize)

def to_file(x, its, func):
    l = [x]
    for i in range(its):
        x = func(x)
        l.append(x)

    with open('iter.dat', 'w') as f:
        f.write('\n'.join(' '.join(map(str, [i, *x])) for i, x in enumerate(l)))

# ejemplos plots de la aplicación estándar
f = eqs.fStandard
x1, x2 = -np.pi, np.pi
y1, y2 = 0, 2*np.pi
plt.xlim(x1, x2)
plt.ylim(y1, y2)
# plot con puntos aleatorios (son muchos, tarda un poco)
plot_random(1000, 1000, x1, x2, y1, y2, f, style = 'x', markersize = 0.1)
plt.show()

# plot con puntos personalizados
plot(np.array([1, 1]), 1000, f, color = 'yellow', style = 'x', markersize = 1)
plot(np.array([0, 2]), 1000, f, color = 'blue', style = 'x', markersize = 1)
plot(np.array([-2, 1]), 1000, f, color = 'green', style = 'x', markersize = 1)
plot(np.array([0.63, 0.61]), 1000, f, color = 'black', style = 'x', markersize = 1)
plot(np.array([0.12, 1.14]), 1000, f, color = 'cyan', style = 'x', markersize = 1)
plot(np.array([3, 6]), 1000, f, color = 'red', style = 'x', markersize = 1)
plt.show()

# ejemplo escribir iteraciones en fichero
to_file(np.array([1, 1]), 1000, f)
