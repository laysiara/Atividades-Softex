
vogais=["a","e","i","o","u"]
cont=0

palavra=input("Digite uma palavra: ")

for letra in palavra:

    if letra in vogais:
        cont+=1

print(cont)