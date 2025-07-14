import math

def criar_funcao(expressao):
    def f(x):
        return eval(expressao, {"x": x, "math": math, "__builtins__": {}})
    return f

def derivada_diferencas_finitas(f, x, h, metodo="centrada"):
    if metodo == "progressiva":
        return (f(x + h) - f(x)) / h
    elif metodo == "regressiva":
        return (f(x) - f(x - h)) / h
    elif metodo == "centrada":
        return (f(x + h) - f(x - h)) / (2 * h)
    else:
        raise ValueError("Método inválido. Use: progressiva, regressiva ou centrada.")

# --- Entrada do usuário ---
expressao = input("Digite a função em x (ex: x**2 + 3*x): ")
x = float(input("Digite o ponto onde deseja derivar (x): "))
h = float(input("Digite o valor de h (ex: 0.001): "))
metodo = input("Método (progressiva, regressiva ou centrada): ").strip().lower()

# --- Processamento ---
f = criar_funcao(expressao)
resultado = derivada_diferencas_finitas(f, x, h, metodo)

# --- Saída ---
print(f"A derivada aproximada de f(x) = {expressao} no ponto x = {x} usando {metodo} é: {resultado:.6f}")
