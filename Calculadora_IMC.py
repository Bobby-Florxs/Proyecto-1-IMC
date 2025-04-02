"""Entrada de datos"""

print("Buen día soy una calculadora de IMC, favor de completar los siguientes datos")

while True: 
    nombre= input("Cual es tu nombre? ")
    if nombre.isalpha() and len(nombre) > 0: 
        break
    else:
        print("No puedes dejar el campo vacío o escribir numeros")

while True: 
    apellido_paterno= input("Cual es tu apellido paterno? ")
    if apellido_paterno.isalpha() and len(apellido_paterno) > 0: 
        break
    else:
        print("No puedes dejar el campo vacío o escribir numeros")

while True: 
    apellido_materno= input("Cual es tu apellido materno? ")
    if apellido_materno.isalpha() and len(apellido_materno) > 0: 
        break
    else:
        print("No puedes dejar el campo vacío o escribir numeros")

while True: 
    try: 
        edad= int(input("cual es tu edad? "))
        if len(str(edad)) > 0:
         break
    except ValueError as e:
        print("No puedes dejar el campo vacío o escribir letras")
        
while True: 
    try: 
        peso= float(input("cual es tu peso en kilogramos? "))
        if len(str(peso)) > 0 and peso > 0:
         break
        else:
            print("No puedes poner 0 ya que es un valor indivisible")
    except ValueError as e:
        print("No puedes dejar el campo vacío o escribir letras")

while True: 
    try: 
        estatura= float(input("cual es tu estatura en metros? "))
        if len(str(estatura)) > 0 and estatura > 0:
         break
        else:
            print("No puedes poner 0 ya que es un valor indivisible")
    except ValueError as e:
        print("No puedes dejar el campo vacío o escribir letras")

"""Calculo de IMC"""
imc = peso / (estatura**2)

print(f"Tu indice de masa corporal es de {imc}")
print(f"Gracias por tu visita {nombre} {apellido_paterno} {apellido_materno}")