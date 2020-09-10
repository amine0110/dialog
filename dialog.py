from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image as img

root = Tk()
root.geometry("400x500")

root.filename = filedialog.askopenfilename(title="select a pic", filetypes=(("png files", "*.png"),("all", "*.*")))
button = Button(root, text="open",width=20, height=2)
fram= Frame(root, width=400, height=450, bg="red")


canvas = Canvas(root, width=400, height=450, bg="red")
lab = Label(canvas, text="hello amine how are you")


button.pack()
canvas.pack()
lab.grid(row=0, column=0, ipadx=100)
mainloop()