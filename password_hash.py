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
        self.window.geometry("671x460")
        self.window.title("Password  hasher")
        #self.window.resizable(height=tk.FALSE,width=tk.FALSE)

        self.currentDir = tk.StringVar()
        self.currentDir.set(os.getcwd())
        algoritmos = ["md5","sha1","sha224","sha256","sha384","sha512"]

        tk.Entry(self.window,textvariable=self.currentDir,width=124).place(x=0,y=0)
        self.password_Frame = tk.LabelFrame(self.window,text="Password",fg="blue",padx=25,pady=10)
        self.password_Frame.grid(row=0,column=0,padx=19,pady=30)
        tk.Label(self.password_Frame,text="Enter Password:").grid(pady=5,row=0,column=0)
        tk.Label(self.password_Frame,text="Confirm password:"+" "*6).grid(pady=5,row=1,column=0)
        self.Entry1 = tk.Entry(self.password_Frame,width=75)
        self.Entry1.grid(pady=1,row=0,column=1)
        self.Entry2 = tk.Entry(self.password_Frame,width=75)
        self.Entry2.grid(pady=1,row=1,column=1)
        

        self.output_Frame = tk.LabelFrame(self.window,text="Password hash",fg="blue",padx=25,pady=10)
        self.output_Frame.grid(row=1,column=0,padx=19,pady=0)
        tk.Label(self.output_Frame,text="MD5").grid(pady=5,row=0,column=0)
        tk.Label(self.output_Frame,text="SHA1").grid(pady=5,row=1,column=0)
        tk.Label(self.output_Frame,text="SHA224").grid(pady=5,row=2,column=0)
        tk.Label(self.output_Frame,text="SHA256").grid(pady=5,row=3,column=0)
        tk.Label(self.output_Frame,text="SHA384").grid(pady=5,row=4,column=0)
        tk.Label(self.output_Frame,text="SHA512").grid(pady=5,row=5,column=0)
        self.md5Out = tk.Entry(self.output_Frame,width=75)
        self.md5Out.grid(pady=1,row=0,column=1)
        self.sha1Out = tk.Entry(self.output_Frame,width=75)
        self.sha1Out.grid(pady=1,row=1,column=1)
        self.sha224Out = tk.Entry(self.output_Frame,width=75)
        self.sha224Out.grid(pady=1,row=2,column=1)
        self.sha256Out = tk.Entry(self.output_Frame,width=75)
        self.sha256Out.grid(pady=1,row=3,column=1)
        self.sha384Out = tk.Entry(self.output_Frame,width=75)
        self.sha384Out.grid(pady=1,row=4,column=1)
        self.sha512Out = tk.Entry(self.output_Frame,width=75)
        self.sha512Out.grid(pady=1,row=5,column=1)
        tk.Button(self.output_Frame,text="COPY",width=9).grid(padx=2,row=0,column=2)
        tk.Button(self.output_Frame,text="COPY",width=9).grid(padx=2,row=1,column=2)
        tk.Button(self.output_Frame,text="COPY",width=9).grid(padx=2,row=2,column=2)
        tk.Button(self.output_Frame,text="COPY",width=9).grid(padx=2,row=3,column=2)
        tk.Button(self.output_Frame,text="COPY",width=9).grid(padx=2,row=4,column=2)
        tk.Button(self.output_Frame,text="COPY",width=9).grid(padx=2,row=5,column=2)

        tk.Button(self.window,text="CREATE HASH").grid(pady=20,row=2,column=0)

        self.window.mainloop()

if __name__ == "__main__":
    Program()


