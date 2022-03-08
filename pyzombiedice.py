# Aluno: Bruno Cesar de Oliveira Franco
# Professor: Galbas Milleo Filho
# Objetivo: Implementação de jogo baseado em ZombieDice na linguagem Python para matéria de Raciocínio Computacional PUCPR.

#Imports
from collections import namedtuple
import random
import time

#Uma função que adiciona um delay no código e uma quebra de linha, para melhorar a usabilidade.
def sleepLineBreak(seconds=1.2):
    #:seconds: Valor número que representa a quantidade de segundos para espera.
    time.sleep(seconds)
    print('')

#Var Jogador
Jogador = namedtuple("Jogador", ["Nome", "Cérebros"])

#Var Dado
Dado = namedtuple("Dado", ["Cor", "Faces"])

class Menu:
    def __init__(self):
        self.__jogadores = Jogadores()
        self.__rodada = Rodada(self.__jogadores.getJogadores())

    #Função principal da partida, faz um loop de rodadas até possuir ao menos um jogador que conseguiu comer 13 ou mais cérebros.
    def __iniciarJogo(self):
        """
        Função principal da partida, faz um loop de rodadas até possuir ao menos um jogador que conseguiu comer 13 ou mais cérebros.
        """
        print('Boa Jogatina!')
        while self.__rodada.continuarJogo():
            self.__rodada.jogarRodada(self.__jogadores.getJogadores())
            self.__jogadores.listarPontos()
        vencedor = self.__rodada.buscarVencedor(
            self.__jogadores.getJogadores())

        print("**************\n\n**************\nE o vencedor foi:")
        sleepLineBreak()
        print(vencedor.Nome,
              "!!! Que comeu", vencedor.Cérebros, "Cérebros!!!!!!\n\n**************")
        sleepLineBreak()

    #Função inicial, da ação a escolha do usuário entre adicionar ou listar jogadores, começar a partida (é necessário ao menos 2 jogadores) ou sair.
    def menu(self):
        """
        Função inicial, da ação a escolha do usuário entre adicionar ou listar jogadores, começar a partida (é necessário ao menos 2 jogadores) ou sair.
        """
        while True:
            decisao = self.__escolherMenu()
            if(decisao == 1):
                self.__jogadores.adicionarJogadores()
            elif(decisao == 2):
                sleepLineBreak(0.6)
                self.__jogadores.listarJogadores()
                sleepLineBreak()
            elif(decisao == 3):
                if(len(self.__jogadores.getJogadores()) <= 1):
                    print(
                        '\nSão necessários ao menos dois jogadores para iniciar o jogo\n')
                else:
                    for jogador in self.__jogadores.getJogadores():
                        print('Jogador:', jogador.Nome, ' | ' 'Cérebros:', jogador.Cérebros)
                    self.__iniciarJogo()
                    break
            else:
                print('\nAté breve e volte logo :D\n')
                print('\nDesenvolvido por: Bruno Franco\n')
                break
   
    #Função que solicita ao usuário a esccolha entre uma das opções de adicionar ou listar jogadores, começar a partida ou sair.
    def __escolherMenu(self):
        """
        Função que solicita ao usuário a esccolha entre uma das opções de adicionar ou listar jogadores, começar a partida ou sair.
        :return: número referente a escolha
        """
        while True:
            try:
                decisao = int(
                    input('\n1 - Adicionar jogadores\n2 - Listar jogadores da partida\n3 - Jogar\n4 - Sair\n\nQuero a opção número: '))
                if(decisao >= 1 and decisao <= 4):
                    return decisao
                else:
                    print('\n\nPor favor, escolha uma opção válida\n\n')
            except:
                print('\n\nPor favor, digite o número da escolha\n\n')

class Jogadores:

    def __init__(self):
        self.__jogadores: Jogador = []

    #Função para buscar jogadores cadastrados
    def getJogadores(self):
        """
        :return: Retorna os jogadores cadastrados.
        """
        return self.__jogadores

    #Função que pergunta o nome do jogodor para registro
    def inputJogador(self):
        """
        #:return: Retorna um Jogador com nome inserido pelo usuário e uma contagem inicial de 0 cérebros.
        """
        nome = input("Informe nome do jogador: ")
        return Jogador(nome, 0)

    #Função que verifica se o um jogador já está ou não cadastrado em jogadores
    def __verificarExistentes(self, jogador):
        """
        #:return: retorna um booleano indicando se existe ou não na lista de jogadores.
        """
        if(jogador in self.__jogadores):
            print("\nEsse jogador já está registrado\n")
            return True
        return False

    #Função que atualiza um jogador, caso ele já esteja cadastrado, será solicitado um novo valor para atualização.
    def atualizarJogador(self, jogador):
        """
        #:jogador: Jogador que será atualizado.
        """
        nome = input("Qual será o novo nome do jogador? ")
        jogadorAtualizado = Jogador(nome, 0)
        while self.__verificarExistentes(jogadorAtualizado):
            self.atualizarJogador(jogadorAtualizado)
        index = self.__jogadores.index(jogador)
        self.__jogadores[index] = jogadorAtualizado

    #Função que solicita ao usuário a escolha de uma das opções quando o usuário tenta cadastrar um nome de jogador já existente.
    def __mesmoNome(self, jogador):
        """
        Função que solicita ao usuário a escolha de uma das opções quando o usuário tenta cadastrar um nome de jogador já existente.
        :jogador: dados do Jogador que houve a tentativa de inserção.
        """
        while True:
            try:
                decisao = int(input(
                    '\nJá existe um jogador com esse nome, o que deseja fazer?\n\n1 - Mudar o nome dos dois jogadores?\n2 - Trocar o nome de inserção?\n3 - Sair\n\nQuero a opção número: '))
                if(decisao == 1):
                    self.atualizarJogador(jogador)
                    self.adicionarJogadores()
                    break
                elif(decisao == 2):
                    self.adicionarJogadores()
                    break
                elif(decisao == 3):
                    break
                else:
                    print('\n\nPor favor, escolha uma opção válida\n\n')
            except:
                print('\n\nPor favor, digite o número da escolha\n\n')

    #Função para adicionar jogador a lista de jogadores.
    def adicionarJogadores(self):
        """
        Função para adicionar jogador a lista de jogadores.
        """
        while True:
            jogador = self.inputJogador()
            if(jogador in self.__jogadores):
                self.__mesmoNome(jogador)
                break
            else:
                self.__jogadores.append(jogador)
            if(input('Deseja adicionar outro jogador? (s/n)') == 'n' or 'N' or 'Não' or 'NÃO' or 'Nao' or 'NAO'):
                break
            else:
                continue

    #Função que traz o nome e o número dos jogadores cadastrados.    
    def listarJogadores(self):
        """
        Função que traz o nome e o número dos jogadores cadastrados.
        """
        for index, jogador in enumerate(self.__jogadores):
            print('\n'+str(index+1)+'º - '+jogador.Nome)

    #Função que traz a pontuação por nome dos jogadores cadastrados
    def listarPontos(self):
        """
        Função que traz a pontuação por nome dos jogadores cadastrados
        """
        print('\nPONTUAÇÃO ATUAL\n')
        for jogador in self.__jogadores:
            print('\n'+jogador.Nome+": "+str(jogador.Cérebros))

class Pontuacao:
    def __init__(self):
        self.__pontuacaoTemp = {
            "Cérebros": 0,
            "Tiros": 0
        }

    #Função que acrescenta Cérebros ou Tiros na pontuação temporaria da rodada.
    def pontuacaoTemporaria(self, face: str, ):
        """
        Função que acrescenta Cérebros ou Tiros na pontuação temporaria da rodada.
        :face: Face de cima da rolagem do dado.
        """
        if(face == "C"):
            self.__pontuacaoTemp["Cérebros"] += 1
        elif(face == "T"):
            self.__pontuacaoTemp["Tiros"] += 1

    #Função que pega pontuação temporaria.
    def getPontuacaoTemporaria(self):
        return self.__pontuacaoTemp

    #Função que atualiza a pontuação de um jogador.
    def pontuarRodada(self, jogador, jogadores):
        """
        Função que atualiza a pontuação de um jogador.
        :jogador: Jogador que será atualizado na lista de jogadores.
        :jogadores: lista de Jogadores da partida.
        """
        jogadorAtualizado = Jogador(
            jogador.Nome, (jogador.Cérebros+self.__pontuacaoTemp["Cérebros"]))
        index = jogadores.index(jogador)
        jogadores[index] = jogadorAtualizado

class Copo:

    def __init__(self):
        self.__copo: Dado = []
        self.__dadosRepetir = []
        self.__dadosUtilizados = []

    def setDadosRepetir(self, dado):
        """
        Função que incrementa um dado a lista de dados que serão utilizados caso o jogador jogue novamente.
        :dado: Dado que rolou Passo.
        """
        self.__dadosRepetir.append(dado)

    def setDadosUtilizados(self, dado):
        """
        Função que incrementa um dado a lista de dados pontuados pelo jogador.
        :dado: Dado que rolou Tiro ou Cérebro.
        """
        self.__dadosUtilizados.append(dado)

    def recolocarCopo(self):
        """
        Função que devolve os dados utilizados pelo jogador ao copo.
        """
        self.__copo.extend(self.__dadosUtilizados)
        self.__dadosUtilizados.clear()

    def resetDadosRepetir(self):
        """
        Função que limpa os valores contidos na lista dadosRepetir
        """
        self.__dadosRepetir.clear()

    def getDadosRepetir(self):
        """
        Função que retorna os valores da lista de dadosRepetir
        :return: Dados que rolaram Passo na jogada anterior
        """
        return self.__dadosRepetir

    def getCopo(self):
        """
        Função que retorna os todos os dados do copo
        :return: Dados restantes do copo
        """
        return self.__copo

    def __traduzirFace(self, face: str):
        """
        Função que recebe uma letra e retorna a palavra correspondente.
        :face: Letra correspondente a rolagem do dado.
        :return: Retorna a palavra correspondente a letra
        """
        if(face == "C"):
            return "Cérebro"
        elif(face == 'P'):
            return "Passo"
        else:
            return "Tiro"

    def __dadosVerdes(self):
        """
        Função que adiciona um dado Verde e suas faces ao copo
        """
        dadoVerde = Dado('Verde', 'CPCTPC')
        self.__copo.append(dadoVerde)

    def __dadosAmarelos(self):
        """
        Função que adiciona um dado Amarelo e suas faces ao copo
        """
        dadoAmarelo = Dado('Amarelo', 'TPCTPC')
        self.__copo.append(dadoAmarelo)

    def __dadosVermelhos(self):
        """
        Função que adiciona um dado Vermelho e suas faces ao copo
        """
        dadoVermelho = Dado('Vermelho', 'TPTCPT')
        self.__copo.append(dadoVermelho)

    def criarCopo(self):
        """
        Função que adiciona 6 dados Verdes, 4 dados Amarelos e 3 dados Vermelhos ao copo.
        """
        self.__copo.clear()
        self.__dadosUtilizados.clear()
        for i in range(6):
            self.__dadosVerdes()
        for i in range(4):
            self.__dadosAmarelos()
        for i in range(3):
            self.__dadosVermelhos()

    def __rolarDado(self, dado):
        """
        Função que rola um dado.
        :dado: Dado a ser rolado
        :return: Retorna a Face que ficou para cima do dado.
        """
        faceCima = random.choice(dado.Faces)
        print('No dado', dado.Cor, 'a face de cima foi:',
              self.__traduzirFace(faceCima))
        return faceCima

    def tirarDado(self):
        """
        Função que retira um dado aleatorio do copo.
        :return: Retorna um dado.
        """
        index = random.randint(1, len(self.__copo))
        index -= 1
        dado = self.__copo.pop(index)
        return dado

    def selecionarDados(self):
        """
        Função que seleciona 3 dados que serão jogados. Estes dados serão uma combinação dos dados que rolagem Passo na jogada anterior e novos.
        :return: Retorna 3 dados.
        """
        selecionados = []
        for i in range((3 - len(self.__dadosRepetir))):
            dado = self.tirarDado()
            selecionados.append(dado)
        if(len(self.__dadosRepetir) > 0):
            selecionados.extend(self.__dadosRepetir)
            self.resetDadosRepetir()
        for i, dado in enumerate(selecionados):
            print(str(i+1)+'º dado tem a cor:', dado.Cor)
        return selecionados

    def jogarDados(self, dados):
        """
        Função que rola os dados e os armazena nas listas de dadosRepetir ou dadosUtilizar dependendo do que foi rolado.
        :dados: dados a serem rolados.
        :return: Retorna uma lista contendo os dados e suas respectivas rolagens.
        """
        rolagem = []
        for dado in dados:
            faceCima = self.__rolarDado(dado)
            rolagem.append([dado, faceCima])
            if(faceCima == 'P'):
                self.setDadosRepetir(dado)
            else:
                self.setDadosUtilizados(dado)
        sleepLineBreak()
        return rolagem

class Rodada:
    def __init__(self, jogadores):
        self.__jogadores = jogadores
        self.__copo = Copo()

    def __jogarNovamente(self):
        """
        Função que repete as ações de selecionar dados e jogar dados.
        :return: retorna uma lista de dados com suas respectivas rolagens
        """
        selecionados = self.__copo.selecionarDados()
        sleepLineBreak()
        rolagem = self.__copo.jogarDados(
            selecionados)
        return rolagem

    #Função que solicita ao usuário a escolha entre jogar novamente ou pontuar.
    def __opcaoRodada(self):
        """
        Função que solicita ao usuário a escolha entre jogar novamente ou pontuar,
        :return: Número referente a escolha do usuário
        """
        while True:
            try:
                decisao = int(
                    input('\n1 - Jogar novamente\n2 - Pontuar cérebros\n\nQuero a opção número: '))
                if(decisao >= 1 and decisao <= 2):
                    return decisao
                else:
                    print('\n\nPor favor, escolha uma opção válida\n\n')
            except:
                print('\n\nPor favor, digite o número da escolha\n\n')

    #Função que verifica se o jogador atual tomou mais de dois tiros, pois caso ele tome 3 ele perderá todos os pontos.
    def __verificarVida(self, pontuacao: Pontuacao):
        """
        Função que verifica se o jogador atual tomou mais de dois tiros, pois caso ele tome 3 ele perderá todos os pontos.
        :pontuacao: pontuacao do jogador atual.
        :return: retorna booleano caso jogador ainda possa continuar jogando
        """
        pontuacaoTemp = pontuacao.getPontuacaoTemporaria()
        if(pontuacaoTemp["Tiros"] > 2):
            print("Você tomou", pontuacaoTemp["Tiros"],
                  "tiros e perdeu todos os cérebros que comeu... x_x")
            return False
        else:
            return True

    #Função que possuí a lógica para que um jogador continue jogando a rodada
    def __escolherOpcaoRodada(self, jogador, pontuacao: Pontuacao, jogadores):
        """
        Função que possuí a lógica para que um jogador continue jogando a rodada
        :jogador: jogador atual
        :pontuacao: pontuacao do jogador atual.
        :return: retorna booleano caso jogador ainda possa continuar jogando
        """
        while True:
            if(len(self.__copo.getCopo()+self.__copo.getDadosRepetir()) < 3):
                self.__copo.recolocarCopo()
            print("\nSua pontuação da rodada é:",
                  pontuacao.getPontuacaoTemporaria())
            decisao = self.__opcaoRodada()
            if(decisao == 1):
                rolagem = self.__jogarNovamente()
                for dado in rolagem:
                    pontuacao.pontuacaoTemporaria(dado[1])
                vivo = self.__verificarVida(pontuacao)
                if(not vivo):
                    break
            else:
                pontuacao.pontuarRodada(
                    jogador, jogadores)
                sleepLineBreak()
                break

    #Função que possuí a lógica de cada rodada, percorre a lista de jogadores indicando o turno de cada um.
    def jogarRodada(self, vencedores):
        """
        Função que possuí a lógica de cada rodada, percorre a lista de jogadores indicando o turno de cada um.
        :vencedor: valor opcional para lista de jogadores que empataram.
        """
        print("\nNOVA RODADA\n")
        sleepLineBreak()
        for jogador in (vencedores or self.__jogadores):
            pontuacao = Pontuacao()
            self.__copo.criarCopo()
            print("Vez do jogador", jogador.Nome,
                  "que tem pontuação:", jogador.Cérebros)
            input('\nAperte qualquer tecla para jogar\n\n')
            selecionados = self.__copo.selecionarDados()
            sleepLineBreak()
            rolagem = self.__copo.jogarDados(selecionados)
            for dado in rolagem:
                pontuacao.pontuacaoTemporaria(dado[1])
            vivo = self.__verificarVida(pontuacao)
            if(not vivo):
                continue
            self.__escolherOpcaoRodada(jogador, pontuacao, vencedores)

    def continuarJogo(self):
        """
        Função que verifica se existe algum jogador que conseguiu comer 13 ou mais cérebros.
        :return: retorna um booleano referente a existencia de outra rodada.
        """
        continuar = True
        for jogador in self.__jogadores:
            if jogador.Cérebros >= 13:
                return False
        return continuar

    def buscarVencedor(self, jogadores):
        """
        Função que encontra o jogador que comeu mais cérebros, caso haja empate, haverá uma rodada desempate entre os jogadores com maior score.
        :jogadores: lista de jogadores da partida
        :return: retorna o vencedor da partida.
        """

        maior = max([jogador.Cérebros for jogador in jogadores])
        vencedores = []
        for jogador in (jogadores):
            if jogador.Cérebros == maior:
                vencedores.append(jogador)
        if(len(vencedores) > 1):
            print(
                'Temos um empateeee!! Vamos a rodada desempate com os jogadores:', *vencedores)
            self.jogarRodada(vencedores)
            return self.buscarVencedor(vencedores)
        else:
            vencedor = vencedores[0]
        return vencedor
    pass


#Inicio do Programa
menu = Menu()
menu.menu()