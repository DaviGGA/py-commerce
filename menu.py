import json
import os
from time import sleep

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


def find(list,id):
    for item in list:
        if item['id'] == int(id):
            p = item
            break
    
    return p

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


def calcula_carrinho(carrinho):
    valor = 0
    for produto in carrinho:
        valor += produto['preco'] * produto['quantidade']

    return valor

def deleta_item_carrinho(id,carrinho):
    
    encontrou = False 
    print(carrinho)
    for produto in carrinho:
        if produto['id'] == int(id):
            carrinho.remove(produto)
            print(carrinho)
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

