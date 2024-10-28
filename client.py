import socket  
from tqdm import tqdm
import tkinter as tk
tries = False
idx = 0

from tkinter import *
message = bytearray()         
# Creating Client Socket 
if __name__ == '__main__': 
    host = 'xxx.xxx.Xxx.xxx'
    port = 8080

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
fileno = 0
idx = 0
# Connecting with Server 
root = Tk()
root.geometry("300x300")
root.configure(background="black")
root.title(" Q&A ")
sock.connect((host, port)) 
print("connected to host")
print()
def Take_input():
    percent = 0
    l=0
    global a
    global b
    a = inputtxt.get()
    b = inputtxt2.get()
    c = a +"\\"+ b
    inputtxt.delete(0, 'end')
    inputtxt2.delete(0, 'end')
    if 1==1:
            if ":" in b:
                sock.send(bytes(c, "utf-8"))
            else:
                sock.send(bytes(a, "utf-8"))
            while True:
                    size=sock.recv(1024).decode()
                    print(size)
                    size = int(size)+1
                    for x in tqdm(range(int(size))):
                        message.extend(sock.recv(128))
                    with open(a, 'wb') as file:
                        output.insert(1.0, "DONE")
                        file.write(message)
                        print(message)
                        print(a)
                        file.close()
                    break
l = Label(text ="What file do you want to send?",bg= "black",fg="white")
inputtxt = Entry(root,
                bg = "light yellow")
l1 = Label(text ="What is it's location?",bg= "black",fg="white")
inputtxt2 = Entry(root,bg = "light cyan")
output = Text(root, height=3,bg = "light green")
Display = Button(root, height = 2,
                 width = 20, 
                 text ="Show",
                 bg="green",
                 command = lambda:Take_input())
padding2 = Text(height=0,
               width=0,
               padx=10,
               pady=20,
               borderwidth=0,
               bg="black")
padding = Text(height=0,
               width=0,
               padx=10,
               pady=20,
               borderwidth=0,
               bg="black")

l.pack()
inputtxt.pack()
l1.pack()
inputtxt2.pack()
padding.pack()
Display.pack()
padding2.pack()
output.pack()

mainloop()
print(a)
