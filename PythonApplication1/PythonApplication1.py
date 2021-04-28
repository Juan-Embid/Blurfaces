from tkinter import *
from tkinter import filedialog
import subprocess, os

root = Tk()

def browseFiles():
    filedialog.askopenfilename(initialdir = "", title = "Select a File", filetypes = (("all files", "*.*"), ("Text files", "*.txt*")))
def openCamera():
  os.system('cmd /c "start microsoft.windows.camera:"')

browse = Button(root, text = "Browse files", command = browseFiles)
browse.pack()
camera = Button(root, text = "Open camera", command = openCamera)
camera.pack()
root.title("BlurApp")
root.geometry("600x300")
root.mainloop()