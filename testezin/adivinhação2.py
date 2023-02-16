#usando for ao inves de while
print("**********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("**********************************")

numero_secreto = 42
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):
    print(f"Tentativa {rodada} de {total_de_tentativas}:")
    chute = input("Digite o seu numero: ")
    print(f'Você digitou {chute}')

    chute_int = int(chute)

    acertou = chute_int == numero_secreto
    chute_maior = chute_int > numero_secreto
    chute_menor = chute_int < numero_secreto

    if acertou:
        print("Você acertou!")
        break
    else:
        if chute_maior:
            print("Você errou! O chute foi maior")
        elif chute_menor:
            print("Você errou! O chute foi menor")
    rodada = rodada + 1
print("Fim do jogo")