import numpy as np
import eqs

to_file = False
func = eqs.fIkeda
dfunc = eqs.dfIkeda
N = 2
trans = 1000
its = 30000
print_freq = 100
exps = []
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
        exps.append((i, cur_exps/(i-trans+1)))

    x = func(x)

if to_file:
    with open('liapDiscN.dat', 'w') as f:
        f.write('\n'.join(' '.join(map(str, [i, *xps])) for i, xps in exps))

print(cur_exps/(its-trans+1))
