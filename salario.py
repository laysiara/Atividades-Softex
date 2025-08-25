
valor=float(input("Digite o valor recebido:"))
horas=float(input("Digite o valor por hora: "))

salario=valor*horas

print("salario bruto: {:.2f}".format(salario))
print("IR  (11%): R$ {:.2f}".format(salario*0.11))
print("INSS (8%): R$ {:.2f}".format(salario*0.08))
print("Sindicato (5%): R$ {:.2f}".format(salario*0.05))
print("Salário Liquido: R$ {:.2f}".format(salario*0.76))