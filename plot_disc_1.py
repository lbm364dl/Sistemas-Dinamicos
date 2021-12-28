import matplotlib.pyplot as plt
import numpy as np
import eqs

x = 0.05
its = 1000
f = eqs.fLogistic
df = eqs.dfLogistic
l = [x]
for i in range(its):
    x = f(x)
    l.append(x)

# plot con (x, f_n(x))
x, y = zip(*zip(l, l[1:]))
plt.plot(x, y, 'o', markersize = 1)
plt.show()

# plot (n, abs(df_n))
# para ver estabilidad comparando con abs(df) = 1
xs = np.linspace(0, 1, 200)
ys = [abs(df(x)) for x in xs]
plt.plot(xs, ys, label = 'abs(df)')
plt.plot([0, 1], [1, 1], label = 'abs(df) = 1')
plt.legend()
plt.show()
