soma=0
n =int(input("Digite algum numero: "))

while n!=0 :
    soma+=n
    n =int(input("Digite algum numero: "))

if soma==0:
    print("Não foi digitado nenhum numero válido")
else:
    print("Soma: ", soma)