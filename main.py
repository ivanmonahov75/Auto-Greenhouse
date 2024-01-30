import tkinter as tk

gh = tk.Tk()
# gh.attributes('-fullscreen', True)
canvas = tk.Canvas(gh, width=480, height=320)
canvas.create_rectangle(0,0, 480, 320, fill='light grey')
canvas.pack()
gh.mainloop()