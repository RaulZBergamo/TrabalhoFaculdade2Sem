import os, json

CAMINHO_ARQUIVO = 'C:/Users/raulb/Desktop/produtos.data'

produtos = []

opcao = None

def gravarArquivo(produtos):
    arquivo = open(CAMINHO_ARQUIVO, "w")
    json.dump(produtos, arquivo)
    arquivo.close()

def lerArquivo():  
    if os.path.exists(CAMINHO_ARQUIVO):
        arquivo = open(CAMINHO_ARQUIVO, "r")

        conteudo_arquivo = arquivo.read()

    if conteudo_arquivo != "":
        global produtos
        produtos = json.loads(conteudo_arquivo)

    arquivo.close()

def clear():
    os.system('cls')

def mostrarMenu():
    clear()
    print('=' * 50 + '\n1) Cadastrar produto.\n2) Consultar produtos por faixa de preço.\n3) Gravar produtos em arquivo\n4) Carregar produtos do arquivo\n5) Sair')

def verificarCod(produtos, codigo):
    codigo_original = codigo
    codigo_valido = False

    while codigo_valido != True:

        codigo_exists_filter = filter(lambda x: (x['codigo'] == codigo), produtos)
        codigo_exists = list(codigo_exists_filter)

        if len(codigo_exists) == 0:
            if codigo != codigo_original:
                print(f'Um produto com um código igual já existia, então o código foi alterado para: {codigo}')
            codigo_valido = True
            return codigo
        else:
            maior_codigo = max(produtos, key=lambda produto: produto['codigo'])
            codigo = maior_codigo['codigo'] + 1

def cadastrarProdutos(produtos):

    codigo = int(input('Código do produto: '))
    codigo_certo = verificarCod(produtos, codigo)
    nome_produto = input('Nome do produto: ')
    descricao_produto = input('Descrição do produto: ')
    valor_produto = float(input('Valor do produto: '))

    dic_produto = {
        "codigo": codigo_certo,
        "nome": nome_produto,
        "descricao": descricao_produto,
        "valor": valor_produto,
    }

    produtos.append(dic_produto)

def consultarProdutos(produtos):

    preco_min = float(input('Preço mínimo: '))
    preco_max = float(input('Preço máximo: '))

    clear()

    print('Código\tNome\t\tDescrição\t\tValor\n' + '=' * 70)

    for produto in produtos:

        if produto['valor'] >= preco_min and produto['valor'] <= preco_max:
            print(f"{produto['codigo']}\t{produto['nome']}\t\t{produto['descricao']}\t\t{produto['valor']}\n" + '-' * 70)
            maior_valor = max(produtos, key=lambda produto: produto['valor'])
            menor_valor = min(produtos, key=lambda produto: produto['valor'])

    print(f"Maior valor: {maior_valor['nome']}" + f"\nMenor valor: {menor_valor['nome']}\n" + '=' * 70)

    input('Pressione qualquer tecla para sair...')

while opcao != 5:

    mostrarMenu()
    opcao = int(input('Sua escolha: '))
    clear()

    if opcao != 5 and (opcao >= 1 or opcao <= 4):
        if opcao == 1:
            cadastrarProdutos(produtos)
        if opcao == 2:
            consultarProdutos(produtos)
        if opcao == 3:
            gravarArquivo(produtos)
        if opcao == 4:
            lerArquivo()
    else:
        print('Saindo...')
        continue