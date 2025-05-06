def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "futebol"
    enforcou = False
    acertou = False

    while (not enforcou and not acertou):
        chute = input("Qual é a letra?")



        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
                print(F'encontrei a letra{letra} na poscição {index}')
                index = index + 1
    print("jogando...")

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
