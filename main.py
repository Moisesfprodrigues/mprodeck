# MPRO Deck App
# Versão base - exemplo completo
import tkinter as tk
from tkinter import messagebox
import pygame, keyboard, os
from PIL import Image, ImageTk

pygame.mixer.init()
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
TOTAL=8

root=tk.Tk()
root.title("MPRO DECK APP")
root.geometry("620x430")
root.configure(bg="#181818")
root.resizable(False,False)

hotkeys=tk.BooleanVar(value=False)
sounds=[]
images=[]
default=[f"BOTÃO {i}" for i in range(1,TOTAL+1)]
labels=[]

for i in range(1,TOTAL+1):
    mp3=os.path.join(BASE_DIR,f"assets/audio/sample{i}.mp3")
    sounds.append(pygame.mixer.Sound(mp3) if os.path.exists(mp3) else None)

    png=os.path.join(BASE_DIR,f"assets/img/img{i}.png")
    if os.path.exists(png):
        im=Image.open(png).resize((72,72),Image.Resampling.LANCZOS)
        images.append(ImageTk.PhotoImage(im))
    else:
        images.append(None)

    txt=os.path.join(BASE_DIR,f"assets/text/label{i}.txt")
    if os.path.exists(txt):
        labels.append(open(txt,encoding="utf8").read().strip() or default[i-1])
    else:
        labels.append(default[i-1])

def play(i):
    if sounds[i]:
        sounds[i].play()
    else:
        messagebox.showerror("Erro",f"sample{i+1}.mp3 não encontrado")

def effect(b):
    c=b["bg"]
    b.configure(bg="#00C853")
    root.after(180,lambda:b.configure(bg=c))

def execute(i):
    effect(buttons[i]); play(i)

title=tk.Label(root,text="MPRO DECK APP",font=("Segoe UI",18,"bold"),
bg="#181818",fg="white")
title.pack(pady=10)

frame=tk.Frame(root,bg="#181818")
frame.pack()

buttons=[]
for i in range(TOTAL):
    b=tk.Button(frame,image=images[i],compound="top",
        text=f"{labels[i]}\n[{i+1}]",
        width=120,height=120,bg="#2A2A2A",fg="white",
        activebackground="#00C853",font=("Segoe UI",10,"bold"),
        relief="flat",wraplength=100,
        command=lambda n=i:execute(n))
    b.grid(row=i//4,column=i%4,padx=10,pady=10)
    buttons.append(b)

bottom=tk.Frame(root,bg="#181818")
bottom.pack(fill="x",pady=5)

def toggle():
    hotkeys.set(not hotkeys.get())
    if hotkeys.get():
        toggle_btn.config(text="🟢 Atalhos ON",bg="#2E7D32")
    else:
        toggle_btn.config(text="🔴 Atalhos OFF",bg="#B71C1C")

toggle_btn=tk.Button(bottom,text="🔴 Atalhos OFF",command=toggle,
bg="#B71C1C",fg="white",relief="flat")
toggle_btn.pack(side="left",padx=25)

tk.Label(bottom,text="© 2026 MPRO | Desenvolvido por Moisés Rodrigues",
bg="#181818",fg="#909090",font=("Segoe UI",8)).pack(side="right",padx=15)

for i in range(TOTAL):
    keyboard.add_hotkey(str(i+1),lambda n=i: root.after(0,lambda: execute(n)) if hotkeys.get() else None)

root.mainloop()
