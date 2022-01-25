import random
import tkinter as tk

root = tk.Tk()
root.title('My First Window')

s = 50


def tick():
    global s

    s += 50

    if s > 50 * 7:
        root.destroy()
        print('BOOM!!')
    else:
        root.geometry(f'{s}x{s}')
        root.configure(bg=random.choice(["white", "black", "red", "green", "blue", "cyan", "yellow", "magenta"]))
        root.after(2000, tick)
        print(int(8 - s/50))


tick()
root.mainloop()
