listaIdades = []
listaAlturas = []

for i in range(2):
    idade = int(input("Digite a idade de alguém: "))
    altura = float(input("Digite a altura desse alguém: "))

    listaIdades.append(idade)
    listaAlturas.append(altura)

maiorAltura = max(listaAlturas)
posicaoAlto = listaAlturas.index(maiorAltura)

idadeAlto = listaIdades[posicaoAlto]

print(f"A pessoa mais alta tem {maiorAltura} metros e {idadeAlto} anos.")