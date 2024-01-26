# Vamo lá, exercício do jogo RPG. ^-^' Vamos se dedicar, mais do que você já
# se dedica, afinal agora é um exercício com temática de jogo! :D Vamos dar
# nosso 100%, assim como você fez no Aleatorium, exercício 20! :D P. Web p Jogos

# tá, voltei, talvez não tanto quanto o 20, mas ok. bora

from random import randint

##################

jogo = True
rodada1 = True
rodada2 = False
rodada3 = False
rodada4 = False
rodada5 = False


ola = "\nOlá jogador, seja bem vindo ao Raph Ael Loyal RPG"

print(ola)
nick = input("Qual seu nick jogador? Como lhe conhecem nas Terras Áereas? -> ")

while (len(nick) > 16):
    nick = input("Por favor, use um Nickname/Apelido de até 16 caractéres.\n")

olaNew = "\nPois bem " +nick+". "
explicacao1 = "Você enfrentará, nessa primeira versão do RAL RPG, 5 oponentes, cada um com duas habilidades diferentes:"
explicacaoOponentes = "\nPoderes dos Raphers(seus inimigos): Lhe causar Dano, ou uma habilidade secreta que você será surpreendido ao enfrentá-lo."
aviso = "\nFique atento a sua vida, e escolha as melhores acoes neste RPG de turno alucinante. Derrote-os e seja o Rei de toda Ael!"
tutorial = "É interessante lhe advertir que suas poções são limitadas (começa com 5) e sua Mana recupera 5 pontos a cada turno. Seu máximo de HP é 100. Os Raphers causam 30 de Dano."

acao1 = "(1)-Tomar Poção, cura 50HP"
acao2 = "(2)-Magia de Fogo, gasta 10MP, causa 50 de dano"
acao3 = "(3)-Magia de Raio, gasta 20MP, causa 80 de dano"
acao4 = "(4)-Magia de Cura, gasta 15MP, recupera 10HP"
acao5 = "(5)-Esperar sua mana recuperar em 5MP"


HP_inicial = 100
MP_inicial = 50
pocoes_inicial = 5

HP_atual = HP_inicial
MP_atual = MP_inicial
pocoes_atual = pocoes_inicial

def tomarDano():
    global HP_atual
    HP_atual -= 30
    
    global jogo

    if HP_atual <= 0:
        jogo = False
        

def potionHP():
    
    global HP_atual
    global pocoes_atual

    if pocoes_atual == 0:
        print(nick+" não tem mais poções.")
        return 0
    
    HP_atual += 50
    pocoes_atual -= 1

    if HP_atual > 100:
        HP_atual = 100

    return 0


def magiaDeFogo():
    global MP_atual

    if (MP_atual < 10):
        print(nick+" não tem mana para a habilidade Magia de Fogo!")
        return 0
    
    MP_atual -= 10

    if MP_atual < 0:
        MP_atual = 0

    print(nick+" conjurou a Magia de Fogo!")
    return 50 #o dano que ela caiusa


def magiaDeRaoi(): # é proposital Raoi / Raio, Raoi é meu nick rs.
    global MP_atual

    if (MP_atual < 20):
        print(nick+" não tem mana para a habilidade Magia de Raio!")
        return 0
    
    MP_atual -= 20

    if MP_atual < 0:
        MP_atual = 0
        
    print(nick+" conjurou a Magia de Raio!")
    return 80


def magiaDeCura():
    global MP_atual
    global HP_atual

    if (MP_atual < 15):
        print(nick+" não tem mana para a habilidade Magia de Cura!")
        return 0
    
    MP_atual -= 15
    HP_atual += 10

    if HP_atual > 100:
        HP_atual = 100

    if MP_atual < 0:
        MP_atual = 0

    print(nick+" conjurou a Magia de Cura!")
    return 0

def printarAcoes():
    print(acao1);print(acao2);print(acao3);print(acao4);print(acao5);

def esperar():
    global MP_atual

    MP_atual += 5

    if MP_atual > 50:
        MP_atual = 50

    print(nick+" apenas esperou pela sua Mana.")
    return 0


def fazerAcao():

    action = input("\nTome sua ação "+nick+".\n")

    if (action == "d"): #Isso aqui é porque o professor pediu como ação tomar dano de um inimigo
        tomarDano() #Entretanto, essa função será usada pelo inimigo, enfim... O nome deveria ser então "darDano()", mas enfim KKKKK
        return

    while( (action != "1") and (action != "2") and (action != "3") and (action != "4") and (action != "5" )):
        action = input("Por favor "+nick+", use 1, 2, 3, 4 ou 5 para representar sua ação.\n")

    if (action == "1"):
        return potionHP()
    elif (action == "2"):
        return magiaDeFogo()
    elif (action == "3"):
        return magiaDeRaoi()
    elif (action == "4"):
        return magiaDeCura()
    else:
        return esperar()

def informacoesPlayer():
    global HP_atual
    global MP_atual
    global pocoes_atual
    
    print("Sua vida atual é: "+ str(HP_atual)+"HP")
    print("Sua mana atual é: "+ str(MP_atual)+"MP")
    print("Você tem "+str(pocoes_atual)+" poções.")


inimigo1_HP = 100
inimigo2_HP = 125
inimigo3_HP = 150
inimigo4_HP = 175
inimigo5_HP = 200

inimigo = "0"

def acaoInimigo():

    global inimigo
    actionEnemy = randint(0,1)    

    if inimigo == "Flygo": #tinha colocado "1", mas com o nome é mais legal xD
        if actionEnemy == 0:
            tomarDano()
            print(nick+" tomou 30 de dano!")
            return
        else:
            global inimigo1_HP
            inimigo1_HP += 20
            print("Flygo se curou em 20HP!")
            return
            
            
    elif inimigo == "Altari": #KKKKKKKK EU TO COPIANDO OS NOMES DE POKÉMONS "AÉREOS", FLYGON, ALTARIA KKKKSRSRSR.
        if actionEnemy == 0:
            tomarDano()
            print(nick+" tomou 30 de dano!")
            return
        else:
            global inimigo2_HP
            inimigo2_HP += 20
            print("Altari se curou em 25HP!")
            return

    elif inimigo == "3":
        return

    elif inimigo == "4":
        return

    else:
        return
        

#while (rodada1):

bemvindo1 = "\nBem vindo "+nick+" ao seu primeiro oponente, o nome dele é Flygo, tente derrotá-lo e prosseguir com sua jornada! Suas ações:"

while jogo:

    print(olaNew + explicacao1 + explicacaoOponentes +aviso)

    respostaTut = input("Deseja receber o tutorial, "+nick+"? (S)im / (N)ão. -> ").lower()

    while (respostaTut != "n" and respostaTut != "s"):
        respostaTut = input("Responda s ou n -> ")

    if (respostaTut == "s"):
        print(tutorial)


    print(bemvindo1)
    printarAcoes()
    
    while(rodada1):

        inimigo = "Flygo"

        if(inimigo1_HP == 0):
            rodada1 = False
            print("Flygo foi derrotado!")
            rodada2 = True
            break
            

        while(inimigo1_HP > 0):
            inimigo1_HP -= fazerAcao()
            acaoInimigo()
            MP_atual += 5
            if (MP_atual > 50):
                MP_atual = 50
            informacoesPlayer()
            if (inimigo1_HP <=0):
                inimigo1_HP = 0
            print("O seu inimigo está com " +str(inimigo1_HP)+"HP.")

    bemvindo2 = "\nSeu segundo oponente, "+nick+", é o corajoso Altari, tome cuidado!"
    
    print(bemvindo2)
    printarAcoes()
    
    while(rodada2):

        inimigo = "Altari"

        if(inimigo2_HP == 0):
            rodada2 = False
            print("Altari foi derrotado!")
            rodada3 = True
            break
            

        while(inimigo2_HP > 0):
            inimigo2_HP -= fazerAcao()
            acaoInimigo()
            MP_atual += 5
            if (MP_atual > 50):
                MP_atual = 50
            informacoesPlayer()
            if (inimigo2_HP <=0):
                inimigo2_HP = 0
            print("O seu inimigo está com " +str(inimigo2_HP)+"HP.")

        
    jogo = False

    
