import tkinter as tk
from tkinter.filedialog import asksaveasfile

#function
def save():
    dummycheck="Something"
    filetosave=asksaveasfile(defaultextension=".txt")
    if filetosave is not None:
        print(dummycheck, file=filetosave)

#window

window=tk.Tk()
window.geometry("500x500")
window.title("Save")

#button

savebutton=tk.Button(window,text="Save", command=save,bd=2)
savebutton.pack()

window.mainloop()