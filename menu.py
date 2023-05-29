import json

def adiciona_ao_carrinho(produto):

    quantidade = int(input(f"Quantos {produto['nome']} você deseja comprar? "))

    with open('carrinho.json', 'r') as file:
        carrinho = json.load(file)
    
    produto['quantidade'] = quantidade
    
    carrinho.append(produto)

    with open('carrinho.json', 'w') as file:
        json.dump(carrinho, file)

    print(f"O produto {produto['nome']} foi adicionado ao carrinho!")

    menu()


def find(list,id):
    for item in list:
        if item['id'] == int(id):
            p = item
            break
    
    return p


def calcula_carrinho(carrinho):
    valor = 0
    for produto in carrinho:
        valor += produto['preco'] * produto['quantidade']

    return valor

def ver_carrinho():
    with open('carrinho.json', 'r') as file:
        carrinho = json.load(file)
    
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



    


def lista_produtos():
    with open('produtos.json', 'r') as file:
        produtos = json.load(file)
        
        for produto in produtos:
            print("=" * 30)
            print(f"Id: {produto['id']}")
            print(f"Nome: {produto['nome']}")
            print(f"Preço: R$ {produto['preco']}")
            print(f"Categoria: {produto['categoria']}")

        option = input('Escolha o produto (ou digite "-" para sair): ')

        if option == '-':
            menu()
        else:
            produto = find(produtos,option)
            
            option = input(f"Deseja adicionar o produto {produto['nome']} ao carrinho? \n 1 - Sim 2 - Não \n")

            if option == '1':
                adiciona_ao_carrinho(produto)
            if option == '2':
                
                print("Retornando ao menu.")


def menu():
    print( "="* 30)
    print("Seja bem-vindo a loja!".center(30))
    print( "="* 30)
    
    print("1 - Lista de produtos")
    print("2 - Carrinho")
    print("\n")
    option = input()

    if option == '1':
        lista_produtos()
    if option == '2':
        ver_carrinho()

menu()

# # Módulo para mexer com JSON

# import json

# # Lê o arquivo, e guarda o conteúdo na variável data

# with open('data.json', 'r') as file:
#     data = json.load(file)


# # Criação do dicionario pessoa

# pessoa = {
#     'nome': "Chico",
#     'idade': 20 
#     }

# # Insere a pessoa no array

# data.append(pessoa)

# # Abre o arquivo e insere o conteúdo da variável data no arquivo

# with open('data.json', 'w') as file:
#     json.dump(data, file)

# print(data)