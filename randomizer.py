import tkinter as tk
import webbrowser
from tkinter import ttk
import random

def nurvus_translations(event):
    webbrowser.open_new("https://yumpoplala.com/phantasystar/")

def noxium_elysium(event):
    webbrowser.open_new("https://rykros.github.io/Noxium-Elysium/")

def generate_battle_points():
    table = [[-1 for _ in range(10)] for _ in range(2)]
    
    for i in range(2):
        numbers = list(range(10))
        random.shuffle(numbers)
        for j in range(10):
            while numbers[j] in [table[x][j] for x in range(i)]:
                random.shuffle(numbers)
            table[i][j] = numbers[j]

    return table

def update_table():
    new_table = generate_battle_points()
    for i in range(2):
        battle_point_table.item(i, values=new_table[i])

root = tk.Tk()
icon_path = "./alis.png"
icon = tk.PhotoImage(file=icon_path)
root.iconphoto(True, icon)
root.configure(bg="white")
root.title("Alisa's Adventure Battle Point Table Randomizer")
root.geometry("500x545")
root.configure(bg="white")

title_path = "./title.png"
title = tk.PhotoImage(file=title_path)
title_label = tk.Label(root, image=title, border=0)
title_label.pack(pady=10)

battle_point_table = ttk.Treeview(root, columns=("A", "B", "C", "D", "E", "F", "G", "H", "I", "J"), height=2, padding=2)

battle_point_table.heading("#0", text="", anchor=tk.W)
for letter in "ABCDEFGHIJ":
    battle_point_table.heading(letter, text=letter, anchor=tk.CENTER)

battle_point_table.column("#0", width=50, anchor=tk.W)
for letter in "ABCDEFGHIJ":
    battle_point_table.column(letter, width=25, anchor=tk.CENTER)

for i in range(2):
    battle_point_table.insert(parent="", index="end", iid=i, text=f"{i+1}", values=("0", "0", "0", "0", "0", "0", "0", "0", "0", "0"))

battle_point_table.pack(fill=tk.NONE, padx=10, pady=10, expand=False)

generate_button = tk.Button(root, text="Generate Battle Points", command=update_table)
generate_button.pack(pady=(10, 75))

mitsutaka = tk.Label(root, text="Original Book Written by Mitsutaka Ode", bg="white")
mitsutaka.pack(pady=0)

lala_frame = tk.Frame(root, bg="white")
lala_frame.pack(pady=0)
lala = tk.Label(lala_frame, text="Translated by Lala Landale", bg="white")
lala.pack(side=tk.LEFT, padx=0)
nurvus_link = tk.Label(lala_frame, text="@ Nurvus Translations", fg="blue", bg="white", cursor="hand2")
nurvus_link.pack(side=tk.LEFT)

rykros_frame = tk.Frame(root, bg="white")
rykros_frame.pack(pady=0)
rykros = tk.Label(rykros_frame, text="App © 2024 Ricky 'Rykros' Runyon", bg="white")
rykros.pack(side=tk.LEFT, padx=0)
noxium_link = tk.Label(rykros_frame, text="@ Noxium Elysium", fg="blue", bg="white", cursor="hand2")
noxium_link.pack(side=tk.LEFT)

sega = tk.Label(root, text="Phantasy Star © 1987-2024 SEGA", bg="white")
sega.pack(pady=0)

nurvus_link.bind("<Button-1>", nurvus_translations)
noxium_link.bind("<Button-1>", noxium_elysium)

root.mainloop()