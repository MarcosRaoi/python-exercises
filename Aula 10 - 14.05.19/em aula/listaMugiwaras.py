mugiwara = ["Monkey D. Luffy","Roronoa Zoro","Nami","Usopp","Vinsmoke Sanji"]
print(mugiwara[0])
print(mugiwara[3])
print("Essas são a posição [0] e posição [3] da Lista Mugiwara")

print("\nLista Mugiwaras:")
print(mugiwara)

print("\nDando Append [ .append() ] no Tony Tony Chopper. Isso coloca ele na última posição:")
mugiwara.append("Tony Tony Chopper")
print(mugiwara)

print("\nDando .append() na Miss All Sundays, tá do nosso lado ou não? hmm")
mugiwara.append("Ms. All Sundays")
print(mugiwara)

print("\nTá, ela saiu do barco, não sabemos, vamos dar .pop(), que removerá a última posição:")
mugiwara.pop()
print(mugiwara)

print("\nVamos dar .insert() na [6] e na [7] o momento que a Nefertari Vivi e o Carue viram Nakamas!")
mugiwara.insert(6,"Nefertari Vivi")
mugiwara.insert(7,"Carue")
print(mugiwara)

print("\nVamos dar .remove() no 'Carue', ele foi entregar a carta em Alubarna.")
mugiwara.remove("Carue") # tira o Carue, ele foi entregar a carta em Alubarna.
print(mugiwara)

print("\nVamos dar pop na [6], na Nefertari Vivi, cabou Alabasta, salvamos, Marinha veio nos pegar, tivemos que sair correndo, mas mostramos nossa marca e criamos um laço que durará para sempre! Avante Alabasta!")
mugiwara.pop(6) # interessante, o pop se você colocar um número, ele seleciona a posição
print(mugiwara)

quantidade_Usopp = mugiwara.count("Usopp")
print("\nA quantidade de Usopp's na lista Mugiwara são:",quantidade_Usopp,"- Obviamente, afinal ele é único!")

posicao_Usopp = mugiwara.index("Usopp")
print("A posição do Usopp nos Piratas do Chapéu-de-Palha é:",posicao_Usopp,"- Entretanto ele é o mais foda!")
