import matplotlib.pyplot as plt
import numpy as np
import eqs

# poner True para escribir los datos en un fichero
to_file = False
func = eqs.fLogistic
# rango de barrido del parámetro
mn, mx = 3, 4
trans, its = 1000, 400
x0 = 0.5
# guardar en un set para quitar repetidos
dat = set()

# iterar parámetro p
for p in np.linspace(mn, mx, 2000):
    x = x0
    # buscando atractor
    for _ in range(trans):
        x = func(x, p)
    # guardando
    for _ in range(its):
        x = func(x, p)
        dat.add((p, x))

dat = sorted(dat)
if to_file:
    with open('feigenbaum_disc.dat', 'w') as f:
        f.write('\n'.join(' '.join(map(str, d)) for d in dat))

p, x = zip(*dat)

plt.plot(p, x, 'x', markersize = 0.015, color = 'red')
plt.show()
