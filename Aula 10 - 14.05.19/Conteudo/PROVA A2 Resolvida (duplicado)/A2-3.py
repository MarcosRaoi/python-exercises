money = 100

item = input("Qual item você quer comprar? ")

if item == "Faquinha":
    preco = 50
elif item == "Espada":
    preco = 75
elif item == "Espada de ouro":
    preco = 500
elif item == "Escudo":
    preco = 50
elif item == "Poção de cura":
    preco = 25
elif item == "Armadura completa":
    preco = 150
elif item == "Magia que com certeza vai fazê-lo ganhar de todo mundo":
    preco = 1000000
else:
    preco = 0


if preco == 0:
    print("Item não existe na loja")
else:
    if preco > money:
        print("Não pode comprar")
    else:
        print("Pode comprar")
