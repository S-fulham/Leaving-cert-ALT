import random
import time

WIDTH = 20
HEIGHT = 20 
forest = for i in range (HEIGHT ="T")
neighbours = [(-1,1), (1,0), (1,1),
              (-1,0), (0,0), (0,1),
              (-1,-1), (0-1), (1,-1)]

moistureLevel = 0.3
realFire = 1 - (moistureLevel)

forest[0][0] = "F"

def printForest(forest):
    for row in forest:
        print(" ".join(row))
    print()

printForest()
#while True:
    

#def getNeighbours(x,y):
