# Importando pacotes
import numpy as np
import torch
import sympy
from sympy import symbols, diff

# Define a variável simbólica
x = symbols('x')

# Definindo a função
f = x**3 + 2*x**2 - x + 1

# Derivada
derivada = diff(f, x)
print("A derivada da função é ", derivada)


# Avaliando a derivada em um ponto específico
valor_ponto = derivada.subs(x, 5)
print("A derivada de f no ponto 5 é ", valor_ponto)

