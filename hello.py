import random
import tkinter as tk


def randomColor():
    return random.choice(["white", "black", "red", "green", "blue", "cyan", "yellow", "magenta"])


root = tk.Tk()
root.title('Hello')
root.configure(bg=randomColor())

text = tk.Text(root, bg=randomColor(), fg=randomColor())
text.insert(1.0, "Hello World")
text.configure(state='disabled')
text.pack(pady=20, padx=20)

root.mainloop()
