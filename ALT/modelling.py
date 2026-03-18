# imports all the libairy I need
import random
import time
import copy
import serial


#creats the 2D grid
WIDTH = 20
HEIGHT = 20
forest = [["🌲" for i in range (HEIGHT)] for i in range(WIDTH)]
#variables
ser = serial.Serial("COM14", 115200)
time.sleep(3)
Flame = 0
Temperature = 0 
soilMoisture = 0
airHumidity = 0
moistureLevel = 0

# gets values from the sensors they're returned in list so I have to strip them to get the values to run the model
def getValues():
    line = ser.readline().decode().strip()
    parts = line.split(",")
    soilMoisture = int(parts[0])
    Temperature = int(parts[1])
    airHumidity = int(parts[3])
    return  Temperature, airHumidity, soilMoisture


#prints the forest
def printForest(forest):
    for row in forest:
        print(" ".join(row))
    print()

#this function gets the neighbouring trees
def getNeighbours(x,y):
    directions = [(-1,1), (1,0), (1,1),
                (-1,0),          (0,1),
                (-1,-1), (0,-1), (1,-1)]
    neighbours = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        #makes sure the trees arent out of bounds
        if 0 <= nx and nx < HEIGHT and 0 <= ny and ny < WIDTH:
            neighbours.append((nx, ny))
    return neighbours


#makes the center of the 2D list tree on fire 
forest [HEIGHT//2][WIDTH//2] = "🔥"

while True:
    Temperature, soilMoisture, airHumidity = getValues()
    newForest = copy.deepcopy(forest)
    for x in range (HEIGHT):
        for y in range (WIDTH):
            #sets burning trees to burnt
            if forest[x][y] == "🔥":
                newForest[x][y] = "."
            #if the tree isnt on fire the neighbouring trees are checked to see if they are burning, if they are the their is a chance for this one to catch on fire 
            elif forest [x][y] == "🌲":
                neighbours = getNeighbours(x,y)
                #calculates the fire chance
                if any (forest[x][y] == "🔥" for x,y  in neighbours):
                    fireChance=random.random()
                    realFire = 0
                    realFire += (Temperature / 40) * 0.4 
                    realFire += (1 - airHumidity / 100) * 0.3  
                    realFire += (1 - soilMoisture / 100) * 0.3  
                    realFire = max(0, min(realFire, 1))   
                    if fireChance < realFire:
                        newForest[x][y] = "🔥" 
    if not any("🔥" in row for row in forest):
        printForest(forest)
        break
    #prints the updated forest and sets the new forest to the original one
    printForest(forest)
    forest=newForest
    print ("This is the moisture level ", moistureLevel)
    print ("This is the temperature ",Temperature)
    print ("This is the air humidity level ",airHumidity)
    print ("This is the the chance of a fire starting level ",realFire)

    #wait one second before printing again
    time.sleep(1)