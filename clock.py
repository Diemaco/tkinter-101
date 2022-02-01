import random
import tkinter as tk
from datetime import datetime


def randomColor():
    return random.choice(["white", "black", "red", "green", "blue", "cyan", "yellow", "magenta"])


def updateStr():
    timeStr.set(datetime.now().strftime("%H:%M:%S"))
    root.after(1000, updateStr)


root = tk.Tk()
root.title('Clock')
root.configure(bg=randomColor())

timeStr = tk.StringVar(value='')

text = tk.Label(root, bg=randomColor(), fg=randomColor())
text.configure(textvariable=timeStr)
text.pack()

updateStr()

root.mainloop()
