import random
import time
import copy

WIDTH = 20
HEIGHT = 20
forest = [["T" for i in range (HEIGHT)] for i in range(WIDTH)]
moistureLevel = 0.3
realFire = 1 - (moistureLevel)
def printForest(forest):
    for row in forest:
        print(" ".join(row))
    print()

def getNeighbours(x,y):
    directions = [(-1,1), (1,0), (1,1),
              (-1,0),        (0,1),
              (-1,-1), (0,-1), (1,-1)]
    neighbours = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx and nx < HEIGHT and 0 <= ny and ny < WIDTH:
            neighbours.append((nx, ny))
    return neighbours


forest [HEIGHT//2][WIDTH//2] = "F"
newForest = copy.deepcopy(forest)
for i in range (20):
    for x in range (HEIGHT):
        for y in range (WIDTH):
            if forest[x][y] == "F":
                newForest[x][y] = "."
            elif forest [x][y] == "T":
                neighbours = getNeighbours(x,y)
                if any (forest[x][y] == "F" for x,y  in neighbours):
                    fireChance=random.randint(0,1)
                    if fireChance > moistureLevel:
                        newForest[x][y] = "F" 


    printForest(forest)
    forest=newForest
    time.sleep(1)
