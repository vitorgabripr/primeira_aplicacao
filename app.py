import os

#!dicionario de restaurantes 
restaurantes = [{'Nome': 'Praça da Bóia', 'Categoria': 'Japonesa', 'Ativo': False}, 
                {'Nome': 'Pizza suprema', 'Categoria': 'Italiana', 'Ativo': True},
                {'Nome': 'Cantina', 'Categoria': 'Italiana', 'Ativo': False}]


def exibir_nome_programa():
#!função para exibir o nome do programa
    print("""
█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█""")


def exibir_opcoes():
#!função para exibir as opções

    print('\n\n1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Finalizar app...')

def voltar_ao_menu_principal():
    #!função para voltar ao menu principal
    
    input("\n\n Digite uma tecla para voltar ao menu principal: ")
    main()


def alternar_estado_restaurante():
    #!função para deixar o restaurante ativado ou desativado
    
    exibir_subtitulo('Alternando estado do restaurante...')

    nome_restaurante = input('Digite o nome do restaurante '
                             'que deseja alternar o estado: ')
    restaurante_encontrado = False

    #?  for para alternar o ativado do restaurante após ativar
    #? o mesmo para desativar
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['Nome']:
            restaurante_encontrado = True
            restaurante['Ativo'] = not restaurante['Ativo']
            mensagem = print(f'O restaurante {nome_restaurante} foi ativado com sucesso!')
            if restaurante['Ativo']:
                print(mensagem)
            else:
               print(f'O restaurante {nome_restaurante} foi desativado com sucesso!')

    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado!')

    voltar_ao_menu_principal()

def opcao_invalida():
#!função para caso o cliente fazer uma escolha que nao esta sendo perguntada

    print('Opção inválida!\n')
    voltar_ao_menu_principal()


def exibir_subtitulo(texto):
#!função para exibir os titulos

    linha = '*' * (len(texto))
    os.system('cls')
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_restaurante():
    #!função para cadastrar restaurantes

    '''
    inputs: Nome do restaurante
    outputs: Add novo restaurante a lista
    
    '''

    exibir_subtitulo("Cadastro de novos restaurantes")
    nome_restaurante = input('Digite o nome do restaurante:  ')
    restaurantes.append(nome_restaurante)
    print(f"\nO restaurante {nome_restaurante} foi cadastrado com sucesso!")
    voltar_ao_menu_principal()

def listar_restaurante():
#!função para listar os restaurantes que foram cadastrados

    exibir_subtitulo("Lista de restaurantes:\n")

 #! o print abaixo é para fazer colunas para listar melhor as opcoes
    print(f'{'Nome do restaurante:'.ljust(22)} | {'Categoria:'.ljust(20)} | Status:')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['Nome']
        categoria = restaurante['Categoria']
        ativo = 'Ativado' if restaurante['Ativo'] else 'Desativado'

        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()


def finalizar_app():
   #!função para finalizar o programa

    exibir_subtitulo('Finalizando app...')
    

def escolher_opcao():
#!função para escolher a opcao

    try:
        opcao_escolhida = int(input('\nEscolha uma opção:  '))

        match opcao_escolhida:
            case 1:
                cadastrar_restaurante()
            case 2:
                listar_restaurante()
            case 3:
                alternar_estado_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()
def main():

    #!função principal para exibir o programa

    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()


