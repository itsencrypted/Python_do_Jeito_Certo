'''
**P2 Pedra, Papel e Tesoura!**
Nosso objetivo é implementar o jogo "Pedra, Papel e Tesoura", utilizando a linha de comando.

O jogo é bem simples. Teremos 2 jogadores que deverão escolher entre pedra, papel ou tesoura. 
Após ambos terem escolhido com qual objeto jogar, deve-se declarar o resultado segundo as regras seguintes:

I. Pedra vence Tesoura.

II. Tesoura vence Papel.

III. Papel vence Pedra.

IV. Quando ambos são iguais, temos um empate.

Na vida real, ambos os jogadores escolhem ao mesmo tempo, mostrando suas mãos. Ainda não sabemos como fazer isso, 
então nosso programa vai funcionar da seguinte maneira:

I. Ao executar o programa, ele deve escrever o nome do jogo e pedir que o jogador 1 faça sua escolha.

II. O programa aguarda o jogador 1 digitar sua escolha e pressionar Enter

III. O programa pede que o jogador 2 digite sua escolha

IV. O programa aguarda o jogador 2 digitar sua escolha e pressionar Enter

V. O programa analisa as 2 escolhas e declara o campeão ou um empate

Obs: O jogador 1 está em clara desvantagem, pois o jogador 2 escolhe já sabendo como ganhar. 
Não se preocupe com isso agora, mantenha o foco na correta interpretação dos resultados. 
Poderemos corrigir esta desvantagem quando aprendermos a usar alguns módulos da linguagem.
'''
print("Pedra, Papel e Tesoura!")

jogador_1 = input("Joagador_1, escolha: pedra, papel ou tesoura.\n").lower()
jogador_2 = input("Joagador_2, escolha: pedra, papel ou tesoura.\n").lower()

if jogador_1 == 'pedra' and jogador_2 == 'tesoura':
    print("Jogador 1 vence!")
elif jogador_2 == 'pedra' and jogador_1 == 'tesoura':
    print("Jogador 2 vence!")

elif jogador_1 == 'tesoura' and jogador_2 == 'papel':
    print("Jogador 1 vence!")
elif jogador_2 == 'tesoura' and jogador_1 == 'papel':
    print("Jogador 2 vence!")

elif jogador_1 == 'pedra' and jogador_2 == 'papel':
    print("Jogador 2 vence!")
elif jogador_2 == 'pedra' and jogador_1 == 'papel':
    print("Jogador 1 vence!")


