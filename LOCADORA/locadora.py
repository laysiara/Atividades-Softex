
filmes=[]

print ("Escolha a opção que você deseja\n*********************************")
print ("1 - ADICIONAR ESTOQUE DE FILME DA LOCADORA")
print ("2 - REMOVER ESTOQUE DA LOCADORA ")
print ("3 - PESQUISA DE FILME PARA ALUGAR")
print ("4 - SAIR")

op=int(input("Opção: "))

while op!=4:

    if op == 1:
        encontrou=0
        
        nomes_estoques=[]
        print("**************************")
        nome=input("Digite o nome do filme: ")

        for elemento in filmes:
            if nome == elemento[0]:
                encontrou+=1

        if encontrou<1:
            print("Esse produto ainda não está cadastrado, deseja adicionar? ")
            resposta=input("(sim) ou (não)?: ").upper()

            if resposta == "SIM":
                
                nomes_estoques.append(nome)
                print("Produto Cadastrado")
                print("**************************")

                estoque_adicionado=int(input("Digite a quantidade de estoque: "))
                while estoque_adicionado<0:
                    estoque_adicionado=int(input("Digite um número válido: "))

                
                nomes_estoques.append(estoque_adicionado)
                filmes.append(nomes_estoques)
                print("**************************")
                print("Atualização completa")
                print("**************************")
            else:
                print("OK")
        else:
            print("Esse produto está cadastrado")
            print("**************************")
            estoque_adicionado=int(input("Digite a quantidade desejada no estoque: "))
            while estoque_adicionado<0:
                estoque_adicionado=int(input("Digite um número válido: "))
            
            for elemento in filmes:
                if nome==elemento[0]:
                    elemento[1]+=estoque_adicionado
            print("**************************")
            print("Produto atualizado.")
 

    if op == 2:

        print("Você deseja remover o produto(1) ou o estoque?(2): ")
        escolha=int(input(""))

        if escolha==1:
            encontrou=0
            while encontrou==0:
                prod=input("Digite o nome do filme que será removido: ")
                for elemento in filmes:
                    if prod == elemento[0]:
                        encontrou+=1
                    else:
                        print("Não foi encontrado")
            
            for i in range(len(filmes)):
                    if filmes[i][0]==prod:
                        filmes.pop(i)
            print("Produto deletado")
        
        elif escolha==2:
            encontrou=0
            while encontrou==0:
                prod=input("Digite o nome do filme que terá o estoque diminuído: ")
                for elemento in filmes:
                    if prod == elemento[0]:
                        encontrou+=1
                        print("Esse filme possui",elemento[1],"de estoque")
                
            

            estoque_dimin=int(input("Digite a quantidade de estoque que será removido: "))

            while estoque_dimin<0:
                estoque_dimin=int(input("Digite um valor válido"))


            for i in range(len(filmes)):
                    if filmes[i][0]==prod:
                        filmes[i][1]-=estoque_dimin
    


    if op==3:

        for i in range(len(filmes)):
            print(f"Filme: {filmes[i][0]}, quantidade disponível: {filmes[i][1]}")

        alugar=input("Deseja escolher algum filme? ").upper()

        if alugar =="SIM":
            encontrou=0

            while encontrou==0:
                nome_alugar=input("Qual o filme escolhido: ")
                for elemento in filmes:
                    if nome_alugar == elemento[0]:
                        encontrou+=1
                        
            for i in range(len(filmes)):
                    if filmes[i][0]==nome_alugar:
                        filmes[i][1]-=1

            print("FILME ALUGADO")
                
    print("filmes: ",filmes)
    print ("Escolha a opção que você deseja\n*********************************")
    print ("1 - ADICIONAR ESTOQUE DE FILME DA LOCADORA")
    print ("2 - REMOVER ESTOQUE DA LOCADORA ")
    print ("3 - PESQUISA DE FILME PARA ALUGAR")
    print ("4 - SAIR")

    op=int(input("Escolha a opção: "))


        