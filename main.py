arquivo_animais = open('animais.csv', 'a', encoding='utf-8')
def organizarTexto(texto):
    print('-' * len(texto))
    print(texto)
    print('-' * len(texto))


def adicionarAnimal():
    nome = str(input('Digite o nome do animal: '))
    especie = str(input('Digite a especie do animal: '))
    raca = str(input('Digite a raca do animal: '))  
    idade = str(input('Digite a idade do animal: '))
    sexo = str(input('Digite o sexo do animal: '))
    arquivo_animais.write(f'{nome};{especie};{raca};{idade};{sexo}\n')
    print('Animal cadastrado com sucesso!')


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
            print('Em construção')
        elif questionamento == 3:
            print('Em construção')
        elif questionamento == 4:
            print('Em construção')
        elif questionamento == 5:
            arquivo_animais.close()
            print('Saindo...')
            break
        else:
            print('Digite uma opção valida!')
            continue
