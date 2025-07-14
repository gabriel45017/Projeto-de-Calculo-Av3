import math

# Define a função a partir da string digitada pelo usuário
def f(x):
    return eval(expressao, {"x": x, "math": math, "_builtins_": {}})

# Função que implementa a soma de Riemann
def soma_riemann(f, a, b, n, metodo):
    largura = (b - a) / n
    soma = 0

    for i in range(n):
        if metodo == "esquerda":
            xi = a + i * largura
        elif metodo == "direita":
            xi = a + (i + 1) * largura
        elif metodo == "meio":
            xi = a + (i + 0.5) * largura
        else:
            raise ValueError("Método inválido. Use: esquerda, direita ou meio.")
        
        soma += f(xi) * largura

    return soma

# Entrada do usuário
expressao = input("Digite a função f(x) (ex: x**2 + 3*x + 1): ").strip()
a = float(input("Digite o limite inferior (a): "))
b = float(input("Digite o limite superior (b): "))
n = int(input("Digite o número de subdivisões (n): "))
metodo = input("Método (esquerda, direita ou meio): ").strip().lower()

# Cálculo e resultado
resultado = soma_riemann(f, a, b, n, metodo)
print(f"\nA aproximação da integral de f(x) entre {a} e {b} pelo método de {metodo} com {n} subdivisões é: {resultado:.6f}")
