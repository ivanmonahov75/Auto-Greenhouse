import tkinter as tk
from tkinter import ttk

gh = tk.Tk()
gh.geometry('480x320')
gh.attributes('-fullscreen', True)
canvas = tk.Canvas(gh, width=480, height=320)

canvas.create_rectangle(0,0, 480, 320, fill='grey')
canvas.create_rectangle(0,0, 480, 30, fill='white')

canvas.create_text(35, 14, text='Cores:', fill='black', font='Helvetica 11 bold')

canvas.create_text(120, 14, text='Current state:', fill='black',  font='Helvetica 11 bold')
canvas.create_text(210, 14, text='Util,%', fill='black',  font='Helvetica 11 bold')
canvas.create_text(275, 14, text='Prod,%', fill='black',  font='Helvetica 11 bold')
canvas.create_text(350, 14, text='Temp,C°', fill='black',  font='Helvetica 11 bold')
canvas.create_text(430, 14, text='Action', fill='black',  font='Helvetica 11 bold')

btn = []
pixel = tk.PhotoImage(width=1, height=1)

for i in range(4):
    canvas.create_text(38, 45+i*25, text=f'Core {i+1}:', fill='black', font='Helvetica 11 bold')
    canvas.create_text(120, 45+i*25, text='Online', fill='black', font='Helvetica 11 bold')
    canvas.create_text(210, 45+i*25, text=f'{34 + i*10}%', fill='black', font='Helvetica 11 bold')
    canvas.create_text(275, 45+i*25, text=f'{34 + i*10}%', fill='black', font='Helvetica 11 bold')
    canvas.create_text(350, 45+i*25, text=f'{34 + i*10}C°', fill='black', font='Helvetica 11 bold')

    btn.append(tk.Button(gh, image=pixel, width=35, height=15, text='Stop', command=gh.destroy, font='Helvetica 11 bold'))
    btn[i].place(x=435, y=33+i*25)
    canvas.create_text(410, 45+i*25, text='Stop', fill='black', font='Helvetica 11 bold')

canvas.create_rectangle(0, 150, 480, 180, fill='white')

canvas.pack()

gh.mainloop()
