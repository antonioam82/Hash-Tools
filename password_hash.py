import hashlib
import tkinter as tk
from tkinter import messagebox
#import threading
import pyautogui
import getpass
import os

class Program:
    def __init__(self):

        self.window = tk.Tk()
        self.window.geometry("750x445")
        self.window.title("Password  hasher")

        self.currentDir = tk.StringVar()
        self.currentDir.set(os.getcwd())

        tk.Entry(self.window,textvariable=self.currentDir,width=124).place(x=0,y=0)

        self.window.mainloop()

if __name__ == "__main__":
    Program()
