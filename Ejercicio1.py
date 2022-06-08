# Mamani Alcon Andres Fabian
# 6948279
import pandas as pd
import numpy as np

bias = np.array([0.0])

def sigmoid(x):
  return (1/(1+np.exp(-x)))

def prediccion(entradas, pesos, bias_vector):
  capa1 = np.dot(entradas, pesos) + bias
  print('capa1: ', capa1)
  capa2 = sigmoid(capa1)
  return capa2

iris = pd.read_csv('iris.csv')
# lista con los datos de petal.length
lis1 = list(map(float, iris['petal.length'])) 
entradas = np.array(lis1)

#pesos, con un valor entre
pesos = np.random.normal(0, 0.05, (len(entradas)))
#pesos = np.random.uniform(-1.0, 1.0, len(entradas))
#print('pesos', pesos)
y_esp = prediccion(entradas, pesos, bias)
print('capa2: ', y_esp)


