import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False, 'nota':5},
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True, 'nota':3},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo': False, 'nota':1}]



def exibir_nome_do_programa():
    print("""
𝚂𝚊𝚋𝚘𝚛 𝙴𝚡𝚙𝚛𝚎𝚜𝚜
""")


def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Ranking dos restaurantes')
    print('5. Sair\n')


def finalizar_app():
    exibir_subtitulo('Finalizando o app')


def voltar_ao_menu_principal():
    input('\nDigite ENTER para voltar ao Menu.')
    main()


def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()


def exibir_subtitulo(texto):
    os.system('cls' if os.name == 'nt' else 'clear')
    linha = '*' * len(texto)
    print(f"\033[92m{texto}\033[0m")
    print(f"\033[94m{linha}\033[0m")
    print()

def classificar_nota(nota):
    if nota <= 2:
        return "Ruim"
    elif nota == 3:
        return "Média"
    else:
        return "Ótima"    


def cadastrar_novo_restaurante():

    exibir_subtitulo('Cadastro de novos restaurantes')

    nome = input('Nome do restaurante: ')
    categoria = input('Categoria: ')

    while True:
        try:
            nota = int(input('Nota (1 a 5): '))

            if 1 <= nota <= 5:
                break

            print("Digite uma nota entre 1 e 5.")

        except ValueError:
            print("Digite apenas números.")

    restaurante = {
        'nome': nome,
        'categoria': categoria,
        'ativo': False,
        'nota': nota
    }

    restaurantes.append(restaurante)

    print(f'\n{nome} cadastrado com sucesso!')

    voltar_ao_menu_principal()


def listar_restaurantes():

    exibir_subtitulo('Listando Restaurantes')

    print(f'{"Nome":<15} | {"Categoria":<15} | {"Nota":<15} | {"Classificação":<15} | Status')
    print('-' *85)

    for restaurante in restaurantes:

        status = "Ativado" if restaurante['ativo'] else "Desativado"

        classificacao = classificar_nota(restaurante['nota'])

        estrelas = "⭐" * restaurante['nota']

        print(f'{restaurante["nome"]:<15} | '
              f'{restaurante["categoria"]:<15} | '
              f'{estrelas:<12} | '
              f'{classificacao:<15} | '
              f'{status:<12}')

    voltar_ao_menu_principal()


def alternar_estado_restaurante():
    exibir_subtitulo('Alternando estado do restaurante')

    nome_restaurante = input('Digite o nome do restaurante: ')

    restaurante_encontrado = False

    for restaurante in restaurantes:  # Para cada restaurante na lista
        if restaurante['nome'].lower() == nome_restaurante.lower():

            restaurante['ativo'] = not restaurante['ativo']
            restaurante_encontrado = True

            if restaurante['ativo']:
                print(f'\nO restaurante "{restaurante["nome"]}" foi ativado com sucesso!')
            else:
                print(f'\nO restaurante "{restaurante["nome"]}" foi desativado com sucesso!')


            break

    if not restaurante_encontrado:
        print('\nRestaurante não encontrado.')

    voltar_ao_menu_principal()


def ranking_restaurantes():
    exibir_subtitulo("Ranking dos Restaurantes")
    ranking = sorted(restaurantes, key=lambda restaurante: restaurante['nota'], reverse=True)

    print(f'{"Posição":<10} {"Nome":<15} {"Nota":<15} {"Classificação":<20}')
    print("-"*56)

    for posicao, restaurante in enumerate(ranking, start=1):
        estrelas = "⭐" * restaurante['nota']
        classificacao = classificar_nota(restaurante['nota'])

        print(f'{posicao:<15} '
              f'{restaurante["nome"]:<15} '
              f'{estrelas:<10} '
              f'{classificacao:<20}')

    voltar_ao_menu_principal()


def escolher_opcao():

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()

        elif opcao_escolhida == 2:
            listar_restaurantes()

        elif opcao_escolhida == 3:
            alternar_estado_restaurante()

        elif opcao_escolhida == 4:
            ranking_restaurantes()

        elif opcao_escolhida == 5:
            finalizar_app()

        else:
            opcao_invalida()

    except ValueError:
        opcao_invalida()


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()