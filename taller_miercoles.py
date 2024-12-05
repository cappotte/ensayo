import ramdom
numero_secreto = ramdom.randint(1,100)
intentos = 0
adivinado = False
intento = int(intento)
intentos += 1

if intento < numero_secreto:
    print("El numero es mayor")
elif intento > numero_secreto:
    print("El numero es menor")
while not adivinado:
    intento = input("Adivina el numero entre 1 y 100(o escribe 'salir' para rendirte):")
    if intento.lower() =='salir':
        print("Te has rendido. El numero secreto era:" , numero_secreto)
        break
else:
    adivinado = True
    print("FELICITACIONES, Adivinastes el numero en {intentos} intentos.")
        