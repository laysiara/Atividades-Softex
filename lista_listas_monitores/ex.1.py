# QUESTÃO 1

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

c = a

a = b
b = c

# Forma mais fácil
# a, b = b, a

print(a, "e", b)