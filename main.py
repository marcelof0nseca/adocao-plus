def cabecalho():
    arquivo_animais = open('animais.txt', 'a', encoding='utf-8')
    arquivo_animais.close()

    arquivo_animais = open('animais.txt', 'r', encoding='utf-8')
    conteudo = arquivo_animais.read()
    arquivo_animais.close()

    if conteudo.strip() == "":
        arquivo_animais = open('animais.txt', 'a', encoding='utf-8')
        arquivo_animais.write(f"|{'NOME':^12}|{'ESPÉCIE':^12}|{'RAÇA':^12}|{'IDADE':^7}|{'SEXO':^6}|{'ESTADO DE SAÚDE':^20}|{'DATA DE CHEGADA':^20}|{'COMPORTAMENTO':^18}|\n")
        arquivo_animais.close()

        


def organizarTexto(texto):
    print('-' * len(texto))
    print(texto)
    print('-' * len(texto))


def adicionarAnimal():
    arquivo_animais = open('animais.txt', 'a', encoding='utf-8')

    nome = str(input('Digite o nome do animal: ')).capitalize()
    especie = str(input('Digite a espécie do animal: ')).capitalize()
    raca = str(input('Digite a raça do animal: ')).capitalize()
    idade = str(input('Digite a idade do animal: ')).capitalize()
    sexo = str(input('Digite o sexo do animal: ')).capitalize()
    estado = str(input('Digite o estado de saúde do animal: ')).capitalize()
    data = str(input('Digite a data de chegada do animal: '))
    comportamento = str(input('Digite o comportamento do animal: ')).capitalize()

    arquivo_animais.write(f'|{nome:^12}|{especie:^12}|{raca:^12}|{idade:^7}|{sexo:^6}|{estado:^20}|{data:^20}|{comportamento:^18}|\n')
    print('Animal cadastrado com sucesso!')
    arquivo_animais.close()


def visualizarAnimais():
    arquivo_animais = open('animais.txt', 'r', encoding='utf-8')
    print(arquivo_animais.read())
    arquivo_animais.close()



cabecalho()
print('Sistema de Gestão para Centros de Adoção de Animais')
while True:
    try:
        questionamento = int(input('1. Adicionar Animal\n2. Visulizar Animais\n3. Editar Animal\n4. Excluir Animal\n5. Sair\nDigite a opção desejada: '))
    except ValueError:
        print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
        continue
    except KeyboardInterrupt:
        print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
        continue
    else:
        if questionamento == 1:
            adicionarAnimal()
        elif questionamento == 2:
            visualizarAnimais()
        elif questionamento == 3:
            print('Em construção')
        elif questionamento == 4:
            print('Em construção')
        elif questionamento == 5:
            print('Saindo...')
            break
        else:
            print('Digite uma opção valida!')
            continue
