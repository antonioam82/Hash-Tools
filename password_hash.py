#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import tkinter as tk
from tkinter import messagebox
import threading
import pyperclip
import os

class Program:
    def __init__(self):

        self.window = tk.Tk()
        self.window.geometry("681x490")
        self.window.title("Password  hasher")
        self.window.resizable(height=tk.FALSE,width=tk.FALSE)

        self.currentDir = tk.StringVar()
        self.currentDir.set(os.getcwd())
        self.password = tk.StringVar()
        self.confirmPassword = tk.StringVar()#
        self.algorithms = ["md5","sha1","sha224","sha256","sha384","sha512"]
        self.md5H = tk.StringVar()
        self.sha1H = tk.StringVar()
        self.sha224H = tk.StringVar()
        self.sha256H = tk.StringVar()
        self.sha384H = tk.StringVar()
        self.sha512H = tk.StringVar()

        tk.Entry(self.window,textvariable=self.currentDir,width=124).place(x=0,y=0)
        tk.Label(self.window,font=('Arial',20,'bold'),text="Password Hasher").grid(row=0,column=0,padx=25,pady=20)
        self.password_Frame = tk.LabelFrame(self.window,text="Password",fg="blue",padx=25,pady=18)
        self.password_Frame.grid(row=2,column=0,padx=19,pady=4)
        tk.Label(self.password_Frame,text="Enter Password:").grid(pady=5,row=0,column=0)
        tk.Label(self.password_Frame,text="Confirm password:"+" "*6).grid(pady=5,row=1,column=0)
        self.Entry1 = tk.Entry(self.password_Frame,textvariable=self.password,width=69,show="*")
        self.Entry1.grid(pady=1,row=0,column=1)
        self.Entry1.focus()
        self.Entry2 = tk.Entry(self.password_Frame,textvariable=self.confirmPassword,width=69,show="*")
        self.Entry2.grid(pady=1,row=1,column=1)
        self.see1 = tk.Button(self.password_Frame,text="SHOW",width=5,command=lambda:self.hider(0))
        self.see1.grid(padx=2,row=0,column=2)
        self.see2 = tk.Button(self.password_Frame,text="SHOW",width=5,command=lambda:self.hider(1))
        self.see2.grid(padx=2,row=1,column=2)

        self.output_Frame = tk.LabelFrame(self.window,text="Password hash",fg="blue",padx=25,pady=10)
        self.output_Frame.grid(row=3,column=0,padx=19,pady=0)
        tk.Label(self.output_Frame,text="MD5").grid(pady=5,row=0,column=0)
        tk.Label(self.output_Frame,text="SHA1").grid(pady=5,row=1,column=0)
        tk.Label(self.output_Frame,text="SHA224    ").grid(pady=5,row=2,column=0)
        tk.Label(self.output_Frame,text="SHA256    ").grid(pady=5,row=3,column=0)
        tk.Label(self.output_Frame,text="SHA384    ").grid(pady=5,row=4,column=0)
        tk.Label(self.output_Frame,text="SHA512    ").grid(pady=5,row=5,column=0)
        self.md5Out = tk.Entry(self.output_Frame,textvariable=self.md5H,width=75)
        self.md5Out.grid(pady=1,row=0,column=1)
        self.sha1Out = tk.Entry(self.output_Frame,textvariable=self.sha1H,width=75)
        self.sha1Out.grid(pady=1,row=1,column=1)
        self.sha224Out = tk.Entry(self.output_Frame,textvariable=self.sha224H,width=75)
        self.sha224Out.grid(pady=1,row=2,column=1)
        self.sha256Out = tk.Entry(self.output_Frame,textvariable=self.sha256H,width=75)
        self.sha256Out.grid(pady=1,row=3,column=1)
        self.sha384Out = tk.Entry(self.output_Frame,textvariable=self.sha384H,width=75)
        self.sha384Out.grid(pady=1,row=4,column=1)
        self.sha512Out = tk.Entry(self.output_Frame,textvariable=self.sha512H,width=75)
        self.sha512Out.grid(pady=1,row=5,column=1)
        tk.Button(self.output_Frame,text="COPY",width=9,command=lambda:self.copy_hash(0)).grid(padx=2,row=0,column=2)
        tk.Button(self.output_Frame,text="COPY",width=9,command=lambda:self.copy_hash(1)).grid(padx=2,row=1,column=2)
        tk.Button(self.output_Frame,text="COPY",width=9,command=lambda:self.copy_hash(2)).grid(padx=2,row=2,column=2)
        tk.Button(self.output_Frame,text="COPY",width=9,command=lambda:self.copy_hash(3)).grid(padx=2,row=3,column=2)
        tk.Button(self.output_Frame,text="COPY",width=9,command=lambda:self.copy_hash(4)).grid(padx=2,row=4,column=2)
        tk.Button(self.output_Frame,text="COPY",width=9,command=lambda:self.copy_hash(5)).grid(padx=2,row=5,column=2)

        tk.Button(self.window,text="CREATE HASH",command=self.init_task).grid(pady=20,row=4,column=0)
        self.buttons = [self.see1,self.see2]
        self.password_entries = [self.Entry1,self.Entry2]
        self.hashes_outputs = [self.md5H,self.sha1H,self.sha224H,self.sha256H,self.sha384H,self.sha512H]
        self.hashes = []

        self.window.mainloop()

    def check_passwords(self):
        if self.Entry1.get() != "" and self.Entry2.get() != "":
            if self.Entry1.get() == self.Entry2.get():
                self.hash()
            else:
                messagebox.showwarning("ERROR","Passwords doesn't match")
                #self.Entry1.delete(0,tk.END)
                #self.Entry2.delete(0,tk.END)
        else:
            messagebox.showwarning("PASSWORD NOT PROVIDED","Enter password for hashing and confirm")
            

    def init_task(self):
        threading.Thread(target=self.check_passwords).start()

    def hash(self):
        data = self.Entry1.get()
        b_data = bytes(data, 'utf-8')
        c = 0
        for i in self.algorithms:
            hasher = hashlib.new(self.algorithms[c],b_data)
            hash_ = hasher.hexdigest()
            print(hash_)
            self.hashes_outputs[c].set(hash_)
            self.hashes.append(hash_)
            c+=1

    def copy_hash(self,v):
        try:
            if len(self.hashes_outputs[v].get()) > 1:
                pyperclip.copy(self.hashes_outputs[v].get())
                messagebox.showinfo("COPIED","Copied to clipboard.")
        except Exception as e:
            messagebox.showwarning("UNEXPECTED ERROR",str(e))
            
    def hider(self,v):
        if self.password_entries[v].get() != "":
            if self.password_entries[v]['show'] == "*":
                self.password_entries[v]['show'] = ""
                self.buttons[v]['text'] = "HIDE"
            else:
                self.password_entries[v]['show'] = "*"
                self.buttons[v]['text'] = "SHOW"

if __name__ == "__main__":
    Program()


