from cProfile import label
from tkinter import Tk, Label, font

window = Tk()
window.title("Digital Clock")
window.geometry("600x300")

window.configure(bg="steelblue")

label = Label(window, text="Heyaaa", font=("Arial Black",78,"bold"),bg="steelblue" ,fg="white")
label.pack(pady=100)

window.mainloop()

