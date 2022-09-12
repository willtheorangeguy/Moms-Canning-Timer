"""
Mom's Canning Timer - Customizable 15-minute stove top timers. 
Copyright (C) 2017-2022 Dog Face Development Co.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

# Import statements
from tkinter import *
import tkinter.messagebox as msgbox
import time

# Timer Program for Burner 1 
def timeStart1():
    # Variables to keep track and display
    global Sec
    global Min
    Sec = 0
    Min = 0
    # Begin Process
    while Min <15:
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
    # Variables to keep track and display
    Sec = 0
    Min = 0
    # Begin Process
    while Min <15:
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
    # Variables to keep track and display
    Sec = 0
    Min = 0
    # Begin Process
    while Min <15:
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
    # Variables to keep track and display
    Sec = 0
    Min = 0
    # Begin Process
    while Min <15:
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
    # Create Window
    window = Tk()
    window.title("Canning Timer")

    # Burner 1
    timer1title = Label(window, text = "#1")
    timer1start = Button(window, text = "Start timer!", command = timeStart1)

    # Burner 2
    timer2title = Label(window, text = "#2")
    timer2start = Button(window, text = "Start timer!", command = timeStart2)

    # Burner 3
    timer3title = Label(window, text = "#3")
    timer3start = Button(window, text = "Start timer!", command = timeStart3)

    # Burner 4
    timer4title = Label(window, text = "#4")
    timer4start = Button(window, text = "Start timer!", command = timeStart4)

    # Pack Statements
    timer1title.pack(side = TOP)
    timer1start.pack(side = TOP)

    timer2title.pack(side = TOP)
    timer2start.pack(side = TOP)

    timer3title.pack(side = TOP)
    timer3start.pack(side = TOP)

    timer4title.pack(side = TOP)
    timer4start.pack(side = TOP)

    # Sustain Window
    window.mainloop()

if __name__ == '__main__':
    timer()
    