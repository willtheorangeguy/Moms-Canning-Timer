"""
Mom's Canning Timer - Customizable 15-minute stove top timers.
Copyright (C) 2017-2026 willtheorangeguy
"""

# pylint: skip-file

import time


def timeStart():
    """Main Time Function"""
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
