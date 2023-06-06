import jogo_de_forca
import jogo_da_adivinhacao


def escolhe_jogo():
    print("********************************")
    print("*******Escolha o seu jogo*******")
    print("********************************")
    print(" ")

    print("Para escolher seu jogo digite:\n1 - Para forca\n2 - Para adivinhação")
    escolha = int(input("Faça sua escolha[1 ou 2]: "))

    if escolha == 1:
        print("Jogo da forca iniciado!")
        jogo_de_forca.jogar_jogo_da_forca()
    elif escolha == 2:
        print("Jogo da adivinhação iniciado!")
        jogo_da_adivinhacao.jogar_jogo_da_adivinhacao()


if __name__ == "__main__":
    escolhe_jogo()
