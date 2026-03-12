##  ADD A PAST FOREST THAT U COMPARE AGAINTS THE CURRENT ONE TO SEE IF ANYTHING CHANGES IF NOTHING CHANGES BREAK THE MODEL

# imports all the libaryies I need
import random
import time
import copy
import serial

ser = serial.Serial("COM14", 115200)
time.sleep(3)
line = ser.readline().decode().strip()
parts = line.split(",")
Flame = 0
Temperature = 0 
soilMoisture = 0
airHumidity = 0

def getValues (Flame, Temperature, soilMoisture, airHumidity):
    Flame.append(int(parts[1].strip()))
    Temperature.append(int(parts[2].strip()))
    soilMoisture.append(int(parts[3].strip()))
    airHumidity.append(int(parts[3].strip()))
    return Flame, Temperature, soilMoisture, airHumidity

#creats the 2D grid
WIDTH = 20
HEIGHT = 20
forest = [["T" for i in range (HEIGHT)] for i in range(WIDTH)]
#variables

moistureLevel = soilMoisture
tempurture = 31
#realFire = 1 - (moistureLevel)

# IF TEMP IS ABOVE 30 DEGREES CELSIUS WHICH IUS THE DANGER ZONE FOR FIRES THE MOSTURE LEVEL IS REDUCED (I WANT TO MAKE THIS CHANGE THE FIRE CHANCE NOT THE MOISUTE LEVEL BECAUSE THE MOISTURE LEVEL ISNT ACTUALLY CHANGING THE CHANCE OF FORE IS JUST INCREASING)
#
#if tempurture > 30:
 #   moistureLevel *= 0.9

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
forest [HEIGHT//2][WIDTH//2] = "F"

while True:
    newForest = copy.deepcopy(forest)
    for x in range (HEIGHT):
        for y in range (WIDTH):
            #sets burning trees to burnt
            if forest[x][y] == "F":
                newForest[x][y] = "."
            #if the tree isnt on fire the neighbouring trees are checked to see if they are burning, if they are the their is a chance for this one to catch on fire 
            elif forest [x][y] == "T":
                neighbours = getNeighbours(x,y)
                #calculates the fire chance
                if any (forest[x][y] == "F" for x,y  in neighbours):
                    fireChance=random.randint(0,1)
                    if fireChance > moistureLevel:
                        newForest[x][y] = "F" 
    if not any("F" in row for row in forest):
        break
    #prints the updated forest and sets the new forest to the original one
    printForest(forest)
    forest=newForest
    print (moistureLevel)
    #wait one second before printing again
    time.sleep(1)