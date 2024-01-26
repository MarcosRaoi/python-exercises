game = True
inventario = []
printarsoumavez = 0

a17 = i1 = armadura1 = "Green Mail"
a2 = i2 = armadura2 = "Blue Mail"
a40 = i3 = armadura3 = "Red Mail" # ou malhas, tanto faz rs.
#nao tá na lista do PDF, mas né... vamo por. E tá no enunciado.

a12 = i4 = espada1 = "Fighter's Sword"
a29 = i5 = espada2 = "Master Sword"
a38 = i6 = espada3 = "Tempered Sword"
a16 = i7 = espada4 = "Golden Sword"

a11 = i8 = escudo1 = "Fighter's Shield"
a35 = i9 = escudo2 = "Red Shield"
a30 = i10 = escudo3 = "Mirror Shield"

a33 = i11 = luva1 = "Power Glove"
a39 = i12 = luva2 = "Titan's Mitt"

a5 = i13 = bumerangue1 = "Boomerang"
a28 = i14 = bumerangue2 = "Magical Boomerang"

a32 = i15 = bota1 = "Pegasus Boots"

a3 = i16 = medalhao1 = "Bombos Medallion"
a10 = i17 = medalhao2 = "Ether Medallion"
a34 = i18 = medalhao3 = "Quake Medallion"

a8 = i19 = cajado1 = "Cane of Byrna"
a9 = i20 = cajado2 = "Cane of Somaria"
a13 = i21 = cajado3 = "Fire Rod"
a20 = i22 = cajado4 = "Ice Rod"

a22 = i23 = magico1 = "Magic Bottles"
a23 = i24 = magico2 = "Magic Cape"
a24 = i25 = magico3 = "Magic Mirror"
a25 = i26 = magico4 = "Magic Mushroom"
a26 = i27 = magico5 = "Magic Potion"
a27 = i28 = magico6 = "Magic Powder"

#nadar1 = "Flippers"

a1 = i29 = utilidade1 = "Basket"
a4 = i30 = utilidade2 = "Book of Mudora"
a6 = i31 = utilidade3 = "Bow and Arrow"
a7 = i32 = utilidade4 = "Bug Catching Net"
a15 = i33 = utilidade5 = "Flute"
a18 = i34 = utilidade6 = "Hammer"
a19 = i35 = utilidade7 = "Hookshot"
a21 = i36 = utilidade8 = "Lamp"
a36 = i37 = utilidade9 = "Shovel"
a37 = i38 = utilidade10 = "Super Bomb"

#nadar1 = "Zora's Flippers"
#coelhorosa = "Moon Pearl"

a14 = i39 = outro1 = "Flippers"
a31 = i40 = outro2 = "Moon Pearl"

todos_itens = [a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26,a27,a28,a29,a30,a31,a32,a33,a34,a35,a36,a37,a38,a39,a40]

#print(todos_itens)

acao1 = "Ação 1 - Bater com a espada (Caso tenha uma espada)"
acao2 = "Ação 2 - Defender com o escudo (caso tenha escudo)"
acao3 = "Ação 3 - Levantar uma pedra (Caso tenha uma das luvas)"
acao4 = "Ação 4 - Correr (Caso tenha as botas)"
acao5 = "Ação 5 - Pegar itens"
acao6 = "Ação 6 - Usar itens"

acoes = acao1+"\n"+acao2+"\n"+acao3+"\n"+acao4+"\n"+acao5+"\n"+acao6+"\n"

navi = "Hey, look listen!\n"
saudacoes = "Olá... Eu irei lhe fazer algumas perguntas antes de começarmos..."

####
breveexplicacoes = "Bom, algumas breves explicações..."
####
tutorial1 = ", gostaria de lhe informar que você tem uma série de ações para tomar, e uma série de perguntas que você pode fazer. São 6 ações ao todo, e uma quantidade imensa de perguntas. Para tomar a ação, digite apenas o número da mesma em questão. Para usar itens, por exemplo, digite apenas o número 6. Se quiser ouvir a explicação da Ação 6, entretanto, escreva acao6 (Mais detalhes da ação, você encontra em 'acao6mais'). Isso funciona para as outras também! :D Sempre que quiser ler este tutorial novamente, digite 'tutorial'! ^-^ - Ah, outra dica também é que 'comandos' mostra todos os comandos que você tem disponível! :)"
podemoscomecar = "Hey, Podemos Começar? Vamos lá...\n"

acaoqual = "\nQual sua ação "

acaonaoentendi = "Não entendi a ação rs... Tente 'comandos' para lhe ajudar. Ou tente escrever apenas um número (1 a 6)! :D"
####

pokequestion = "Você é 'menino' ou 'menina'(Ou 'outro'...)?\n"
meninoburro = "Eu não entendi o que você quis dizer, ou seja, tu é burro que nem um menino. Vai ficar Aventureiro então."
nicknamemax16 = "Sinto muito, nicknames podem ter até no máximo 16 caracteres.\n"
nickpref = "Você tem alguma maneira que prefere que lhe chamem"
quertut = "Você deseja receber o tutorial "
semtut = "Tá bom, sem tutorial pra você... Quando precisar, digite: 'tutorial'"

sintomuito = "Sinto muito, não tem como pegar >>"
sem = "<< sem ter >>"
substituiu = "<< substituiu >>"
comoachou = "Como você achou >>"
estranho = "<<? Estranho isso aí... Pegue primeiro >>"

#####

acao5mais = "Hello, quer pegar Itens? Digite o nome exato do item, ou escolha através do código alfabético dele (a1 até a40) ou número de série dele (i1 até i40) - Ah, tem outra coisa, você pode tentar pelo o que ele representa. Por exemplo, quer a primeira espada? Tente 'espada1'. "

acao6mais = "Listen, quer usar seus Itens? Para isso você precisa tê-los no Inventário. A função Usar está disponíveis para alguns itens, e para outros não. Os itens que já tem funções específicas na ação 1, na ação 2, na ação 3 e na ação 4, você não conseguirá usá-los por aqui. Alguns outros itens específicos também não podem. :)"
acao1mais = "Listen, bater com uma espada necessita TER uma espada! Isso significa que você precisa pegar a espada1, a espada2, a espada3 ou a espada4! :D São elas: "+espada1+", "+espada2+", "+espada3+" e "+espada4+". Boa sorte! :)"
acao2mais = "Listen, defenda-se dos inimigos! :O Pra isso, precisas de um Escudo... Temos disponíveis o escudo1, escudo2 ou escudo3, tente pegá-los... São eles: "+escudo1+", "+escudo2+" e "+escudo3+". Watch out! ^^'"
acao3mais = "Listen, você precisa de uma luva1 ou uma luva2 para conseguir carregar uma pedrona daquelas! São elas: "+luva1+" e "+luva2+"... Hey! Tente pegá-las para levantar uma pedra e arremessá-la! Ela pode estar atrasando seu caminho! :D"
acao4mais = "Listen, para correr, bem bem rápdio, uma arrancadona e tanto... Você precisará fazer isso com segurança e aderência, pra isso precisará de uma bota! :D Tente a: "+bota1+". Terá mais sucesso com ela no inventário! :D"

#####

itemqual = "Qual item deseja pegar "
itemsucesso = "Item pego com sucesso! -> "
itemnaoentendi = "Não entendi o item, poderia repetir "

itemjatem = "Você já tem esse item no inventário "

#####

usarfechar = "(OBS: Para fechar o inventário, basta 'fechar')"
usarqual = "Qual item deseja usar "
usarnaotem = "Você não tem esse item no inventário, tente outro!\n"

inventariovazio = "Seu inventário está vazio "
inventariofechado = "Seu inventário foi fechado com sucesso! :)"

usararmadura = "Hey! Isso é uma Armadura! Você já está usando-a..."
usarespada = "Watch out! :O Isso é uma Espada, tome cuidado... Use sua ação 1 para maior precisão!"
usarescudo = "Watch out! O_O Isso é um Escudo! Para se defender com mais vigor, use a ação 2!"
usarluva = "Listen! Se você quer arremessar pedras, aconselho que use a ação 3!"
usarbota = "Listen! Se quer dar uma arrancada, aconselho que Corra com a ação 4! ;)"
usaroutro1 = "Look, entendo que queira nadar com as Zora's Flippers, entretanto não temos nenhum local de mergulho por aqui, sinto muito... ''/"
usaroutro2 = "Look, acho louvável que não queira virar um Coelhinho Rosa, mas estamos bem longe do Dark World, não se preocupe! =^-^="

### confesso que aqui perdi a criatividade / tempo / saco, sinto muito x_x ###

usarbumerangue1 = "Você acaba de usar seu "+bumerangue1+"!Foi longe e voltou! rere!"
usarbumerangue2 = "Você acaba de usar seu "+bumerangue2+"!Foi muuuuuito longe e voltou! ririri"

usarmedalhao1 = "Você acaba de usar "+medalhao1+"!"
usarmedalhao2 = "Você acaba de usar "+medalhao2+"!"
usarmedalhao3 = "Você acaba de usar "+medalhao3+"!"

usarcajado1 = "Você acaba de usar "+cajado1+"!"
usarcajado2 = "Você acaba de usar "+cajado2+"!"
usarcajado3 = "Você acaba de usar "+cajado3+"!"
usarcajado4 = "Você acaba de usar "+cajado4+"!"

usarmagico1 = "Você acaba de usar "+magico1+"!"
usarmagico2 = "Você acaba de usar "+magico2+"!"
usarmagico3 = "Você acaba de usar "+magico3+"!"
usarmagico4 = "Você acaba de usar "+magico4+"!"
usarmagico5 = "Você acaba de usar "+magico5+"!"
usarmagico6 = "Você acaba de usar "+magico6+"!"

usarutilidade1 = "Você acaba de usar "+utilidade1+"!"
usarutilidade2 = "Você acaba de usar "+utilidade2+"!"
usarutilidade3 = "Você acaba de usar "+utilidade3+"!"
usarutilidade4 = "Você acaba de usar "+utilidade4+"!"
usarutilidade5 = "Você acaba de usar "+utilidade5+"!"
usarutilidade6 = "Você acaba de usar "+utilidade6+"!"
usarutilidade7 = "Você acaba de usar "+utilidade7+"!"
usarutilidade8 = "Você acaba de usar "+utilidade8+"!"
usarutilidade9 = "Você acaba de usar "+utilidade9+"!"
usarutilidade10 = "Você acaba de usar "+utilidade10+"!"

#####

#acao1
espadada = "Você deu uma bela de uma espadada em, "
semespada = "Você não tem nenhuma Espada em seu inventário "

#acao2
defesa = "Watch out! :O Fazia tempo que não via uma bela defesa dessas "
semescudo = "Você não tem nenhum Escudo em seu inventário "

#acao3
levantada = "Wow, você é muito forte! Levantou a pedra "
semluva = "Você não tem nenhuma Luva em seu inventário "

#acao4
corrida = "Caramba O-O, que arrancada foi essa!? Você é muito "
sembota = "Você não tem nenhuma Bota em seu inventário "



#######
#"tutorial, comandos, acoes, inventario, itens"#

comandos = "Comandos:" 
c_comandos = "\n'comandos' - Mostra os comandos."
c_tutorial = "\n'tutorial' - Mostra o tutorial."
c_inventario = "\n'inventario' - Mostra os itens que você tem no inventário."
c_acoes = "\n'acoes' - Mostra as ações disponíveis padrão."
c_itens = "\n'itens' - Mostra todos os itens disponíveis que podem ser pegos."

c_acao1 = "\n'acao1' - Mostra a Ação 1!"
c_acao2 = "\n'acao2' - Mostra a Ação 2!"
c_acao3 = "\n'acao3' - Mostra a Ação 3!"
c_acao4 = "\n'acao4' - Mostra a Ação 4!"
c_acao5 = "\n'acao5' - Mostra a Ação 5!"
c_acao6 = "\n'acao6' - Mostra a Ação 6!"

c_acao1mais = "\n'acao1mais' - Mostra mais explicações a respeito da Ação 1..."
c_acao2mais = "\n'acao2mais' - Mostra mais explicações a respeito da Ação 2..."
c_acao3mais = "\n'acao3mais' - Mostra mais explicações a respeito da Ação 3..."
c_acao4mais = "\n'acao4mais' - Mostra mais explicações a respeito da Ação 4..."
c_acao5mais = "\n'acao5mais' - Mostra mais explicações a respeito da Ação 5..."
c_acao6mais = "\n'acao6mais' - Mostra mais explicações a respeito da Ação 6..."


comandos += c_comandos + c_tutorial + c_inventario + c_acoes + c_itens

comandos += c_acao1 + c_acao2 + c_acao3 + c_acao4 + c_acao5 + c_acao6
comandos += c_acao1mais + c_acao2mais + c_acao3mais + c_acao4mais + c_acao5mais + c_acao6mais

# depois vc faz essa parte, completa etc... pro psor, n precisa, vai tomar muito tempo.
######################

print(navi+saudacoes)

gender = input(pokequestion).lower()

if (gender == "menina"):
    Lonk = "Zolda"
    aventureirx = "Aventureira"
    carx = "cara"
    ousadx = "ousada"
    gananciosx = "gananciosa"
    astutx = "astuta"
    poderosx = "minha poderosa"
    fracx = "fraca"
    defensivx = "defensiva"
    indefesx = "indefesa"
    sozinhx = "sozinha"
    perrapadx = "perrapada"
    rapidx = "rápida"
    franzinx = "franzina"
    esquecidinhx = "esquecidinha"
    curiosx = "curiosa"

elif (gender == "outro"):
    Lonk = "Navi"
    aventureirx = "Aventureirx"
    carx = "carx"
    ousadx = "ousadx"
    gananciosx = "gananciosx"
    astutx = "astutx"
    poderosx = "livre poderosx"
    fracx = "fracote"
    defensivx = "defensivx"
    indefesx = "indefesx"
    sozinhx = "sozinhx"
    perrapadx = "perrapadx"
    rapidx = "rápidx"
    franzinx = "franzinx"
    esquecidinhx = "esquecidinhx"
    curiosx = "curiosx"

else:
    Lonk = "Lonk"
    aventureirx = "Aventureiro"
    carx = "caro"
    ousadx = "ousado"
    gananciosx = "ganancioso"
    astutx = "astuto"
    poderosx = "meu poderoso"
    fracx = "fraco"
    defensivx = "defensivo"
    indefesx = "indefeso"
    sozinhx = "sozinho"
    perrapadx = "perrapado"
    rapidx = "rápido"
    franzinx = "franzino"
    esquecidinhx = "esquecidinho"
    curiosx = "curioso"
    
    if (gender != "menino"):
        print(meninoburro)

#caro é a saudação comum... tem outros adjetivos que uso durante o programa. Vou por cada um para uma ação. 

nick = input(nickpref+" "+carx+" "+aventureirx+" "+Lonk+"?\n")
while (len(nick) > 16):
    nick = input(nicknamemax16)

#depois de pegar o nick etc, completa o tutorial.
nomeinteiro = carx+" "+aventureirx+" "+nick
tutorial = "Listen "+nomeinteiro + tutorial1

print(breveexplicacoes)

desejatutorial = input(quertut+curiosx+" "+aventureirx+" "+nick+"? (S/N)\n").lower()

if desejatutorial == "s" or desejatutorial == "sim" or desejatutorial == "claro" or desejatutorial == "yes" or desejatutorial == "claro meu bom senhor":
    print(tutorial)
else:
    print(semtut)
    
print(podemoscomecar)
print(acoes)

#######################################################################################################
#######################################################################################################

while(game):
    acao = input(acaoqual+nomeinteiro+"?\n")

    if acao == "tutorial": 
        print(tutorial)

    elif acao == "comandos" or acao == "help" or acao == "ajuda" or acao == "socorro": #socorro KKKKKKK
        print(comandos)

    elif acao == "acoes":
        print(acoes)

    elif acao == "inventario" or acao == "meus itens" or acao == "meu inventario":
        print(inventario)

    elif acao == "itens" or acao == "todos itens" or acao == "item" or acao == "todos os itens" or acao == "lista de itens":
        print(todos_itens)

    elif acao == "acao1":
        print(acao1)

    elif acao == "acao2":
        print(acao2)

    elif acao == "acao3":
        print(acao3)

    elif acao == "acao4":
        print(acao4)

    elif acao == "acao5":
        print(acao5)

    elif acao == "acao6":
        print(acao6)

    elif acao == "acao5mais":
        print(acao5mais)

    elif acao == "acao6mais":
        print (acao6mais)

    elif acao == "acao1mais":
        print (acao1mais)

    elif acao == "acao2mais":
        print (acao2mais)

    elif acao == "acao3mais":
        print (acao3mais)

    elif acao == "acao4mais":
        print (acao4mais)
    
    
    elif acao == "5" or acao == "pegar" or acao == "pegar itens" or acao == "Pegar itens" or acao == "pega" or acao == "Pega" or acao == "Pega item" or acao == "Pega itens": ## adicionadas pegar e pegar itens pra ficar mais opções mais legaizin.
    ##aqui poderia colocar uns if no começo de que se a acao =="pegar", acao recebe 5, mas sei lá... desne.

        item = input(itemqual+gananciosx+" "+aventureirx+" "+nick+"?\n")
                
        if (item == i1 or item == "i1" or item == "a17" or item == "armadura1"):
            item = i1
    
        elif (item == i2 or item == "i2" or item == "a2" or item == "armadura2"):
            if (i1 not in inventario):
                print(sintomuito+i2+sem+i1)
                continue
            item = i2
            inventario.remove(i1)
            print(i2,substituiu,i1)            

        elif (item == i3 or item == "i3" or item == "a40" or item == "armadura3"):
            if (i2 not in inventario):
                print(sintomuito+i3+sem+i2)
                continue
            item = i3
            inventario.remove(i2)
            print(i3,substituiu,i2)            
   
        elif (item == i4 or item == "i4" or item == "a12" or item == "espada1"):
            item = i4

        elif (item == i5 or item == "i5" or item == "a29" or item == "espada2"):
            if (i4 not in inventario):
                print(comoachou+i5+sem+i4+estranho+i4+"...")
                continue
            item = i5
            print(i5,substituiu,i4)
            inventario.remove(i4)
                  
        elif (item == i6 or item == "i6" or item == "a38" or item == "espada3"):
            if (i5 not in inventario):
                print(sintomuito+i6+sem+i5)
                continue
            item = i6
            inventario.remove(i5)
            print(i6,substituiu,i5)
            
        elif (item == i7 or item == "i7" or item == "a16" or item == "espada4"):
            if (i6 not in inventario):
                print(sintomuito+i7+sem+i6)
                continue
            item = i7
            inventario.remove(i6)
            print(i7,substituiu,i6)
            
        elif (item == i8 or item == "i8" or item == "a11" or item == "escudo1"):
            item = i8
            
        elif (item == i9 or item == "i9" or item == "a35" or item == "escudo2"):
            if (i8 not in inventario):
                print(sintomuito+i9+sem+i8)
                continue
            item = i9
            inventario.remove(i8)
            print(i9+substituiu+i8)
            
        elif (item == i10 or item == "i10" or item == "a30" or item == "escudo3"):
            if (i9 not in inventario):
                print(sintomuito+i10+sem+i9)
                continue
            item = i10
            inventario.remove(i9)
            print(i10+substituiu+i9)
 
        elif (item == i11 or item == "i11" or item == "a33" or item == "luva1"):
            item = i11
            
        elif (item == i12 or item == "i12" or item == "a39" or item == "luva2"):
            if (i11 not in inventario):
                print(comoachou+i12+sem+i11+estranho+i11+"...")
                continue
            item = i12
            inventario.remove(i11)
            print(i12+substituiu+i11)
            
        elif (item == i13 or item == "i13" or item == "a5" or item == "bumerangue1"):
            item = i13
            
        elif (item == i14 or item == "i14" or item == "a28" or item == "bumerangue2"):
            if (i13 not in inventario):
                print(sintomuito+i14+sem+i13)
                continue
            item = i13
            inventario.remove(i13)
            print(i14+substituiu+i13)
            
        elif (item == i15 or item == "i15" or item == "a32" or item == "bota" or item == "bota1"):
            item = i15
        elif (item == i16 or item == "i16" or item == "a3" or item == "medalhao1"):
            item = i16
        elif (item == i17 or item == "i17" or item == "a10" or item == "medalhao2"):
            item = i17
        elif (item == i18 or item == "i18" or item == "a34" or item == "medalhao3"):
            item = i18
        elif (item == i19 or item == "i19" or item == "a8" or item == "cajado1"):
            item = i19
        elif (item == i20 or item == "i20" or item == "a9" or item == "cajado2"):
            item = i20
        elif (item == i21 or item == "i21" or item == "a13" or item == "cajado3"):
            item = i21
        elif (item == i22 or item == "i22" or item == "a20" or item == "cajado4"):
            item = i22
        elif (item == i23 or item == "i23" or item == "a22" or item == "magico1"):
            item = i23
        elif (item == i24 or item == "i24" or item == "a23" or item == "magico2"):
            item = i24
        elif (item == i25 or item == "i25" or item == "a24" or item == "magico3"):
            item = i25
        elif (item == i26 or item == "i26" or item == "a25" or item == "magico4"):
            item = i26
        elif (item == i27 or item == "i27" or item == "a26" or item == "magico5"):
            item = i27
        elif (item == i28 or item == "i28" or item == "a27" or item == "magico6"):
            item = i28
        elif (item == i29 or item == "i29" or item == "a1" or item == "utilidade1"):
            item = i29
        elif (item == i30 or item == "i30" or item == "a4" or item == "utilidade2"):
            item = i30
        elif (item == i31 or item == "i31" or item == "a6" or item == "utilidade3"):
            item = i31
        elif (item == i32 or item == "i32" or item == "a7" or item == "utilidade4"):
            item = i32
        elif (item == i33 or item == "i33" or item == "a15" or item == "utilidade5"):
            item = i33
        elif (item == i34 or item == "i34" or item == "a18" or item == "utilidade6"):
            item = i34
        elif (item == i35 or item == "i35" or item == "a19" or item == "utilidade7"):
            item = i35
        elif (item == i36 or item == "i36" or item == "a21" or item == "utilidade8"):
            item = i36
        elif (item == i37 or item == "i37" or item == "a36" or item == "utilidade9"):
            item = i37
        elif (item == i38 or item == "i38" or item == "a37" or item == "utilidade10"):
            item = i38
        elif (item == i39 or item == "i39" or item == "a14" or item == "outro1"):
            item = i39
        elif (item == i40 or item == "i40" or item == "a31" or item == "outro2"):
            item = i40
     
        else:
            item = input(itemnaoentendi+gananciosx+" "+aventureirx+" "+nick+"? ^^'\n")

            ##inventario.append(item) # se não pegar o item pelo código, e o nome do item estiver na lista de todos os itens, coloca ele no inventário do Lonk.
            ##print(itemsucesso+item) #sou meio burro né... ali em cima podia ser, exemplo: item == "i40" or item == "a31" or item == i40 ... Já que tem o nome X_x
            #se bem que sei lá, menos coisa pra eu escrever... ^^"

        ## aqui, pelo código, ele tá conseguindo pegar dois itens iguais, dois bumerangues por exemplo, i13 ##

        ####, tá, vamo ver se ele faz agora....

        if item in inventario:
            print(itemjatem+esquecidinhx+" "+aventureirx+" "+nick+"...rs")
            #inventario.remove(item)

        else:
            inventario.append(item)
            print(itemsucesso+item)

    elif acao == "6" or acao == "usar" or acao == "usar item" or acao == "usar itens" or acao == "Usar" or acao == "Usar itens" or acao == "usa" or acao == "Usa" or acao == "Usa item" or acao == "usa item": # preciso checar se ele tem o item né lul...

        if printarsoumavez == 0: ## FAMOSA POG. PROGRAMAÇÃO ORIENTADA A GAMBIARRAS. ## VLW FLW.
            print(usarfechar)
            printarsoumavez += 1
        
        if (inventario == []):
            print(inventariovazio+nomeinteiro)
            continue
        
        usar = input(usarqual+astutx+" "+aventureirx+" "+nick+"?\n")

        if usar == "fechar":
            print(inventariofechado)
            continue
        
        while (usar not in inventario):
            usar = input(usarnaotem)
            if usar == "fechar":
                print(inventariofechado)
                break

        if (usar == armadura1 or usar == armadura2 or usar == armadura3):
            print(usararmadura)

        elif (usar == espada1 or usar == espada2 or usar == espada3 or usar == espada4):
            print(usarespada)

        elif (usar == escudo1 or usar == escudo2 or usar == escudo3):
            print(usarescudo)

        elif (usar == luva1 or usar == luva2):
            print(usarluva)

        elif usar == bota1:
            print(usarbota)

        elif usar == outro1:
            print(usaroutro1)

        elif usar == outro2:
            print(usaroutro2)
            
        #####################################################################################################################################################
        ############################## TÁ, ACABAMOS OS QUE NÃO PODEM SER USADOS, BORA PROS UTILIZÁVEIS..... #################################################
        ############ VOU USAR VARIÁVEIS, PORQUE PRETENDO MUDAR OS ITENS E TUDO MAIS DEPOIS, FICAR MAIS CUSTOMIZÁVEL, MAS POR ENQUANTO VOU PEGANDO ###########
        # AS INFOS DO THE LEGEND OF ZELDA - A LINK TO THE PAST ... NAO LEMBRO MUUITO DO GAME, SÓ JOGUEI EMULADOR, ENTÃO NÉ, VOU PEGANDO AJUDA DA WIKI #######
        # FONTES: https://zelda.gamepedia.com/Magic_Powder  -------- EXEMPLO ETC. ###########################################################################
        #####################################################################################################################################################

        elif ("Boomerang" in usar):
            if (bumerangue1 in inventario):
                print(usarbumerangue1)
            else:
                print(usarbumerangue2)

        elif ("Medallion" in usar):
            if (usar == medalhao3):
                print(usarmedalhao3)
            elif (usar == medalhao2):
                print(usarmedalhao2)
            else:
                print('O único medalhão "inútil"... '+usarmedalhao1)

        elif ("Cane of" in usar):
            if (usar == cajado1):
                print(usarcajado1)
            else:
                print(usarcajado2)

        elif ("Rod" in usar):
            if (usar == cajado3):
                print(usarcajado3)
            else:
                print(usarcajado4)

        elif ("Magic" in usar):
            if (usar == magico1):
                print(usarmagico1)
            elif (usar == magico2):
                print(usarmagico2)
            elif (usar == magico3):
                print(usarmagico3)
            elif (usar == magico4):
                print(usarmagico4)
            elif (usar == magico5):
                print(usarmagico5)
            else:
                print(usarmagico6)

        #### os com nome diferente, os utilidades basicamente... "utilidades" etc. ####

        else:
            if (usar == utilidade1):
                print(usarutilidade1)
            elif (usar == utilidade2):
                print(usarutilidade2)
            elif (usar == utilidade3):
                print(usarutilidade3)
            elif (usar == utilidade4):
                print(usarutilidade4)
            elif (usar == utilidade5):
                print(usarutilidade5)
            elif (usar == utilidade6):
                print(usarutilidade6)
            elif (usar == utilidade7):
                print(usarutilidade7)
            elif (usar == utilidade8):
                print(usarutilidade8)
            elif (usar == utilidade9):
                print(usarutilidade9)
            else:
                if (usar == "fechar"):
                    continue
                print(usarutilidade10)

        ######## sorrry......... cabou a criatividade, rsrsrs .

    elif acao == "1" or acao == "usar espada" or acao == "espada" or acao == "bater" or acao == "atacar" or acao == "Bater" or acao == "Bater com a espada":
        if ((espada1 in inventario) or (espada2 in inventario) or (espada3 in inventario) or (espada4 in inventario)):
            print(espadada+poderosx+" "+aventureirx+" "+nick)
        else:
            print(semespada+fracx+" "+aventureirx+" "+nick)

    elif acao == "2" or acao == "usar escudo" or acao == "escudo" or acao == "defender" or acao == "Defender" or acao == "Defender com o escudo":
        if ((escudo1 in inventario) or (escudo2 in inventario) or (escudo3 in inventario)):
            print(defesa+defensivx+" "+aventureirx+" "+nick+"....")
        else:
            print(semescudo+indefesx+" "+aventureirx+" "+nick)

    elif acao == "3" or acao == "usar luva" or acao == "luva" or acao == "por a luva" or acao == "por luva" or acao == "levantar" or acao == "Levantar" or acao == "Levantar uma pedra":
        if ((luva1 in inventario) or (luva2 in inventario)):
            print(levantada+sozinhx+" "+aventureirx+" "+nick+"!:O")

        else:
            print(semluva+franzinx+" "+aventureirx+" "+nick)

    elif acao == "4" or acao == "usar bota" or acao == "bota" or acao == "calçar bota" or acao == "calcar bota" or acao == "por a bota" or acao == "por bota" or acao == "correr":
        if (bota1 in inventario):
            print(corrida+rapidx+" "+aventureirx+" "+nick+"!!!! O----------O")
        else:
            print(sembota+perrapadx+" "+aventureirx+" "+nick)

    elif acao == "sair" or acao == "Sair" or acao == "false" or acao == "False" or acao == "/quit" or acao == "@quit" or acao == "falou" or acao == "flw":
        print("Falou o/")
        game = False

    ## lul, essa é pica /\

    else:
        print(acaonaoentendi)
            
            
            
            
        
            

        
            
        
        

        

        

        
        
        
            
        
        
                
