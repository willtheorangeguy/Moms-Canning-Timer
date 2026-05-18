"""
Mom's Canning Timer - Customizable 15-minute stove top timers.
Copyright (C) 2017-2026 willtheorangeguy
"""

# pylint: disable=invalid-name, global-variable-undefined, redefined-outer-name

# Import Statements
import time
from tkinter import Tk, Label, Button, TOP


def timeStart1():
    """Main Time Function 1"""
    # Variables to keep track and display
    global Sec
    global Min
    Sec = 0
    Min = 0
    # Begin Process
    while Min < 15:
        Sec += 1
        print(str(Min) + " Min " + str(Sec) + " Secs ")
        time.sleep(1)
        if Sec == 59:
            Sec = 0
            Min += 1
            print(str(Min) + " Minutes ")
            if Min == 15:
                break


# Timer Program for Burner 2
def timeStart2():
    """Main Time Function 2"""
    # Variables to keep track and display
    Sec = 0
    Min = 0
    # Begin Process
    while Min < 15:
        Sec += 1
        print(str(Min) + " Min " + str(Sec) + " Secs ")
        time.sleep(1)
        if Sec == 59:
            Sec = 0
            Min += 1
            print(str(Min) + " Minutes ")
            if Min == 15:
                break


# Timer Program for Burner 3
def timeStart3():
    """Main Time Function 3"""
    # Variables to keep track and display
    Sec = 0
    Min = 0
    # Begin Process
    while Min < 15:
        Sec += 1
        print(str(Min) + " Min " + str(Sec) + " Secs ")
        time.sleep(1)
        if Sec == 59:
            Sec = 0
            Min += 1
            print(str(Min) + " Minutes ")
            if Min == 15:
                break


# Timer Program for Burner 4
def timeStart4():
    """Main Time Function 4"""
    # Variables to keep track and display
    Sec = 0
    Min = 0
    # Begin Process
    while Min < 15:
        Sec += 1
        print(str(Min) + " Min " + str(Sec) + " Secs ")
        time.sleep(1)
        if Sec == 59:
            Sec = 0
            Min += 1
            print(str(Min) + " Minutes ")
            if Min == 15:
                break


def timer():
    """Main Window"""
    # Create Window
    window = Tk()
    window.title("Canning Timer")

    # Burner 1
    timer1title = Label(window, text="#1")
    timer1start = Button(window, text="Start timer!", command=timeStart1)

    # Burner 2
    timer2title = Label(window, text="#2")
    timer2start = Button(window, text="Start timer!", command=timeStart2)

    # Burner 3
    timer3title = Label(window, text="#3")
    timer3start = Button(window, text="Start timer!", command=timeStart3)

    # Burner 4
    timer4title = Label(window, text="#4")
    timer4start = Button(window, text="Start timer!", command=timeStart4)

    # Pack Statements
    timer1title.pack(side=TOP)
    timer1start.pack(side=TOP)

    timer2title.pack(side=TOP)
    timer2start.pack(side=TOP)

    timer3title.pack(side=TOP)
    timer3start.pack(side=TOP)

    timer4title.pack(side=TOP)
    timer4start.pack(side=TOP)

    # Sustain Window
    window.mainloop()


if __name__ == "__main__":
    timer()
