"""
Mom's Canning Timer - Customizable 15-minute stove top timers.
Copyright (C) 2017-2026 willtheorangeguy
"""

# pylint: skip-file

import tkinter as tk

counter = 0


def counter_label(label):
    """Main Time Function"""

    def count():
        """Counting Seconds"""
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000, count)

    count()


root = tk.Tk()
root.title("Counting Seconds")
label = tk.Label(root, fg="green")
label.pack()
counter_label(label)
button = tk.Button(root, text="Stop", width=25, command=root.destroy)
button.pack()
root.mainloop()
