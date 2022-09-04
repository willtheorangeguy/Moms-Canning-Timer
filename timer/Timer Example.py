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
