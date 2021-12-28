import matplotlib.pyplot as plt
import numpy as np
import eqs
import rk
import vectorfield

# poner ecuaciones y parámetros en eqs.py

# ejemplo plot Rossler
trans = 5000
f = eqs.fRossler

# plot 3d (por defecto ejes xyz)
rk.plot(np.array([0.3, 0.5, 0.2]), 2500, 0.01, f, plot3d = True, trans = trans)
plt.show()

# plot proyección ejes yz
rk.plot(np.array([0.3, 0.5, 0.2]), 2500, 0.01, f, coords = [1, 2], trans = trans)
plt.show()

# plot proyección ejes xz
rk.plot(np.array([0.3, 0.5, 0.2]), 2500, 0.01, f, coords = [0, 2], trans = trans)
plt.show()

# por defecto proyección sobre ejes xy (coords = [0, 1])
rk.plot(np.array([0.3, 0.5, 0.2]), 2500, 0.01, f, trans = trans)
plt.show()

# escribir iteraciones en archivo
rk.to_file(np.array([0.3, 0.5, 0.2]), 2500, 0.01, f)


# ejemplo plot 2d con campo vectorial y algunas soluciones
f = eqs.fEjemplo
# puntos críticos y autovectores obtenidos con Maple
cs = np.array([
    [0, 0], 
    [175/64, -25/64],
    [4275/3584, -1325/3584]
])
cx, cy = cs[:,0], cs[:,1]

eig = np.array([
    [[-7, 1], [1, -4/3]], 
    [[-7, 1], [37/9, 1]]
])

# vista y punto central
rang = 5
x0, y0 = cs[2]
x_range = [x0 - rang, x0 + rang]
y_range = [y0 - rang, y0 + rang]

# separatrices de sillas y sol periodica
gen = rk.initial(eig[0,0], cs[0], 1, 0.001)
rk.plot(gen, 22, 0.01, f, color = 'red', label = 'separatriz')
gen = rk.initial(eig[0,0], cs[0], -1, 0.001)
rk.plot(gen, 50, 0.01, f, color = 'red')
gen = rk.initial(eig[0,1], cs[0], 1, 0.001)
rk.plot(gen, 45, -0.01, f, color = 'red')
gen = rk.initial(eig[0,1], cs[0], -1, 0.001)
rk.plot(gen, 27, -0.01, f, color = 'red')

gen = rk.initial(eig[1,0], cs[1], 1, 0.001)
rk.plot(gen, 25, -0.01, f, color = 'green', label = 'separatriz')
gen = rk.initial(eig[1,0], cs[1], -1, 0.001)
rk.plot(gen, 22, -0.01, f, color = 'green')
gen = rk.initial(eig[1,1], cs[1], 1, 0.001)
rk.plot(gen, 24, 0.01, f, color ='green')
gen = rk.initial(eig[1,1], cs[1], -1, 0.001)
rk.plot(gen, 26, 0.01, f, color = 'green')

gen = np.array([2, -0.4])
rk.plot(gen, 400, 0.001, f, color = 'blue', label = 'solución periódica')

# soluciones particulares
rk.plot(np.array([0, -2]), 400, 0.001, f, color = 'k', label = 'soluciones particulares')
rk.plot(np.array([0, -2]), 400, -0.001, f, color = 'k')

rk.plot(np.array([2, 2]), 400, 0.001, f, color = 'k')
rk.plot(np.array([2, 2]), 400, -0.001, f, color = 'k')

rk.plot(np.array([5, -0.3]), 400, 0.001, f, color = 'k')
rk.plot(np.array([5, -0.3]), 400, -0.001, f, color = 'k')

rk.plot(np.array([-2, 2]), 400, 0.001, f, color = 'k')
rk.plot(np.array([-2, 2]), 400, -0.001, f, color = 'k')

# campo vectorial
# número de flechas
dx, dy = 23, 23
vectorfield.plot_vec_field(x_range, y_range, cx, cy, dx, dy, f)


plt.xlim(-4, 6)
plt.ylim(-5.5, 4)
plt.legend()
plt.show()
