import matplotlib.pyplot as plt
import numpy as np
import eqs

to_file = True
func = eqs.fIkeda
dfunc = eqs.dfIkeda
N = 2
trans = 1000
its = 50000
print_freq = 100
exps = []
times = []
cur_exps = np.zeros(N)
J = np.eye(N)
x = np.array([0.5, 0.5])

for i in range(1, trans):
    x = func(x)

for i in range(trans, its+1):
    # producto de jacobianos
    # para cada factorización QR, actualizar J como Q
    J, R = np.linalg.qr(dfunc(x) @ J)
    # y la diagonal de R es la contribución a los exponentes de Liapunov
    cur_exps += np.log(np.abs(np.diag(R)))

    if i % print_freq == 0:
        exps.append(cur_exps/(i-trans+1))
        times.append(i)

    x = func(x)

if to_file:
    with open('liapDiscN.dat', 'w') as f:
        f.write('\n'.join(' '.join(map(str, [i, *xps])) for i, xps in zip(times, exps)))

exps = list(zip(*exps))
for i in range(N):
    plt.plot(times, exps[i])

plt.show()
print(cur_exps/(its-trans+1))
