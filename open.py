import tkinter as tk
from tkinter.filedialog import askopenfile

#function

def open_File():
    file=askopenfile(mode="r", filetypes=[("python files","*.py")])
    if file is not None:
        content=file.read()
        print(content)
#window

window=tk.Tk()
window.geometry("500x500")
window.title("Open")

#button

openbutton=tk.Button(window,text="Open", command=open_File)
openbutton.pack()



window.mainloop()