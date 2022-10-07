# metodo pede_num_menu

def pede_num_menu(minimo, maximo, pergunta):
    numero = int(input(pergunta))
    if (numero >= minimo) and (numero <= maximo):
        return numero
    else:
        return pede_num_menu(minimo, maximo,
                             f"Você digitou um valor invalido, por favor digite entre a faixa de valor entre {minimo} a {maximo}\n")




#Class resposável pelas opções do menu
class Jogo():
    #inicia a class
    def __init__(self, map=""):
        self.map = "*"
        self.jogadores = []
        self.escolha = []

    # escolhe o map ou volta o menu através da opçõa 4
    def mapa(self):
        escolha = pede_num_menu(1, 4, """Digite entre 1 a 3 para escolher o map
         1 - *
         2 - @
         3 - #

         4 - Press return to the menu\n\n""")
        map_escolhido = ""
        print("\n" * 100)
        if escolha == 1:
            map_escolhido = "*"
        elif escolha == 2:
            map_escolhido = "@"
        elif escolha == 3:
            map_escolhido = "#"
        else:
            menu()
        self.map = map_escolhido
    #metodo privado caucula o ganhador
    def __ganhou(self):
        print("teste")
        j1 = self.escolha[0]
        j2 = self.escolha[1]
        j3 = self.escolha[2]
        print(j1,j2,j3)
        if (j1 == j2) and (j2 == j3):
            print("Jogo empatado")
        elif (  (j1 == 1) and (j2 == 2) and (j3 == 2) ) or ( (j1 == 2) and (j2 == 3) and (j3 == 3)  ) or ( (j1 == 3) and (j2 == 1) and (j3 == 1)  ):
            print( 10 * "JOGADOR 1 WINS !!!\n")
        elif (  (j2 == 1) and (j1 == 2) and (j3 == 2) ) or ( (j2 == 2) and (j1 == 3) and (j3 == 3)  ) or ( (j2 == 3) and (j1 == 1) and (j3 == 1)  ):
            print( 10 * "JOGADOR 2 WINS !!!\n")
        elif (  (j3 == 1) and (j1 == 2) and (j2 == 2) ) or ( (j3 == 2) and (j1 == 3) and (j2 == 3)  ) or ( (j3 == 3) and (j1 == 1) and (j2 == 1)  ):
            print( 10 * "JOGADOR 3 WINS !!!\n")
        else:
            print("Empate!!!")


    #Jogo em sí
    def play(self):
        #controlador para nomera os players
        #começa em 1 para estabelecer na posição 0 jogador 1
        c = 1
        while c <= 3:
            jogador = str(input("Digite seu nome: "))
            self.jogadores.append([jogador, {c}])
            c += 1
        c = 0
        #pede entrada de dados para o jogo
        while c <= 2:
            print(40 * self.map)
            print(f"{self.jogadores[c][0]} faça sua escolha")
            print("""
            Digite sua opção
            1 - pedra 
            2 - tesoura
            3 - papel """)
            escolha = int(input("Digite sua escolha: "))
            for x in range(0, 10):
                print(40 * self.map)
            #Guarda a escolha do player
            self.escolha.append(escolha)
            c += 1
        self.__ganhou()


#instancia a class jogo na var jogo para chamar os metodos
jogo = Jogo()
#Menu mostra opções e captura respotas do jogador
def menu():
    # Mostra na tela opções a escolher.
    print("""
    *************************************************
    1 - play
    2 - score
    3 - map

    0 - quit   
    *************************************************

    """, )
    # Captura a opção escholida.
    opcao_menu = pede_num_menu(0, 3, "Digite um número entre 0 a 3\n")
    # executa a opção através da função.
    if opcao_menu == 0:
        print("Jogo finalizado!")
    elif opcao_menu == 1:
        jogo.play()
    elif opcao_menu == 2:
        jogo.score()
    else:
        jogo.mapa()
#inicia o game
menu()


