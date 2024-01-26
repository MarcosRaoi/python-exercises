infantaria = int(input("Quantos soldados vão entrar em veículos? "))

contador = 1
motoristas = 0
passageiros = 0

while contador <= infantaria:
    if contador % 4 == 0:
        motoristas = motoristas + 1
    else:
        passageiros = passageiros + 1

    contador = contador + 1

if infantaria % 4 != 0: #Para equivaler o último carro, que só teria passageiros
    motoristas = motoristas + 1
    passageiros = passageiros - 1

print("Serão ", motoristas, " motoristas e ", passageiros, " passageiros")
