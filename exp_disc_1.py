import matplotlib.pyplot as plt
from math import log
import eqs

to_file = False
# función y jacobiano
func = eqs.fLogistic
dfunc = eqs.dfLogistic

# introducir varios valores iniciales para comparar sus plots
x = [0.35, 0.55, 0.66]
its = 10000
l = [[] for _ in range(len(x))]
acc = len(x) * [0]

for i in range(1, its+1):
    for j, val in enumerate(x):
        acc[j] += log(abs(dfunc(val)))
        l[j].append(acc[j]/i)
        x[j] = func(val)

if to_file:
    with open('exp_disc.dat', 'w') as f:
        f.write('\n'.join(' '.join(map(str, [i, *vals])) for i, vals in enumerate(zip(*l), 1)))

for val in l:
    print(val[-1])
    plt.plot(val, linewidth = 0.3)

plt.show()
