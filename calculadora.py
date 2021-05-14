#calculadora.py


print(" ")
print("Ahora prueva esta calculadora")

operacion = input("Que operacion quieres hacer? ")
primernumero = input("primer numero: ")
segundonumero = input("segundo numero: ")

if operacion == "suma":
    suma = int(primernumero)+int(segundonumero)
    print(str(primernumero)+" + "+str(segundonumero)+" = "+str(suma))
elif operacion == "multiplicacion":
    multiplicacion = int(primernumero)*int(segundonumero)
    print(str(primernumero)+" x "+str(segundonumero)+" = "+str(multiplicacion))
else:
    print("Lo sentimos, ha habido un error.")
    print("Las operaciones disponibles son: suma, multiplicacion.")
    print(" ")
