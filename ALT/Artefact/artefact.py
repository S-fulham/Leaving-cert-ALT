import serial
from datetime import datetime
import time


ser = serial.Serial("COM14", 115200)
time.sleep(3)


with open("log.csv", "w") as file:
    file.write("Flame, Temperature, soilMoisture\n")
while True:
    line = ser.readline().decode().strip()
    timestamp = datetime.now().strftime("%H:%M:%S")


    print("Logging", timestamp, line)


    with open("log.csv", "a") as file:
        file.write(f"{timestamp},{line}\n")