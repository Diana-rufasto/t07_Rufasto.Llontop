edad=22
edad_invalida=(edad<25 or edad>100)
while(edad_invalida):
    edad=int(input("ingrese edad:"))
    edad_invalida=(edad<25 or edad >100)
#fin_while
print("edad valida:",edad)



#Ejercicio02
hemoglobina=10
hemoglobina_invalida=(hemoglobina<13 or hemoglobina>16)
while(hemoglobina_invalida):
    hemoglobina=float(input("ingrese hemoglobina:"))
    hemoglobina_invalida=(hemoglobina<13 or hemoglobina>16)
#fin_while
print("hemoglobina valida:",hemoglobina)



#Ejercicio03
talla=1.53
talla_invalida=(talla<1.55 or talla>1.65)
while(talla_invalida):
    talla=float(input("ingrese talla:"))
    talla_invalida=(talla<1.55 or talla>1.65)
#fin_while
print("talla valida:",talla)


#Ejercicio04
peso=50.5
peso_invalida=(peso<52 or peso>75)
while(peso_invalida):
    peso=float(input("ingrese peso:"))
    peso_invalida=(peso<52 or peso>75)
#fin_while
print("peso valida:",peso)



#Ejercicio05
#monto total para saber si gana una vale
monto_total=350.0
monto_total_invalida=(monto_total<400 or monto_total>500)
while(monto_total_invalida):
    monto_total=float(input("ingrese monto total:"))
    monto_total_invalida=(monto_total<400 or monto_total>500)
#fin_while
print("monto total valida:",monto_total)
