# QUESTÃO 9

lista_todos = []
list_par = []
list_impar = []

for i in range(5):

  n = int(input("Digite um numero: "))

  lista_todos.append(n)

  if n % 2 == 0:
    list_par.append(n)
  else:
    list_impar.append(n)

print(lista_todos)
print(list_par)
print(list_impar)