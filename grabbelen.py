import random
import tkinter as tk
import tkinter.messagebox

items = [
    'betere gui',
    '€10',
    'Kauwgom die onder de tafel zat',
    'Gebruikt zakdoekje',
    'Iemands sleutel',
    'Iemands sok',
    'Iemands portemonnee',
    'Mil\'s lege kauwgom bakje',
    'Random jumbo bonnetje',
    'Spel die je al hebt',
    'Ticket voor pretpark die dicht is door corona'
]


def randomColor():
    return random.choice(["white", "black", "red", "green", "blue", "cyan", "yellow", "magenta"])


def updateStr():
    amountStr.set(len(items))


def randomItem():
    i = random.choice(items)
    items.remove(i)

    return i


def grabbel():
    if len(items) == 0:
        tkinter.messagebox.showerror('Oops', 'Er is niks meer om te grabbelen')
    else:
        tkinter.messagebox.showinfo('Iets gevonden', f'Gefeliciteerd, je hebt een {randomItem()} gegrabbeld!')
        updateStr()


root = tk.Tk()
root.title('Grabbelen')
root.configure(bg=randomColor())

amountStr = tk.StringVar(value=len(items))

text = tk.Label(root, bg=randomColor(), fg=randomColor())
text.configure(textvariable=amountStr)
text.pack()

button = tk.Button(text='Grabbel', bg=randomColor(), fg=randomColor())
button.pack(pady=20, padx=20)
button.configure(command=grabbel)

updateStr()

root.mainloop()
