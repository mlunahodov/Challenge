from time import sleep
from os import system


def validar_nome(nome):
    if nome.replace(' ', '').isalpha() == False:
        return False

    return True


def validar_cpf(cpf):
    primeiro = cpf[0]
    contador = 0
    for i in cpf:
        if i == primeiro:
            contador += 1

    if cpf.isdigit() == False or len(cpf) != 11 or contador == 11:
        return False

    lista_cpf = [i for i in cpf]
    lista_nove_primeiros = [i for i in cpf[0:-2]]
    lista_dez_primeiros = [i for i in lista_cpf[0:-1]]
    valores_primeiro_digito = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    valores_segundo_digito = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    soma = 0

    for i, j in enumerate(lista_nove_primeiros):
        soma += int(j) * int(valores_primeiro_digito[i])

    resto = soma % 11

    if resto < 2:
        lista_cpf[9] = '0'
    else:
        lista_cpf[9] = str(11 - resto)

    soma = 0

    for i, j in enumerate(lista_dez_primeiros):
        soma += int(j) * int(valores_segundo_digito[i])

    resto = soma % 11

    if resto < 2:
        lista_cpf[10] = '0'
    else:
        lista_cpf[10] = str(11 - resto)

    cpf_validado = ''.join(lista_cpf)

    for i in usuarios:
        if cpf in i:
            return False

    if cpf == cpf_validado:
        return True



def cadastrar_usuario():
    system('cls')
    print('----------ÁREA DE CADASTRO DE USUÁRIO----------')

    nome = input('Nome: ')

    while validar_nome(nome) == False:
        print('Nome deve conter apenas letras.')

        nome = input('Nome: ')

        validar_nome(nome)

    cpf = input('CPF (apenas digitos): ')

    while validar_cpf(cpf) == False:
        system('cls')
        print('CPF inválido ou já cadastrado!')
        print('''[ 1 ] Tentar Novamente
[ 2 ] Sair.''')

        escolha = input('Opção: ')

        match escolha:
            case '1':
                cpf = input('CPF (apenas digitos): ').strip()
                validar_cpf(cpf)
            case '2':
                return False
            case _:
                print('Escolha inválida.')
                break


    placa_carro = input('Placa do carro: ')

    system('cls')
    print('Cadastro realizado com sucesso!')
    print('Estamos te encaminhando para a área do cliente...')
    sleep(3)
    system('cls')

    global cpf_logado
    cpf_logado = cpf
    usuarios.append((nome, cpf, placa_carro))


def login():
    while True:
        system('cls')
        print('----------ÁREA DE LOGIN----------')

        nome = input('Nome: ')
        cpf = input('CPF (apenas digitos): ')
        placa = input('Placa do carro: ')
        dados = (nome, cpf, placa)

        if dados in usuarios:
            system('cls')
            print('Login realizado com sucesso!')
            print('Estamos te encaminhando para a área do cliente.')
            sleep(3)
            global cpf_logado
            cpf_logado = cpf
            return True
        else:
            system('cls')
            print('Os dados fornecidos não estão cadastrados no sistema.')
            sleep(2)

        print('''OPÇÕES:
[ 1 ] Tentar novamente
[ 2 ] Voltar ao menu principal''')

        escolha = input('Escolha: ')

        if escolha == '1':
            system('cls')
            continue
        elif escolha == '2':
            system('cls')
            return False
        else:
            print('Por favor, escolha uma opção válida')


def area_cliente():
    while True:
        system('cls')
        print('''----------OPÇÕES PARA CLIENTES----------
[ 1 ] Agendar Vistoria
[ 2 ] Pedir Guincho
[ 3 ] Ver Meus Dados
[ 4 ] Serviços Mecânicos
[ 5 ] Serviços Elétricos
[ 6 ] Sair''')

        escolha = input('Opção: ')

        if escolha == '1':
            vistoria()
        elif escolha == '2':
            guincho()
        elif escolha == '3':
            mostrar_dados()
        elif escolha == '4':
            servicos_mecanicos()
        elif escolha == '5':
            servicos_eletricos()
        elif escolha == '6':
            break
        else:
            print('Escolha inválida.')


def vistoria():
    system('cls')
    print('----------MARCAR VISTORIA----------')

    data = input('Para quando quer marcar a vistoria (dd/mm/aaaa)? ')
    local = input('Em qual oficina? ')

    print(f'Sua vistoria foi marcada para a data {data} na oficina {local}.')
    sleep(3)

    return (data, local)


def guincho():
    while True:
        system('cls')
        print('----------PEDIR GUINCHO----------')

        localizacao = input('Onde seu carro está? ')

        print(f'Estamos enviando um guincho para a localização informada ({localizacao}).')
        sleep(3)
        break


def mostrar_dados():
    system('cls')
    print('----------DADOS DO USUÁRIO----------')

    for i in usuarios:
        if cpf_logado in i:
            print(f'Nome: {i[0]}')
            print(f'CPF: {i[1]}')
            print(f'Placa: {i[2]}')

    sair = input('Pressione ENTER para sair. ')

    if sair:
        return None


def servicos_mecanicos():
    while True:
        system('cls')
        print('''----------SERVIÇOS MECÂNICOS----------
[ 1 ] Trocar Óleo e Filtros
[ 2 ] Verificar e ajustar fluidos
[ 3 ] Reparar motor e transmissão
[ 4 ] Trocar correias e mangueiras
[ 5 ] Voltar ao Menu Cliente''')

        escolha = input('Opção: ')

        match escolha:
            case '1':
                system('cls')
                print('\nVerificando.')
                sleep(1)
                system('cls')
                print('\nVerificando..')
                sleep(1)
                system('cls')
                print('\nVerificando...')
                sleep(1)
                print('A troca de óleo e filtros foi realizada!')
                sleep(2)
            case '2':
                system('cls')
                print('\nVerificando.')
                sleep(1)
                system('cls')
                print('\nVerificando..')
                sleep(1)
                system('cls')
                print('\nVerificando...')
                sleep(1)
                print('Os fluídos foram verificados e ajustados!')
                sleep(2)
            case '3':
                system('cls')
                print('\nVerificando.')
                sleep(1)
                system('cls')
                print('\nVerificando..')
                sleep(1)
                system('cls')
                print('\nVerificando...')
                sleep(1)
                print('Seu motor e transmissão foram reparados!')
                sleep(2)
            case '4':
                system('cls')
                print('\nVerificando.')
                sleep(1)
                system('cls')
                print('\nVerificando..')
                sleep(1)
                system('cls')
                print('\nVerificando...')
                sleep(1)
                print('Suas correias e mangueiras foram trocadas!')
                sleep(2)
            case '5':
                break
            case _:
                system('cls')
                print('\nOpção inválida, digite uma opção válida!')
                sleep(2)


def servicos_eletricos():
    while True:
        system('cls')
        print('''----------SERVIÇOS ELÉTRICOS----------
[ 1 ] Trocar bateria
[ 2 ] Instalar novo sistema de iluminação
[ 3 ] Reparar sistema de ignição e partida
[ 4 ] Voltar ao Menu Cliente''')

        escolha = input('Opção: ')

        match escolha:
            case '1':
                system('cls')
                print('\nVerificando.')
                sleep(1)
                system('cls')
                print('\nVerificando..')
                sleep(1)
                system('cls')
                print('\nVerificando...')
                sleep(1)
                print('Sua bateria foi trocada!')
                sleep(2)
            case '2':
                system('cls')
                print('\nVerificando.')
                sleep(1)
                system('cls')
                print('\nVerificando..')
                sleep(1)
                system('cls')
                print('\nVerificando...')
                sleep(1)
                print('Seu novo sistema de iluminação foi instalado!')
                sleep(2)
            case '3':
                system('cls')
                print('\nVerificando.')
                sleep(1)
                system('cls')
                print('\nVerificando..')
                sleep(1)
                system('cls')
                print('\nVerificando...')
                sleep(1)
                print('Seu sistema de ignição e partida foram reparados!')
                sleep(2)
            case '4':
                break
            case _:
                system('cls')
                print('\nOpção inválida, digite uma opção válida!')
                sleep(2)


def main():
    while True:
        system('cls')
        print('''----------MENU DE OPÇÕES----------
[ 1 ] Fazer Cadastro
[ 2 ] Fazer Login
[ 3 ] Sair''')

        escolha = input('Escolha uma opção: ')

        if escolha == '1':
            if cadastrar_usuario() != False:
                area_cliente()
        elif escolha == '2':
            if login() == True:
                area_cliente()
            else:
                continue
        elif escolha == '3':
            system('cls')
            print('Volte sempre! :D')
            sleep(1)
            break
        else:
            system('cls')
            print('Opção inválida. Por favor, escolha novamente.')
            sleep(2)

if __name__ == '__main__':
    cpf_logado = ''
    usuarios = []
    main()