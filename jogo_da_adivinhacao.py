import random


def jogar_jogo_da_adivinhacao():
    print("********************************")
    print("Bem vindo ao jogo de adivinhação")
    print("********************************")
    print(" ")

    rodada: int = 0
    numero_secreto: int = 0
    total_de_tentativas = 1
    pontos = 1000

    print("Qual o nível de dificuldade você deseja??")
    dificuldade = int(input("1 - Fácil \n2 - Médio\n3 - Difícil\nDigite o número da sua escolha: "))

    while dificuldade > 3 or dificuldade < 1:
        dificuldade = int(input("Você digitou uma opção inválida, digite entre 1 e 3 para escolher a dificuldade:"))
    if dificuldade == 1:
        numero_secreto = random.randint(1, 10)
        rodada: int = 3
    elif dificuldade == 2:
        numero_secreto = random.randint(1, 50)
        rodada: int = 5
    elif dificuldade == 3:
        numero_secreto = random.randint(1, 100)
        rodada: int = 10

    while total_de_tentativas <= rodada:
        print(f"Tentativa {total_de_tentativas} de {rodada}: ")
        chute_str = input("Digite um número: ")
        print(f"Você digitou: {chute_str}.")
        chute = int(chute_str)
        total_de_tentativas = total_de_tentativas + 1

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("Você acertou!")
            print(f"Sua pontuação foi {pontos}.")
            break
        else:
            if maior:
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif menor:
                print("Você errou! O seu chute foi menor que o número secreto.")

        pontos = pontos - abs(numero_secreto - chute)
    print(f"Sua pontuação foi {pontos}.")
    print(f"O número correto era {numero_secreto}!!")
    print("Fim do jogo")


if __name__ == "__main__":
    jogar_jogo_da_adivinhacao()
