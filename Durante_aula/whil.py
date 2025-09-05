

senha="123"
login="iara"

continuar=True
i=0

while continuar and i<3:
    log=input("")
    sen=input("")

    if log==login and sen == senha:
        continuar=False
       
    i+=1

if continuar == False:
    print("Aertou")

else: 
    print("perdeu")
