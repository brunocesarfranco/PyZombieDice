# Aluno: Bruno Cesar de Oliveira Franco
# RA: 1112022100423
# Curso: Analise e Desenolvimento de Sistemas
# Professor: Galbas Milleo Filho
# Objetivo: Implementação protótipo (4ª semana) de jogo baseado em 
#           ZombieDice na linguagem Python para matéria
#           de Raciocínio Computacional PUCPR.
#Repositório: https://github.com/brunocesarfranco/PyZombieDice

#Importando biblioteca random para numeros aleatorios
import random

#Inicio de jogo
start=0

# Numero de Jogadores
num_players=2

# Numero total de turnos no jogo
max_turns=num_players * 500

# Pontuação requerida para vitoria
winning_score=13

# Numero total de dados
max_dice=13

# Numero de fases dos dados
max_sides=6

# Pontuação Inicial
scores = [0] * num_players

# Numero de dados selecionados no turno
dice_per_turn = 3

# Define a diferença entre os dados
# O ultimo elemento do array define a cor
master_green_die = ["cerebro", "cerebro", "cerebro", "correr", "correr", "shotgun", "verde"]

master_yellow_die = ["cerebro", "cerebro", "correr", "correr", "shotgun","shotgun" , "amarelo"]

master_red_die = ["cerebro", "correr", "correr",  "shotgun", "shotgun", "shotgun",  "vermelho"]

# Define os dados que o jogo usará com base no número máximo de lados do dado
green_die = []
yellow_die = []
red_die = []
for i in range(0, max_sides):
    green_die.append(master_green_die[i % (len(master_green_die) - 1)])
    yellow_die.append(master_yellow_die[i % (len(master_yellow_die) - 1)])
    red_die.append(master_red_die[i % (len(master_red_die) - 1)])
green_die.append("verde")
yellow_die.append("amarelo")
red_die.append("vermelho")

# Define a quantidade de dados disponiveis em jogo
# 6 dados verdes, 4 dados amarelos e 3 dados vermelhos
dice=[green_die, green_die, green_die, green_die, green_die, green_die, yellow_die, yellow_die, yellow_die, yellow_die, red_die, red_die, red_die]


# Verificando que os valores selecionados para as variáveis do jogo não quebram o jogo
if dice_per_turn > max_dice:
    print ("O número de dados selecionado excede a quantidade de dados totais em jogo (", dice_per_turn, ">", max_dice, ")")
    raise SystemExit

if (start == 0):
  print("Seja bem-vindo ao ZombieDice!\n")
for j in range(0, max_turns):
    print ("Pontuação atual")
    for i in range(0, num_players):
        print ("Jogador", i+1, ":", scores[i])
    print ("Jogador ",(j%num_players)+1,"'s joga...")
    print ("")
    input ("Pressione Enter para jogar os dados...")

    # Contadores
    brains = 0
    shotguns = 0

    # As seleções de dados são predeterminadas, mas os jogadores não sabem disso
    dice_selections = random.sample(range(0, max_dice), max_dice)

    # Seleciona o dado pra jogar
    # A primeira vez que os dados rolados são simplesmente os três primeiros selecionados
    dice_to_roll = []
    for dice_pulled in range(0, dice_per_turn):
        dice_to_roll.append(dice_selections[dice_pulled])

    roll_again = "sim"
    # Enquanto o jogador quer continuar rolando...
    while roll_again == "sim" or roll_again == "s":
        # Joga o dado...
        print ("")
        print ("Dados retirados: ")

        for i in range(0, dice_per_turn):
            roll = dice[dice_to_roll[i]][(random.randint(0, max_sides - 1))]
            print(dice[dice_to_roll[i]][max_sides], " - ", roll)

            # Se o jogador tirar um cérebro, adicione um ao total de cérebros para esta rodada e selecione outro dado
            # Se o jogador tirar uma espingarda, adicione uma ao total de espingardas para esta rodada e selecione outro dado
            # Se o jogador tirar um corredor, não faça nada e não selecione outro dado
            if roll == "cerebro":
                brains+=1
                dice_to_roll[i] = dice_selections[dice_pulled]
                dice_pulled+=1
            elif roll == "shotgun":
                shotguns+=1
                dice_to_roll[i] = dice_selections[dice_pulled]
                dice_pulled+=1
                
        print ("cerebros = ", brains, "; shotguns = ", shotguns)
        # Se o jogador não tiver rolado três espingardas, pergunta se ele quer continuar rolando
        if shotguns < 3:
            roll_again = input("Você quer jogar novamente? (S/N)")
        else:
            break
    
    # Se o jogador não rolou três espingardas, adicione o número de cérebros que rolou à sua pontuação total
    if shotguns < 3:
        scores[j%num_players]+=brains
        # Verifique se o jogador tem cérebros o suficiente para vencer
        if scores[j%num_players] >= winning_score:
            print ("Jogador", j%num_players+1, "ganhou!")
            raise SystemExit
        else:
            print ("Sua pontuação é",scores[j%num_players])
    else:
        print("Argh! Você levou um tiro!!!")

    print ("")