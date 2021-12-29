import matplotlib.pyplot as plt
import numpy as np
import eqs

to_file = False
x = 0.05
its = 1000
func = eqs.fLogistic
dfunc = eqs.dfLogistic
l = [x]
for i in range(its):
    x = func(x)
    l.append(x)

xs = list(zip(l, l[1:]))
if to_file:
    with open('iter.dat', 'w') as f:
        f.write('\n'.join(' '.join(map(str, [i, *x])) for i, x in enumerate(xs)))

# plot con (x, f_n(x))
x, y = zip(*xs)
plt.plot(x, y, 'o', markersize = 1)
plt.show()

# plot (n, abs(df_n))
# para ver estabilidad comparando con abs(df) = 1
xs = np.linspace(0, 1, 200)
ys = [abs(dfunc(x)) for x in xs]
plt.plot(xs, ys, label = 'abs(df)')
plt.plot([0, 1], [1, 1], label = 'abs(df) = 1')
plt.legend()
plt.show()
