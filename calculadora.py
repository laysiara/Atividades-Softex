
num1=int(input("Digite um numero: "))
num2=int(input("Digite o segundo numero: "))
op=input("Escolha a operação desejada(+,-,*,/): ")

if op =="+":
  resultado=num1+num2
elif op == "-":
  resultado=num1-num2
elif op == "*":
  resultado=num1*num2
else:
  resultado=num1/num2

print(resultado)