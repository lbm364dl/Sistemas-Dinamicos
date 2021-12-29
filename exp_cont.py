import numpy as np
import matplotlib.pyplot as plt
import eqs
from rk import it

to_file = False
# ecuaciones
func = eqs.fRossler
dfunc = eqs.dfRossler
# dimensión (no sirve para N = 1)
N = 3
# iteraciones de transición
trans = 1000
# iteraciones totales
its = 10000
# pasos de iteración para un jacobiano
jump = 10 

# dato inicial
x = np.array([0.12, 1.13, 0.34])
h = 0.01

# transitorio
for i in range(1, trans):
    x = it(x, h, func)

# calcular exponentes
exps = []
cur_exps = np.zeros(N)
times = []
# J contiene la evolución del jacobiano
J = np.eye(N)
for i in range(trans, its+1):
    cur_df = lambda M: dfunc(x) @ M
    # aproximación numérica de la evolución de J en el instante discreto siguiente (actual + jump * h)
    # usando el jacobiano en el instante discreto actual df(x)
    for j in range(jump):
        # itera a la vez todas las columnas de J
        J = it(J, h, cur_df)
        # iterar también el dato inicial
        x = it(x, h, func)

    # factorización QR, Q será el nuevo J
    J, r = np.linalg.qr(J)
    # la diagonal de R es la contribución a los exponentes
    cur_exps += np.log(np.abs(np.diag(r)))
    times.append(h * jump * (i - trans + 1))
    exps.append(cur_exps/times[-1])

np.set_printoptions(precision = 8, suppress = True)

if to_file:
    with open('exp_cont.dat', 'w') as f:
        f.write('\n'.join(' '.join(map(str, [i, *xps])) for i, xps in zip(times, exps)))

exp_sum = list(map(sum, exps))
plt.plot(times, exp_sum, label = 'suma')

exps = list(zip(*exps))
for i in range(N):
    plt.plot(times, exps[i])

plt.legend()
plt.show()
print(cur_exps/(h*jump*(its-trans+1)))
