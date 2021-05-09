import os.path
import random

controle = [] #controla o máximo de jogadas, que é 25, para definir empate
turno = [] #controla de quem é o turno, dependendo do último valor do array

def criaNovoPlayer(): #cria novo player
    print("")
    nome = input("Digite o nome do jogador: ") 
    if os.path.isfile(nome + ".txt"): #verifica se ja existe um arquivo com o nome do jogador digitado
        os.system("cls")
        print("Jogador já existente\n")
    else:
        arquivo = open(nome + ".txt", "w") #caso não exista, um novo arquivo txt dele é criado e aberto para escrever
        arquivo.write("%i\n" %0) #digita a primeira linha, de vitórias, que no início é zero
        arquivo.write("%i\n" %0) #segunda linha, de derrotas
        arquivo.close() #fecha o arquivo
        os.system("cls") #limpa os dados anteriores do terminal (utilizado em todas as funções para não acumular dados)
        print("Jogador {0} registrado" .format(nome))

def excluirPlayer(): #exclui players
    print("")
    nome = input("Digite qual jogador será removido: ")
    if os.path.isfile(nome + ".txt"): #verifica se o jogador existe, e caso existir, executa a exclusão
        os.system("cls")
        print("Jogador {0} removido" .format(nome))
        os.remove(nome + ".txt") #exclui
    else:
        os.system("cls")
        print("Jogador já excluído ou não existente") #se o jogador não for encontrado

def pontos(): #abre e verifica os arquivos do jogador escolhido, e printa de forma organizada as vitórias e derrotas
    print("")
    nome = input("Digite o nome do jogador: ")
    if os.path.isfile(nome + ".txt"): 
        arquivo = open(nome + ".txt")
        pontos = arquivo.readlines() #le todo o arquivo
        vitorias = int(pontos[0]) #adiciona o valor da primeira linha a uma variavel
        derrotas = int(pontos[1]) #adiciona a segunda
        os.system("cls")
        print("Jogador {0}:\n\n  Vitórias: {1} \n  Derrotas: {2}" .format(nome, vitorias, derrotas)) 
    else:
        os.system("cls")
        print("Jogador não existente")

def cj(): #função para explicar como se joga o jogo
    os.system("cls")
    print("")
    print("Quando solicitado os valores em 'X' ou 'Y' digite para 'X' a linha\ndesejada (0 para primeira, 1 para segunda) e 'Y' para a coluna. Por-\ntanto, digitar '(1, 4)' marcará a quinta coluna da segunda linha. \nPara evitar confusão, será sempre indicado de quem é o turno.")

matrizMain = [
    [" "," "," "," "," "], 
    [" "," "," "," "," "],
    [" "," "," "," "," "],  #matriz principal para armazenar as jogadas
    [" "," "," "," "," "],
    [" "," "," "," "," "],
] 

def reset():
    global matrizMain #deixa essa variavel com escopo global, para voltar ela ao normal depois de um jogo
    matrizMain = [[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "],[" "," "," "," "," "]] 

def matriz(): #criar formatação da matriz, para entrada de dados no local certo
    os.system("cls")
    print(" ---------------------")
    print (" | " + matrizMain[0][0] + " | " + matrizMain[0][1] + " | " + matrizMain[0][2] + " | " + matrizMain[0][3] + " | " + matrizMain[0][4] + " | " )
    print(" |---+---+---+---+---|")
    print (" | " + matrizMain[1][0] + " | " + matrizMain[1][1] + " | " + matrizMain[1][2] + " | " + matrizMain[1][3] + " | " + matrizMain[1][4] + " | " )
    print(" |---+---+---+---+---|")
    print (" | " + matrizMain[2][0] + " | " + matrizMain[2][1] + " | " + matrizMain[2][2] + " | " + matrizMain[2][3] + " | " + matrizMain[2][4] + " | " )
    print(" |---+---+---+---+---|")
    print (" | " + matrizMain[3][0] + " | " + matrizMain[3][1] + " | " + matrizMain[3][2] + " | " + matrizMain[3][3] + " | " + matrizMain[3][4] + " | " )
    print(" |---+---+---+---+---|")
    print (" | " + matrizMain[4][0] + " | " + matrizMain[4][1] + " | " + matrizMain[4][2] + " | " + matrizMain[4][3] + " | " + matrizMain[4][4] + " | " )
    print(" ---------------------")

def vit(a): #nesse inicio funciona como a função de verificar os pontos. Abre os arquivos, lê e adiciona as linhas a uma variável, mas possibilita também a edição
    arquivox = open(playerX + ".txt", "r")
    pontosx = arquivox.readlines()
    vitoriasx = int(pontosx[0])
    derrotasx = int(pontosx[1])
    arquivox = open(playerX + ".txt", "w")
    arquivoo = open(playerO + ".txt", "r")
    pontoso = arquivoo.readlines()
    vitoriaso = int(pontoso[0])
    derrotaso = int(pontoso[1])
    arquivoo = open(playerO+ ".txt", "w")
    if a == "x": #se x ganhar, adiciona uma vitoria a ele e uma derrota ao o
        arquivox.write("%i\n" % (vitoriasx + 1))
        arquivox.write("%i\n" % derrotasx)                
        arquivoo.write("%i\n" % vitoriaso)
        arquivoo.write("%i\n" % (derrotaso + 1))
    elif a == "o": #funciona ao contrário da condição acima
        arquivox.write("%i\n" % vitoriasx )
        arquivox.write("%i\n" % (derrotasx + 1))                       
        arquivoo.write("%i\n" % (vitoriaso + 1))
        arquivoo.write("%i\n" % (derrotaso))
    arquivoo.close()
    arquivox.close()
    reset() #reseta a matriz vazia, para que não fique as informações do jogo

def jogoMain():
    global playerX #torna o escopo dessas variaveis global
    global playerO #=
    while True:
        x = random.randint(1, 2) #gera um número aleatório. Se for 1, o jogador "X" começa. 2, "O" começa
        playerX = input("Qual jogador será o 'X'?: ")
        playerO = input("Qual jogador será o 'O'?: ")
        if os.path.isfile(playerX + ".txt"): #verificam a existencia dos players escolhidos. Caso contrário, a função para
            if os.path.isfile(playerO + ".txt"): #=
                matriz() #mostra a matriz vazia
                if x == 1: #usa o número aleatória para escolher o iniciante
                    print ("Jogador {0} começa".format(playerX))
                elif x == 2: #=
                    print ("Jogador {0} começa".format(playerO))
            else:
                print("Jogador {0} não registrado".format(playerO))
                return False
        else:
            print("Jogador {0} não registrado".format(playerX))
            return False
        if x == 1: # "turno" vai ser responsável por chamar a função certa para o jogador certo
            turno.append(x)
        elif x == 2: #=
            turno.append(x)

        while len(controle) != 25: #detecta empate, a partir da lista de controle      
            if (matrizMain[0][0] == "X" and matrizMain[0][1] == "X" and matrizMain[0][2] == "X" and matrizMain[0][3] == "X") or (matrizMain[1][0] == "X" and matrizMain[1][1] == "X" and matrizMain[1][2] == "X" and matrizMain[1][3] == "X") or (matrizMain[2][0] == "X" and matrizMain[2][1] == "X" and matrizMain[2][2] == "X" and matrizMain[2][3] == "X")or (matrizMain[3][0] == "X" and matrizMain[3][1] == "X" and matrizMain[3][2] == "X" and matrizMain[3][3] == "X")or (matrizMain[4][0] == "X" and matrizMain[4][1] == "X" and matrizMain[4][2] == "X" and matrizMain[4][3] == "X")or (matrizMain[0][1] == "X" and matrizMain[0][2] == "X" and matrizMain[0][3] == "X" and matrizMain[0][4] == "X")or (matrizMain[1][1] == "X" and matrizMain[1][2] == "X" and matrizMain[1][3] == "X" and matrizMain[1][4] == "X") or (matrizMain[2][1] == "X" and matrizMain[2][2] == "X" and matrizMain[2][3] == "X" and matrizMain[2][4] == "X") or (matrizMain[3][1] == "X" and matrizMain[3][2] == "X" and matrizMain[3][3] == "X" and matrizMain[3][4] == "X") or (matrizMain[4][1] == "X" and matrizMain[4][2] == "X" and matrizMain[4][3] == "X" and matrizMain[4][4] == "X")or (matrizMain[0][0] == "X" and matrizMain[1][1] == "X" and matrizMain[2][2] == "X" and matrizMain[3][3] == "X")or (matrizMain[1][1] == "X" and matrizMain[2][2] == "X" and matrizMain[3][3] == "X" and matrizMain[4][4] == "X") or (matrizMain[0][1] == "X" and matrizMain[1][2] == "X" and matrizMain[2][3] == "X" and matrizMain[3][4] == "X") or (matrizMain[1][0] == "X" and matrizMain[2][1] == "X" and matrizMain[3][2] == "X" and matrizMain[4][3] == "X")or (matrizMain[4][0] == "X" and matrizMain[3][1] == "X" and matrizMain[2][2] == "X" and matrizMain[1][3] == "X")or (matrizMain[3][1] == "X" and matrizMain[2][2] == "X" and matrizMain[1][3] == "X" and matrizMain[0][4] == "X") or (matrizMain[3][0] == "X" and matrizMain[2][1] == "X" and matrizMain[1][2] == "X" and matrizMain[0][3] == "X") or (matrizMain[4][1] == "X" and matrizMain[3][2] == "X" and matrizMain[2][3] == "X" and matrizMain[1][4] == "X") or (matrizMain[0][0] == "X" and matrizMain[1][0] == "X" and matrizMain[2][0] == "X" and matrizMain[3][0] == "X") or (matrizMain[0][1] == "X" and matrizMain[1][1] == "X" and matrizMain[2][1] == "X" and matrizMain[3][1] == "X") or (matrizMain[0][2] == "X" and matrizMain[1][2] == "X" and matrizMain[2][2] == "X" and matrizMain[3][2] == "X")or (matrizMain[0][3] == "X" and matrizMain[1][3] == "X" and matrizMain[2][3] == "X" and matrizMain[3][3] == "X")or (matrizMain[0][4] == "X" and matrizMain[1][4] == "X" and matrizMain[2][4] == "X" and matrizMain[3][4] == "X")or (matrizMain[1][0] == "X" and matrizMain[2][0] == "X" and matrizMain[3][0] == "X" and matrizMain[4][0] == "X")or (matrizMain[1][1] == "X" and matrizMain[2][1] == "X" and matrizMain[3][1] == "X" and matrizMain[4][1] == "X") or (matrizMain[1][2] == "X" and matrizMain[2][2] == "X" and matrizMain[3][2] == "X" and matrizMain[4][2] == "X") or (matrizMain[1][3] == "X" and matrizMain[2][3] == "X" and matrizMain[3][3] == "X" and matrizMain[4][3] == "X") or (matrizMain[1][4] == "X" and matrizMain[2][4] == "X" and matrizMain[3][4] == "X" and matrizMain[4][4] == "X"):
                #acima, todas as condições possíveis de vitória
                vit("x") 
                print("Jogador {0} venceu".format(playerX))
                controle.clear() #limpa a lista que detecta empates
                return False
            elif (matrizMain[0][0] == "O" and matrizMain[0][1] == "O" and matrizMain[0][2] == "O" and matrizMain[0][3] == "O") or (matrizMain[1][0] == "O" and matrizMain[1][1] == "O" and matrizMain[1][2] == "O" and matrizMain[1][3] == "O") or (matrizMain[2][0] == "O" and matrizMain[2][1] == "O" and matrizMain[2][2] == "O" and matrizMain[2][3] == "O")or (matrizMain[3][0] == "O" and matrizMain[3][1] == "O" and matrizMain[3][2] == "O" and matrizMain[3][3] == "O")or (matrizMain[4][0] == "O" and matrizMain[4][1] == "O" and matrizMain[4][2] == "O" and matrizMain[4][3] == "O")or (matrizMain[0][1] == "O" and matrizMain[0][2] == "O" and matrizMain[0][3] == "O" and matrizMain[0][4] == "O")or (matrizMain[1][1] == "O" and matrizMain[1][2] == "O" and matrizMain[1][3] == "O" and matrizMain[1][4] == "O") or (matrizMain[2][1] == "O" and matrizMain[2][2] == "O" and matrizMain[2][3] == "O" and matrizMain[2][4] == "O") or (matrizMain[3][1] == "O" and matrizMain[3][2] == "O" and matrizMain[3][3] == "O" and matrizMain[3][4] == "O") or (matrizMain[4][1] == "O" and matrizMain[4][2] == "O" and matrizMain[4][3] == "O" and matrizMain[4][4] == "O")or (matrizMain[0][0] == "O" and matrizMain[1][1] == "O" and matrizMain[2][2] == "O" and matrizMain[3][3] == "O")or (matrizMain[1][1] == "O" and matrizMain[2][2] == "O" and matrizMain[3][3] == "O" and matrizMain[4][4] == "O") or (matrizMain[0][1] == "O" and matrizMain[1][2] == "O" and matrizMain[2][3] == "O" and matrizMain[3][4] == "O") or (matrizMain[1][0] == "O" and matrizMain[2][1] == "O" and matrizMain[3][2] == "O" and matrizMain[4][3] == "O")or (matrizMain[4][0] == "O" and matrizMain[3][1] == "O" and matrizMain[2][2] == "O" and matrizMain[1][3] == "O")or (matrizMain[3][1] == "O" and matrizMain[2][2] == "O" and matrizMain[1][3] == "O" and matrizMain[0][4] == "O") or (matrizMain[3][0] == "O" and matrizMain[2][1] == "O" and matrizMain[1][2] == "O" and matrizMain[0][3] == "O") or (matrizMain[4][1] == "O" and matrizMain[3][2] == "O" and matrizMain[2][3] == "O" and matrizMain[1][4] == "O") or (matrizMain[0][0] == "O" and matrizMain[1][0] == "O" and matrizMain[2][0] == "O" and matrizMain[3][0] == "O") or (matrizMain[0][1] == "O" and matrizMain[1][1] == "O" and matrizMain[2][1] == "O" and matrizMain[3][1] == "O") or (matrizMain[0][2] == "O" and matrizMain[1][2] == "O" and matrizMain[2][2] == "O" and matrizMain[3][2] == "O")or (matrizMain[0][3] == "O" and matrizMain[1][3] == "O" and matrizMain[2][3] == "O" and matrizMain[3][3] == "O")or (matrizMain[0][4] == "O" and matrizMain[1][4] == "O" and matrizMain[2][4] == "O" and matrizMain[3][4] == "O")or (matrizMain[1][0] == "O" and matrizMain[2][0] == "O" and matrizMain[3][0] == "O" and matrizMain[4][0] == "O")or (matrizMain[1][1] == "O" and matrizMain[2][1] == "O" and matrizMain[3][1] == "O" and matrizMain[4][1] == "O") or (matrizMain[1][2] == "O" and matrizMain[2][2] == "O" and matrizMain[3][2] == "O" and matrizMain[4][2] == "O") or (matrizMain[1][3] == "O" and matrizMain[2][3] == "O" and matrizMain[3][3] == "O" and matrizMain[4][3] == "O") or (matrizMain[1][4] == "O" and matrizMain[2][4] == "O" and matrizMain[3][4] == "O" and matrizMain[4][4] == "O"):
                #=
                vit("o")
                print("Jogador {0} venceu".format(playerO))
                controle.clear() #=
                return False
            elif turno[-1] == 1: #aqui é onde a lista "turno" é utilizada. Para o último valor "1", turno X, para "2", turno 0
                jogada("x")
            elif turno [-1] == 2:
                jogada("o")
        else:
            print("Empate")
            controle.clear()
            return False
        
def jogada(a):
    if a == "x":
        g = 'x'
        h = "X"
        i = 2
    elif a == "o": #essas condiçoes fazem a função fazer as alterações, dependendo de quem é o turno
        g = 'o'
        h = "O"
        i = 1
    while True:
        print("Turno {0}".format(g))
        xx = int(input("Digite o x (linha): "))
        yy = int(input("Digite o y (coluna): "))
        if xx > 4 or xx < 0 or yy > 4 or yy < 0: #impede que números inválidos, fora da matriz, sejam inseridos
            print("Posição não existe. Tente outra")
            return True #permite que a função continue sendo executada normalmente
        elif matrizMain[xx][yy] == " ": #verifica se já não há algum símbolo na matriz
            matrizMain[xx][yy] = h #altera o valor na matriz
            controle.append("p") #adiciona à lista controle, que é limitada até 25, detectando algum empate
            turno.append(i) #deixa o valor 1 ou 2 no final da lista, chamando então a próxima função, inicando a jogada do outro jogador
            os.system("cls")
            matriz() #mostra a atual matriz
            return False
        elif matrizMain[xx][yy] != " ": #caso já haja valor inserido, uma nova posição é solicitada
            print("Posição já ocupada, tente outra")
            return True

def main(): #função principal, que fica sendo executada em loop até o terminal ser fechado, independentemente de qualquer opção escolhida
    os.system("cls")
    while True:
        print("")
        print("----------- MENU ----------")
        print("| 1 -- Criar novo jogador |")
        print("| 2 -- Exibir pontuações  |")
        print("| 3 -- Excluir Jogador    |")
        print("| 4 -- Iniciar jogo       |")
        print("| 5 -- Como jogar         |")
        print("---------------------------")
        print("")

        opcao = input("Escolha uma das opções acima: ")

        if opcao == "1":
            criaNovoPlayer()
        elif opcao == "2":
            pontos()
        elif opcao == "3":
            excluirPlayer()
        elif opcao == "4":
            jogoMain()
        elif opcao == "5":
            cj()

main()