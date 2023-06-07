import json
import os
from time import sleep


# Termina as compras. Na pratica, abre o arquivo do carrinho e deleta todos os objetos de produtos no json.
def finalizar_compra(valor):
    option = input("Tem certeza que deseja finalizar a compra? 1 - Sim 2 - Não\n")

    if option == '1':
        loading()


        with open('carrinho.json', 'w') as file:
            json.dump([], file)

        print(f"Compra no valor de R$ {valor} finalizada com sucesso! Retornando ao menu...")
        sleep(1.5)
        os.system('cls')
        menu()
    elif option == '2':
        loading()
        ver_carrinho()

# Abre o json de carrinho e adiciona o  produto selecionado
def adiciona_ao_carrinho(produto):

    quantidade = int(input(f"Quantos {produto['nome']} você deseja comprar? "))

    if quantidade <= 0:
        print("Quantidade inválida.")
        adiciona_ao_carrinho(produto)

    with open('carrinho.json', 'r') as file:
        carrinho = json.load(file)
    
    produto['quantidade'] = quantidade
    
    carrinho.append(produto)

    with open('carrinho.json', 'w') as file:
        json.dump(carrinho, file)

    print(f"O produto {produto['nome']} foi adicionado ao carrinho!")

    lista_produtos()


# Função auxilitar que itera a lista de produtos, caso encontre o produto com o id passado via parâmetro, retorna esse produto.
def find(list,id):
    for item in list:
        if item['id'] == int(id):
            p = item
            break
    
    return p

# Função que emula um carregamento, usa a biblioteca os para usar o comando "clear" do terminal
def loading():
    carregando = 'carregando'
    os.system('cls')
    print(carregando)
    sleep(0.25)
   
    for i in range(3):
        os.system('cls')
        carregando += '.'
        print(carregando)
        sleep(0.25)

    os.system('cls')


# Itera todos os items do carrinho, adicionando a uma variável acumuladora que adiciona o preço * quantidade de cada produto iterado
# que é retornada ao fim da função
def calcula_carrinho(carrinho):
    valor = 0
    for produto in carrinho:
        valor += produto['preco'] * produto['quantidade']

    return valor

# Encontra o item via id, o carrinho é passado via parâmetro, remove o item do dicionário e reesceve o arquivo json
def deleta_item_carrinho(id,carrinho):
    
    encontrou = False 
    for produto in carrinho:
        if produto['id'] == int(id):
            carrinho.remove(produto)
            
            with open('carrinho.json', 'w') as file:
                json.dump(carrinho, file)
            
            encontrou = True

    if encontrou:
        print("Produto excluído com sucesso!")
        sleep(2)
        loading()
        ver_carrinho()

    else:
        print("Desculpe, não encontramos o produto.")
        sleep(2)
        loading()
        ver_carrinho()

# Abre o arquido de carrinho, pega todos os produtos nele e itera, printando-os.
def ver_carrinho():
    
    with open('carrinho.json', 'r') as file:
        carrinho = json.load(file)

    print('=' * 30)
    print("CARRINHO".center(30))

    for produto in carrinho:
            print("=" * 30)
            print(f"Id: {produto['id']}")
            print(f"Nome: {produto['nome']}")
            print(f"Preço: R$ {produto['preco']}")
            print(f"Quantidade: {produto['quantidade']}")
            print(f"Categoria: {produto['categoria']}")

    print("=" * 30)
    
    valor = calcula_carrinho(carrinho)

    print(f"Valor do carrinho: R$ {valor}")

    print("=" * 30)
    print("1 - Finalizar compra")
    print("2 - Excluir produto do carrinho")
    print("3 - Voltar ao menu\n")

    option = input('')

    if option == '1':
        finalizar_compra(valor)
    elif option == '2':
        id = input("Digite o Id do produto: ")
        deleta_item_carrinho(id,carrinho)
    elif option == '3':
        loading()
        menu()

    

# Abre o arquivo json de produtos, itera todos, printando-os.
def lista_produtos():
    with open('produtos.json', 'r') as file:
        produtos = json.load(file)
        
        for produto in produtos:
            print("=" * 30)
            print(f"Id: {produto['id']}")
            print(f"Nome: {produto['nome']}")
            print(f"Preço: R$ {produto['preco']}")
            print(f"Categoria: {produto['categoria']}")

        option = input('Escolha o produto pelo Id (ou digite "-" para sair): ')

        if option == '-':
            loading()
            menu()
        else:
            produto = find(produtos,option)
            
            option = input(f"Deseja adicionar o produto {produto['nome']} ao carrinho? \n 1 - Sim 2 - Não \n")

            if option == '1':
                loading()
                adiciona_ao_carrinho(produto)
            elif option == '2':
              loading()             
              lista_produtos()

# Menu principal da aplicação, que faz as "rotas" para outras funções
def menu():
    print( "="* 30)
    print("Seja bem-vindo a loja!".center(30))
    print( "="* 30)
    
    print("1 - Lista de produtos")
    print("2 - Carrinho")
    print("\n")

    op = input()

    if op == '2':
        loading()
        ver_carrinho()

    elif op == '1':
        loading()
        lista_produtos()
    
  

menu()

