from typing import List, Dict

from models.product import Produto
from utils.helper import formata_floar_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def main() -> None:
    print('==================================')
    print('========== Bem-vinda(o) ==========')
    print('============= PyShop =============')
    print('==================================')

    menu()


def menu() -> None:

    print('\nSelecione uma opção abaixo:')
    print('1 - Cadastrar produto')
    print('2 - Listar produtos')
    print('3 - Comprar produto')
    print('4 - Visualizar carrinho')
    print('5 - Fechar pedido')
    print('6 - Sair do sistema\n')

    try:
        opcao = int(input())
        if opcao == 1:
            cadastrar_produto()
        elif opcao == 2:
            listar_produtos()
        elif opcao == 3:
            comprar_produto()
        elif opcao == 4:
            visualizar_carrinho()
        elif opcao == 5:
            fechar_pedido()
        elif opcao == 6:
            print('Volte sempre!')
            exit(0)
        else:
            print('Opção inválida.')
            menu()
    except ValueError:
        print('Opção inválida.')
        menu()


def cadastrar_produto() -> None:
    print('Cadastro de produto')
    print('===================')

    preco = 0

    nome: str = input('Informe o nome do produto: ')

    while True:
        try:
            preco: float = float(input('Informe o preço do produto: '))
            x = 0
        except ValueError:
            print('Precisa ser um valor numérico.\n')
            x = 1
        if x == 0:
            break

    produto: Produto = Produto(nome, preco)
    produtos.append(produto)

    print(f'O produto {produto.nome} foi cadastrado com sucesso.')
    menu()


def listar_produtos() -> None:
    if len(produtos) > 0:
        print('Listagem de produtos')
        print('====================')
        for produto in produtos:
            print(produto)
            print('--------------------')
    else:
        print('Ainda não há produtos cadastrados.')
    menu()


def comprar_produto() -> None:
    if len(produtos) > 0:
        print('Informe o código do produto que deseja adicionar ao carrinho: ')
        print('==================== Produtos disponíveis ====================')
        print('--------------------------------------------------------------')
        for produto in produtos:
            print(produto)
            print('--------------------')
        codigo: int = int(input())

        produto: Produto = pega_pedido_por_codigo(codigo)
        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quantidade: int = item.get(produto)
                    if quantidade:
                        item[produto] = quantidade + 1
                        print(f'O produto {produto.nome} agora possui {item[produto]} unidades no carrinho.')
                        tem_no_carrinho = True
                        menu()
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                    menu()

            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                menu()
        else:
            print(f'O produto com o código {codigo} não foi encontrado.')
            menu()
    else:
        print('Ainda não há produtos à venda.')
    menu()


def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('Produtos no carrinho:')

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('--------------------')
    else:
        print('Ainda não há produtos no carrinho.')
    menu()


def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0

        print('Produtos do carrinho')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('--------------------')
        print(f'Sua fatura é de {formata_floar_str_moeda(valor_total)}')
        carrinho.clear()
        menu()
    else:
        print('Ainda não há produtos no carrinho.')
        menu()


def pega_pedido_por_codigo(codigo: int) -> Produto:
    p = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p


if __name__ == '__main__':
    main()
