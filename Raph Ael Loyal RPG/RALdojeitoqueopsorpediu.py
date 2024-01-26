jogo = True
rodada1 = True

ola = "\nOlá jogador, seja bem vindo ao Raph Ael Loyal RPG"
print(ola)

nick = input("Qual seu nick jogador? Como lhe conhecem nas Terras Áereas? -> ")

while (len(nick) > 16):
    nick = input("Por favor, use um Nickname/Apelido de até 16 caractéres.\n")

olaNew = "\nPois bem " +nick+". "
explicacaoProf = "Nessa versão para enviar pro Psor, pq ele pediu, vai ser simplificada."

manaFogo = 20
manaRaio = 30
manaCura = 15

danoATK = 20
danoFogo = 50
danoRaio = 80

potHP = 50
curaHP = 10
recuperaMP = 5

enemyATK1 = 30
enemyATK2 = 40


acao0 = "(0) - Ataque básico, causa "+ str(danoATK)+" de dano"
acao1 = "(1) - Tomar Poção, cura "+str(potHP)+"HP"
acao2 = "(2) - Magia de Fogo, gasta "+ str(manaFogo)+"MP, causa "+str(danoFogo)+" de dano"
acao3 = "(3) - Magia de Raio, gasta "+ str(manaRaio)+"MP, causa "+str(danoRaio)+" de dano"
acao4 = "(4) - Magia de Cura, gasta "+ str(manaCura)+"MP, recupera "+str(curaHP)+"HP"
acao5 = "(5) - Concentrar-se, para sua mana recuperar em +"+ str(recuperaMP)+"MP"



HP_inicial = 100
MP_inicial = 50
pocoes_inicial = 5

HP_atual = HP_inicial
MP_atual = MP_inicial
pocoes_atual = pocoes_inicial

def tomarDano():
    global HP_atual
    HP_atual -= enemyATK1
    
    #global jogo

    #if HP_atual <= 0:
    #    jogo = False

def tomarMaisDano():
    global HP_atual
    HP_atual -= enemyATK2
    
    #global jogo

    #if HP_atual <= 0:
    #    jogo = False
        

def potionHP():
    
    global HP_atual
    global pocoes_atual

    if pocoes_atual == 0:
        print(nick+" não tem mais poções.")
        return 0
    
    HP_atual += potHP
    pocoes_atual -= 1

    if HP_atual > 100:
        HP_atual = 100

    print(nick+" utilizou uma Poção de Health Points!")
    return 0


def magiaDeFogo():
    global MP_atual

    if (MP_atual < manaFogo):
        print(nick+" não tem mana para a habilidade Magia de Fogo!")
        return 0
    
    MP_atual -= manaFogo

    if MP_atual < 0:
        MP_atual = 0

    print(nick+" conjurou a Magia de Fogo causando 50 de dano!")
    return danoFogo #o dano que ela caiusa


def magiaDeRaoi(): # é proposital Raoi / Raio, Raoi é meu nick rs.
    global MP_atual

    if (MP_atual < manaRaio):
        print(nick+" não tem mana para a habilidade Magia de Raio!")
        return 0
    
    MP_atual -= manaRaio

    if MP_atual < 0:
        MP_atual = 0
        
    print(nick+" conjurou a Magia de Raio causando 80 de dano!")
    return danoRaio


def magiaDeCura():
    global MP_atual
    global HP_atual

    if (MP_atual < manaCura):
        print(nick+" não tem mana para a habilidade Magia de Cura!")
        return 0
    
    MP_atual -= manaCura
    HP_atual += curaHP

    if HP_atual > 100:
        HP_atual = 100

    if MP_atual < 0:
        MP_atual = 0

    print(nick+" conjurou a Magia de Cura curando-se em 10HP e gastando 15MP!")
    return 0 #pq não dá dano.

def printarAcoes():
    print(acao0);print(acao1);print(acao2);print(acao3);print(acao4);print(acao5);

def esperar():
    global MP_atual

    MP_atual += recuperaMP

    if MP_atual > 50:
        MP_atual = 50

    print(nick+" concentrou-se pela sua Mana, além do comum.")
    return 0

def atkbasico():
    print(nick+" atacou com bravura tirando 20 de HP de seu oponente!")
    return danoATK

def fazerAcao():

    action = input("Tome sua ação "+nick+". -> ")

    if (action == "d"): #Isso aqui é porque o professor pediu como ação tomar dano de um inimigo
        tomarDano() #Entretanto, essa função será usada pelo inimigo, enfim... O nome deveria ser então "darDano()", mas enfim KKKKK
        return 0

    while( (action != "0") and (action != "1") and (action != "2") and (action != "3") and (action != "4") and (action != "5" )):
        action = input("Por favor "+nick+", use 0, 1, 2, 3, 4 ou 5 para representar sua ação.\n")

    if (action == "0"):
        return atkbasico()
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


inimigo1_HP = 200 # aqui era 100, mas como eu coloquei um inimigo só, será 200, talquei? :D


inimigo = "Mendonça"
bemvindoProPsor = "\nBem vindo "+nick+" ao seu único oponente, o nome dele é "+inimigo+", tente derrotá-lo! Suas ações:"

def acaoInimigo(): #vai ser diferente.  

    actionEnemy = input("Faça a ação do inimigo:(ATAQUE1) ou (ATAQUE2) -> ").lower()

    while ( (actionEnemy != "ataque1" and actionEnemy != "ataque2")):
        actionEnemy = input("Apenas aceito: 'ataque1' ou 'ataque2' -> ").lower()
        
    if actionEnemy == "ataque1":
        tomarDano()
        print(nick+" tomou 30 de dano pelo Ataque(1) 'Investida' de "+inimigo+"!")
        return
    else:
        tomarMaisDano()
        print(nick+" tomou 40 de dano pelo Ataque(2) 'Mordida' de "+inimigo+"!")
        return



while jogo:

    print(olaNew + explicacaoProf)
    print(bemvindoProPsor)
    printarAcoes()

    while(rodada1):

        #inimigo = "Flygo" n usei.

        turno = 1


        while(inimigo1_HP > 0):
            
            print("\nTurno "+str(turno)+ " - SUA VEZ");turno += 1 #YUUUGIIIOOOHHH
            inimigo1_HP -= fazerAcao()
            
            print("O seu inimigo está com " +str(inimigo1_HP)+"HP.")
            
            if(inimigo1_HP <= 0):
                rodada1 = False
                print(inimigo+" foi derrotado! Parabéns "+nick+", você mandou bem!")
                break

            informacoesPlayer()

            print("\nTurno "+str(turno)+ " - VEZ INIMIGO");turno += 1
            acaoInimigo()

            if(HP_atual <= 0):
                rodada1 = False
                print(nick,"foi derrotado! Mais sorte na próxima vez!")
                break

            
            print("O seu inimigo está com " +str(inimigo1_HP)+"HP.")
            informacoesPlayer()
            
            
            MP_atual += 5
            if (MP_atual > 50):
                MP_atual = 50

    #print("Parabéns jogador, você venceu! :D")
    jogo = False
            
            
    
    
