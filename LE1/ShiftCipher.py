from unidecode import unidecode
from collections import Counter
import time

# Função de ataque por distribuição de frequência
def frequencia(cipherText):

    #Percentagens de frequência dos caracteres (a-z) em Português.
    # https://www.dcc.fc.up.pt/~rvr/naulas/tabelasPT/
    frequencias = {
        'a': 13.9, 'b': 1.0, 'c': 4.4, 'd': 5.4, 'e': 12.2, 'f': 1.0,
        'g': 1.2, 'h': 0.8, 'i': 6.9, 'j': 0.4, 'k': 0.1, 'l': 2.8,
        'm': 4.2, 'n': 5.3, 'o': 10.8, 'p': 2.9, 'q': 0.9, 'r': 6.9,
        's': 7.9, 't': 4.9, 'u': 4.0, 'v': 1.3, 'w': 0.0, 'x': 0.3,
        'y': 0.0, 'z': 0.4,
    } # Letras mais frequentes: A (13.9) e E (12.2)

    contagem = Counter(i.lower() for i in cipherText if i.isalpha())
    
    # Pega a letra mais comum
    letraFrequente, _ = contagem.most_common(1)[0]
    charAscii = ord(letraFrequente.lower())
    chave = charAscii - 97
    
    # Faz a primeira tentativa com a letra mais freqeunte do português = A
    print(f'Letra mais frequente do texto cifrado: {letraFrequente}')
    print(f'Possível chave: {chave} \n')
    Decriptacao(chave, cipherText)

    # Caso não tenha dado certo faz uma segunda tentativa com a segunda letra mais frequente = E
    letraFrequente2, _ = contagem.most_common(2)[1]
    charAscii2 = ord(letraFrequente2.lower())
    chave2 = charAscii2 - 97
    print(f'Segunda letra mais frequente do texto cifrado: {letraFrequente2}')
    print(f'Possível chave: {chave2} \n')
    Decriptacao(chave2, cipherText)


# Função de ataque de força bruta
def forcaBruta(cipherText):

    for chave in range(1, 26): 
        listaDecriptografado = []
        
        for caracter in cipherText:
            charAscii = ord(caracter.lower())
            
            if charAscii < 97 or charAscii > 122:
                listaDecriptografado.append(caracter)
                continue
            
            charAscii -= chave
                
            # Se o valor ASCII for menor que 97 soma 26 para fazer a volta
            if charAscii < 97:
                charAscii += 26
                
            listaDecriptografado.append(chr(charAscii))
        
        print(f"Possível texto cifrado com chave {chave}:\n{''.join(listaDecriptografado)} \n")


# Função de encriptação
def encriptacao(chave):
    listaCriptografado = []
    plainText = unidecode(input("Digite um texto para ser cifrado: "))

    # Codigo ASCII vai de 97 a 122 (minusculo)

    for caractere in plainText:
        charAscii = ord(caractere.lower())
        chave1 = chave

        while chave1 != 0:

            if charAscii < 97 or charAscii > 122:
                pass

            elif charAscii == 122:
                charAscii = 97

            else: 
                charAscii +=1

            chave1 -= 1      

        listaCriptografado.append(chr(charAscii))

    cipherText = ''.join(listaCriptografado)
    print(f"Seu texto cifrado é \n{cipherText} \n")

# Função de decriptação
def Decriptacao(chave, cipherText):
    # Decriptar é o mesmo que encriptar, só que a chave é negativa
    
    listaDecriptografado = []

    # Codigo ASCII vai de 97 a 122 (minusculo)

    for caractere in cipherText:
        charAscii = ord(caractere.lower())
        chave1 = chave

        while chave1 != 0:
            if charAscii < 97 or charAscii > 122:
                pass

            elif charAscii == 97:
                charAscii = 122

            else: 
                charAscii -=1

            chave1 -= 1          

        listaDecriptografado.append(chr(charAscii))

    print(f"Seu texto em claro é \n{''.join(listaDecriptografado)} \n")
    

# Função principal
def main():
    opcao = int(input(f'Escolha uma opção: \n 1 - Encriptar \n 2 - Decriptar \n 3 - Força Bruta \n 4 - Distribuição de Frequência \n 5 - Sair \n'))

    if opcao < 1 or opcao > 5:
        print("Opção inválida!")
        main()
    
    # Se for as opções de encriptar ou decriptar a chave é necessária
    if opcao == 1 or opcao == 2:
        chave = int(input("Digite a chave k de 0 a 25: ")) % 26    # Caso o usuário digite um número maior que 25, o módulo 26 garante que a chave fique entre 0 e 25.

    if opcao == 1:
        encriptacao(chave)
        main()

    elif opcao == 2:
        cipherText = unidecode(input("Digite o texto cifrado: "))
        Decriptacao(chave, cipherText)
        main()

    elif opcao == 3:
        start = time.time()
        cipherText = unidecode(input("Digite o texto cifrado: "))
        forcaBruta(cipherText)
        print(f"Tempo: {(time.time()-start)*1000:.2f}ms")
        main()
    
    elif opcao == 4:
        start = time.time()
        cipherText = unidecode(input("Digite o texto cifrado: "))
        frequencia(cipherText)
        print(f"Tempo: {(time.time()-start)*1000:.2f}ms")
        main()
    
    elif opcao == 5:
        print("Fim")

main()

