n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
op = input("Digite a operação (+, -, *, /): ")

if op == "+":
    print("Resultado:", n1 + n2)
elif op == "-":
    print("Resultado:", n1 - n2)
elif op == "*":
    print("Resultado:", n1 * n2)
elif op == "/":
    if n2 != 0:
        print("Resultado:", n1 / n2)
    else:
        print("Erro: divisão por zero")
else:
    print("Operação inválida")