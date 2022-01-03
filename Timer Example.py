# Copyright 2017-2022 Dog Face Development Co.
import time

# Main Time Function
def timeStart():
    # Variables to keep track and display
    Sec = 0
    Min = 0
    # Begin Process
    timeLoop = start
    while timeLoop:
        Sec += 1
        print(str(Min) + " Min " + str(Sec) + " Secs ")
        time.sleep(1)
        if Sec == 59:
            Sec = 0
            Min += 1
            print(str(Min) + " Minutes ")
            if Min == 15:
                break

# Ask to Begin
start = input("Would you like to begin Timing? (y/n): ")
if start == "y":
    timeStart()
