from tkinter import *

# janela principal
janela = Tk()
janela.title("Cifra de Vigenere")
janela.geometry("400x400+200+200")

# FUNCOES

# cifrar texto
def cifrar():
    # pegando o texto a ser encifrado
    palavra_pura = texto_entrada.get()

    # pegando chave a ser utilizada no ciframento
    chave = chave_entrada.get()

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
    texto_saida.delete("1.0", END)
    texto_saida.insert(INSERT, nova_palavra)

# decifrar texto
def decifrar():
    # pegando o texto a ser decifrado
    palavra_cifrada = texto_entrada.get()

    # pegando chave usada no ciframento
    chave = chave_entrada.get()

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
                # cobrindo o caso do valor passar de 'A'
                if valor < ord("A"):
                    valor += 26
            # verificando se e letra minuscula
            else:
                # subtraindo valor da chave da letra
                valor -= ord(chave[i % len(chave)].lower()) - 97
                # cobrindo o caso do valor passar de 'a'
                if valor < ord("a"):
                    valor += 26
            i += 1
            nova_palavra += chr(valor)
        else:
            nova_palavra += letra
    # pegando a palavra decifrada e mostrando na area correspondente
    texto_saida.delete("1.0", END)
    texto_saida.insert(INSERT, nova_palavra)

# WIDGETS

# label da palavra a ser cifrada
texto_label = Label(janela, text="Texto: ")
texto_label.place(x=10, y=10)

# area de texto para entrada da palavra
texto_entrada = Entry(janela)
texto_entrada.place(x=10, y=30, width=380)

# label da chave
chave_label = Label(janela, text="Chave: ")
chave_label.place(x=10, y=60)

# area de texto para entrada da chave
chave_entrada = Entry(janela)
chave_entrada.place(x=10, y=80, width=380)

# botao de cifrar
cifrar_botao = Button(janela, text="Cifrar", command=cifrar)
cifrar_botao.place(x=10, y=110)

# botao de decifrar
decifrar_botao = Button(janela, text="Decifrar", command=decifrar)
decifrar_botao.place(x=60, y=110)

# label da palavra cifrada/decifrada
texto_saida_label = Label(janela, text="Texto Cifrado/Decifrado: ")
texto_saida_label.place(x=10, y=140)

# area de texto para saida da palavra cifrada/decifrada
texto_saida = Text(janela, width=46, height=4)
texto_saida.place(x=10, y=170)

# loop da janela
janela.mainloop()