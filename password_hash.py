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
        self.window.geometry("671x365")
        self.window.title("Password  hasher")
        self.window.resizable(height=tk.FALSE,width=tk.FALSE)

        self.currentDir = tk.StringVar()
        self.currentDir.set(os.getcwd())

        tk.Entry(self.window,textvariable=self.currentDir,width=124).place(x=0,y=0)
        self.password_Frame = tk.LabelFrame(self.window,text="Password",fg="blue",padx=25,pady=10)
        self.password_Frame.grid(row=0,column=0,padx=19,pady=30)
        self.label1 = tk.Label(self.password_Frame,text="Enter Password:")
        self.label1.grid(pady=5,row=0,column=0)
        self.label2 = tk.Label(self.password_Frame,text="Confirm password:"+" "*6)
        self.label2.grid(pady=5,row=1,column=0)
        self.Entry1 = tk.Entry(self.password_Frame,width=75)
        self.Entry1.grid(pady=1,row=0,column=1)
        self.Entry2 = tk.Entry(self.password_Frame,width=75)
        self.Entry2.grid(pady=1,row=1,column=1)
        self.window.mainloop()

if __name__ == "__main__":
    Program()

