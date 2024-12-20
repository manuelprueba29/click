
#comprehesion en python
listanum=list(range(100))
#print (listanum)


#filtar numero pares en un rango por lista 
pares=[elemento for elemento in listanum if elemento%2==0]
#print(pares)

 #crear  un diccionario por zip
idEstudiante=[1,2,3]
estudiante=['juan','juddn','juag']

estudianteconcodigo={uid:estudiante for uid, estudiante in zip(idEstudiante, estudiante)}

print(estudianteconcodigo)

#
import random
random_numeros=[]
for i in range(10):
    random_numeros.append(random.randint(1,3))

#print(random_numeros)
#conjunto set en pyton es utilizado con {}
no_repetir={numeros for numeros in random_numeros}
#print(no_repetir)
