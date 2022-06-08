import random
import numpy 
from deap import algorithms
from deap import base
from deap import creator
from deap import tools
import pandas as pd

N_nodos = 5
data= pd.read_csv("recorrido.csv", sep=",", header=None)
array=numpy.asarray(data)
recorrido = data.iloc[:, :].values
"""
recorrido  = [[0, 7, 8, 9, 20], 
            [7, 0, 10, 4, 11],
            [9, 10, 0, 11, 5],
            [8, 4, 11, 0, 17],
            [20, 11, 5, 17, 0]]
#print(recorrido)
"""
nodos=["a","b","c","d","e"]
def comienzo(nodos,comienzo):
    longitud=len(nodos)
    indice=-1
    for i in range(longitud):
        if(nodos[i]==comienzo):
            return i
def mostrar_camino(ordenado):
    longitud=len(ordenado)
    sum=0
    for i in range(longitud):
        print(nodos[ordenado[i]],'-> ',end="")
    print(nodos[ordenado[0]])

def mostrar_costos(individual):
    longitud=len(individual)
    sum=0
    for i in range(longitud-1):
        print(recorrido[individual[i]][individual[i+1]],'   ',end="")
    print(recorrido[individual[i+1]][individual[0]])

def mostrarnodos(vec):
    for i in vec:
        print(i,' ',end="")
    print()
def evalua_posicion(individual):
    longitud=len(individual)
    sum=0
    for i in range(longitud-1):
        sum=sum+recorrido[individual[i]][individual[i+1]]
    sum=sum+recorrido[individual[i+1]][individual[0]]
    return sum,

def principio(individual,a):
    longitud=len(individual)
    indice=0
    for i in range(longitud):
        if(individual[i]==a):
            indice=i
    ordenado=individual[indice:]+individual[:indice]
    return ordenado

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("permutation", random.sample, range(N_nodos), N_nodos)

toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.permutation)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", evalua_posicion)
toolbox.register("mate", tools.cxPartialyMatched)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=2.0/N_nodos)
toolbox.register("select", tools.selTournament, tournsize=3)

def main(seed=0):
    random.seed(seed)
    pop = toolbox.population(n=300)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("Avg", numpy.mean)
    stats.register("Std", numpy.std)
    stats.register("Min", numpy.min)
    stats.register("Max", numpy.max)

    algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=100, stats=stats,
                        halloffame=hof, verbose=False)
    print()
    print('Lista de nodos :')
    mostrarnodos(nodos)
    #print('Recorridos :')
    #print(recorrido)
    print('cual es el nodo de inicio?')
    nodo=str(input()).lower()
     
    while nodo==-1:
        print('El nodo no existe, ingres de nuevo')
        nodo=input()
    
    inicio = comienzo(nodos, nodo)
    vector = principio(pop[0], inicio)
    
    print('Mejor recorrido: ')
    print('Camino: ')
    mostrar_camino(vector)
    print('Costos: ')
    mostrar_costos(vector)
    print('Suma total :', evalua_posicion(pop[0])[0])
    
    return pop, stats, hof
if __name__ == "__main__":
    pop, stats, hof=main()
