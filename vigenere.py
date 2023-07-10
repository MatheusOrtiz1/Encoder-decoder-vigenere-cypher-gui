import PySimpleGUI as sg

sg.theme('DarkAmber')   # Tema
# Todos os elementos dentro da janela.
layout = [  [sg.Text('Texto a ser cifrado'), sg.InputText(key='texto_entrada')],
            [sg.Text('Chave'), sg.InputText(key='chave_entrada')],
            [sg.Button('Cifrar'), sg.Button('Decifrar')],
            [sg.Text('Texto cifrado/decifrado'), sg.Output(size=(40, 5), key='texto_saida')]]

# Cria a janela
window = sg.Window('Cifra de Vigenere', layout)

# Loop de eventos para processar "eventos" e obter os "valores" das entradas
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: # Se o usuário fechar a janela ou clicar em cancelar
        break
    if event == 'Cifrar':
        # pegando o texto a ser encifrado
        palavra_pura = values['texto_entrada']

        # pegando chave a ser utilizada no ciframento
        chave = values['chave_entrada']

        # variaveis de controle
        nova_palavra = ""
        i = 0

        # laco de repeticao para modificar a palavra
        for letra in palavra_pura:
            # verificando se e letra
            if letra.isalpha():
                valor = ord(letra)
                # verificando se e letra maiuscula
                if letra.isupper():
                    # adicionando valor da chave da letra
                    valor += ord(chave[i % len(chave)].upper()) - 65
                    # cobrindo o caso do valor passar de 'Z'
                    if valor > ord("Z"):
                        valor -= 26
                # verificando se e letra minuscula
                else:
                    # adicionando valor da chave da letra
                    valor += ord(chave[i % len(chave)].lower()) - 97
                    # cobrindo o caso do valor passar de 'z'
                    if valor > ord("z"):
                        valor -= 26
                i += 1
                nova_palavra += chr(valor)
            else:
                nova_palavra += letra

        # pegando a palavra cifrada e mostrando na area correspondente
        window['texto_saida'].update(nova_palavra)

    elif event == 'Decifrar':
        # pegando o texto a ser decifrado
        palavra_cifrada = values['texto_entrada']

        # pegando chave usada no ciframento
        chave = values['chave_entrada']

        # variaveis de controle
        nova_palavra = ""
        i = 0

        # laco de repeticao para modificar a palavra
        for letra in palavra_cifrada:
            # verificando se e letra
            if letra.isalpha():
                valor = ord(letra)
                # verificando se e letra maiuscula

                if letra.isupper():
                    # subtraindo valor da chave da letra
                    valor -= ord(chave[i % len(chave)].upper()) - 65

                    if valor < ord("A"):
                        valor += 26

                else:
                    # subtraindo valor da chave da letra
                    valor -= ord(chave[i % len(chave)].lower()) - 97

                    if valor < ord("a"):
                        valor += 26

                i += 1

                nova_palavra += chr(valor)

            else:
                nova_palavra += letra

        window['texto_saida'].update(nova_palavra)

window.close()
