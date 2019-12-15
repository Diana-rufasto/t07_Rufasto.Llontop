#Ejercicio01
#Pedir edad de ingreso a la escuela PNP
edad=10
edad_invalida=(edad<16 or edad >25)
while(edad_invalida):
    edad=int(input("ingrese edad:"))
    edad_invalida=(edad<16 or edad >25)
#fin_while
print("edad valida:",edad)



