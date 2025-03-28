# -*- coding: utf-8 -*-
"""FT_Polos e Zeros

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zou6XdC-FSSvgZ_7xnyclX0Jv5jlTd_h
"""

# Commented out IPython magic to ensure Python compatibility.
# Exibir tudo no mesmo documento
# %matplotlib inline

import sympy
from sympy import *
from sympy.physics.control.lti import TransferFunction
from sympy.physics.control.control_plots import pole_zero_plot
s = sympy.symbols('s')
c, C = symbols('c C', cls = Function)

# Print mais bonito no SymPy
init_printing(use_unicode=True)

# Condicoes Iniciais - NULAS
y0 = 0
dy_0 = 0

# Defina aqui a equação diferencial no domínio 's'
# s^2C(s)-sy(0)-y'(0) + 6(sC(s)-y(0)) + 2C(s) = 2(sR(s)-y(0)) + R(s)
equacao_em_s  = Eq(((s**2)*C(s)-s*y0-dy_0)+12*(s*C(s)-y0)+32*C(s), 2/(s**3))

# Resolve a equação para G(s) = C(s) / R(s)
G_s = solve(equacao_em_s, C(s))
print(G_s[0])

num, den = fraction(G_s[0])
print(num)
print(den)


ft1 = TransferFunction(num, den, s)
print(ft1)


pole_zero_plot(ft1)