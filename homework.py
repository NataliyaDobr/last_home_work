# f(x) = 5x^2 + 10x - 30
# Определить корни
# Найти интервалы, на которых функция возрастает
# Найти интервалы, на которых функция убывает
# Построить график
# Вычислить вершину
# Определить промежутки, на котором f > 0
# Определить промежутки, на котором f < 0

import sympy
import matplotlib.pyplot as plt
import numpy as np

from sympy.solvers import solve
from sympy import Symbol

x = Symbol("x")
f = 5*x**2+10*x-30
print(f)
#Определить корни
print(solve(f,x))

# Найти производную
dif_f = f.diff(x)
print(dif_f)
print(solve(dif_f,x))
# Найти интервалы, на которых функция возрастает
# Найти интервалы, на которых функция убывает
left_point = dif_f.subs(x, -10).evalf()
print(left_point)
right_point = dif_f.subs(x, 10).evalf()
print(right_point)
# функция убывает на промежутке от минус бесконечности до -1 и возрастает на промежутке от -1 до плюс бесконечности

# Построить график
interval = np.arange(-100, 100, 1)
f_values = [f.subs(x, value) for value in interval]
fig = plt.figure(figsize=(10, 10))
plt.plot(interval,f_values)
plt.show()

# Вычислить вершину
x_0 = -10/(2*5)
y_0 = f.subs(x, x_0).evalf()
print(x_0,y_0)

# Определить промежутки, на котором f > 0
# Определить промежутки, на котором f < 0
# так как найдены корни параболы функцию можно разложить на множители 5(x-x1)(x-x2).
# так как 5>0, чередование знаков будет начинаться с +
# f> 0 на промежутке от минус бесконечности до -sqrt(7) - 1 и от -1 + sqrt(7) до плюс бесконечности
# f< 0 на промежутке от -sqrt(7) - 1 до -1 + sqrt(7)