import numpy as np
import matplotlib.pyplot as plt

# Rango de valores
x = np.linspace(-10, 10, 400)

# Funciones de activación
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def tanh(x):
    return np.tanh(x)

def relu(x):
    return np.maximum(0, x)

def leaky_relu(x, alpha=0.01):
    return np.where(x > 0, x, alpha * x)

def softplus(x):
    return np.log(1 + np.exp(x))

# Lista de funciones
functions = [
    (sigmoid(x), "Sigmoid"),
    (tanh(x), "Tanh"),
    (relu(x), "ReLU"),
    (leaky_relu(x), "Leaky ReLU"),
    (softplus(x), "Softplus")
]

# Graficar
for y, name in functions:
    plt.figure()
    plt.plot(x, y, label=name)
    plt.title(f"Función de Activación: {name}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()
    plt.show()