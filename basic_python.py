#basic python
print("Hola mundo")

variable = input("Como te llamas? ")

print("Hola "+variable+"!")

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
    print("las operaciones disponibles son: suma, multiplicacion.")
