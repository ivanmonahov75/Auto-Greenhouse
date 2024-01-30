import tkinter as tk
from tkinter import ttk

gh = tk.Tk()
gh.geometry('480x320')
gh.attributes('-fullscreen', True)
canvas = tk.Canvas(gh, width=480, height=320)
canvas.create_rectangle(0,0, 480, 320, fill='grey')
canvas.create_rectangle(0,0, 480, 32, fill='white')

canvas.create_text(115, 18, text='Reactor cores State:', fill='black', font='Helvetica 8 bold')
canvas.pack()

gh.mainloop()