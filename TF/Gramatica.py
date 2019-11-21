import nltk
from nltk import CFG
from nltk.parse.generate import generate
from random import randint
import numpy as np

patron1=""
patron2=""
identity=""
inputTest=[]
def inputTestFill(idselected):
    f=open("data-"+ str(idselected), "r")

    fl =f.readlines()
    inputTest=[]
    for x in fl:
        inputTest.append(x)

def activefunction(x):
    return 1 if(x>0) else -1

def startdebths(*argv):
    global patron1,patron2,identity
    patron1=np.array([argv[0]])
    patron2=np.array([argv[1]])
    identity=np.identity(4,dtype=int)


def weightmatrix():
    W1=np.subtract(np.dot(patron1.transpose(),patron1),identity)
    W2=np.subtract(np.dot(patron2.transpose(),patron2),identity)
    matriz_sum=np.add(W1,W2)
    return matriz_sum

        
def similar(prueba):
    testMatrix=np.array([prueba])
    output=np.dot(testMatrix,weightmatrix())
    result=map(activefunction,output.tolist()[0])
    return list(result)

def main():
    startdebths(inputTest)
    pruebas=inputTest
    results=[]
    for prueba in pruebas:
        results.append(similar(prueba))
    print(*results)


Usuario = CFG.fromstring("""

F -> SU P
F -> I
F -> P
SU -> 'yo'
P -> VTC CO
P -> VT OD
P -> VI
P -> VTC E
P -> VT E
I -> 'hola' | 'adios'
E -> 'bien' | 'mal'
VTC -> 'como' | 'evito'
VT -> 'hago' | 'duermo'
CO -> 'grasas' | 'frutas' | 'saludable' | 'dañino'
OD -> 'deporte' | 'ejercicio'
VI -> 'fumo' | 'bebo' | 'camino'
""")

Robot = CFG.fromstring("""

F -> SU P
F -> P
SU -> 'tu'
P -> VTC CO
P -> VT OD
P -> VI
P -> VTC E
P -> VT E
E -> 'bien' | 'mal'
VTC -> 'comes' | 'evitas'
VT -> 'haces' | 'duermes'
CO -> 'grasas' | 'frutas' | 'saludable' | 'dañino'
OD -> 'deporte' | 'ejercicio'
VI -> 'fumas' | 'bebes' | 'caminas'
""")

def ChatBot(frase):
    try:
        palabras = frase.decode("utf-8").split()
        print(palabras)
        Usuario.check_coverage(palabras)

        respuesta=''
        if('hola' in palabras):
            respuesta += 'hola, '
        elif('adios' in palabras):
            return 'adios!'
        randomnumber=randint(1,20)
        for i, sentence in enumerate(generate(Robot, n=20)):
            if(i == randomnumber):
                respuesta += ' ¿ '+' '.join(sentence) + ' ?'
        
        return respuesta
    


    except:
        return 'No entiendo'

#if __name__ == "__main__":
#    main()
