# Sistemas-Dinamicos
Herramientas para la asignatura de sistemas dinámicos y caos

Estos programas fueron creados con la intención de realizar plots en Python con matplotlib en lugar de usar gnuplot, ya que la mayoría de sus usos en la asignatura
son para hacer plots de datos obtenidos con los programas en C, y manipular ambas herramientas cada vez que se cambian datos puede ser tedioso. El objetivo
es ofrecer (casi) todas estas funcionalidades directamente en programas de Python fácilmente configurables (los programas no piden parámetros por la entrada
estándar, se introducen en el propio código) y ver los plots directamente, aunque también hay opciones para guardar los datos en ficheros si alguien lo necesita.

Programas:
- eqs.py: aquí se introducen todas las funciones de iteración de los sistemas y sus respectivos parámetros.
- rk.py: implementación de Runge-Kutta, plots (incluye 3d y proyecciones) y obtención de datos iniciales cerca de puntos críticos.
- vectorfield.py: plot de campo vectorial en 2d.
- plot_cont.py: ejemplos de cómo utilizar lo anterior para hacer plots de sistemas de tiempo continuo.
- plot_disc_1.py, plot_disc_2.py: plots de sistemas de tiempo discreto de dimensiones 1 y 2. Para dimensión 2 se incluye opción de iterar con n datos iniciales aleatorios.
- feigenbaum_disc.py: diagrama de Feigenbaum para sistemas de tiempo discreto.
- feigenbaum_cont.py, feigenbaum_cont.cpp: diagrama de Feigenbaum para sistemas de tiempo continuo. Este programa en Python hubiera sido demasiado lento.
Se compila y ejecuta feigenbaum_cont.cpp (compilar con -O3 para que tarde menos), y se puede visualizar el plot con feigenbaum_cont.py.
- exp_disc_1.py: exponentes de Liapunov para sistemas de tiempo discreto de dimensión 1. Permite introducir varios datos iniciales para comparar.
- exp_disc_N.py: exponentes de Liapunov para sistemas de tiempo discreto de dimensión N > 1. Incluye suma de los exponentes.
- exp_cont.py: exponentes de Liapunov para sistemas de tiempo continuo de dimensión N > 1. Incluye suma de los exponentes.
