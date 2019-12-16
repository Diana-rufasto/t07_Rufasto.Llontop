#Ejercicio01
s=0
n=50
for n in range (103):
    if((n+2)==0):
        n+=2
    #fin_if
#fin_for
print("serie:",n)


#Ejercicio02
s=0
for i in range (60):
    if((i % 2 )==0):
        s=s+i
    #fin_if
#fin_for
print("Suma:",s)


#Ejercicio03
i=0
for i in range(80):
    if((i%2)==0):
        i+=2
        print(i)
    #fin_if
#fin_for
print("Termina programa")


#Ejercicio04
n=0
for n in range(30):
    if((n<=30)):
        n+=1
        print(n)
    #fin_if
#fin_for


#Ejercicio05
n=0
for n in range(100):
    if((n%10)==0):
        n+=10
        print(n)
    #fin_if
#fin_for
print("numeros de 10 en 10")
