
from ast import Delete
from cgitb import text
from email.mime import image

import tkinter as tk
from tkinter import*
from tkinter import ttk
from turtle import bgcolor
from PIL import Image, ImageTk


#create the main window
logs=Tk()
logs.geometry("350x400")
logs.title("Insturmentu noma")
logs.configure(bg="lightgreen")

logo_frame= tk.Frame(logs)
logo_frame.grid(row=6, column=0, columnspan=5, padx=10,pady=10)

logo_image =Image.open("istsais spy2ttf2.png")
resized_logo= logo_image.resize((200,200))
logo= ImageTk.PhotoImage(resized_logo)
logo_label= ttk.Label(logo_frame, image=logo)
logo_label.grid(row=6,column=1, columnspan=55, padx=50, pady=50)

btn=Button(logs, text="pasūtījums", bd="10", command=lambda: pasutijums())
btn1=Button(logs, text="aizvērt", bd="10", command=logs.destroy)
btn.grid(row=1, column=1, padx=25, pady=25)
btn1.grid(row=1, column=3, padx=25, pady=25)


def pasutijums():
    logs1=Toplevel()
    logs1.geometry("350x350")
    logs1.title("Instrumetu saraksts")
    


    ttk.Label(logs1, text="Izvēlies darbinieku:", foreground="green").grid(column=1, row=3, padx=20, pady=20,)
    ttk.Label(logs1, text="Izvēlies instrumentu").grid(column=1, row=4, padx=20, pady=20)
    ttk.Label(logs1, text="Norādi cenu:").grid(column=1, row=5, padx=20, pady=20)
    ttk.Label(logs1, text="Nomas dienas:").grid(column=1, row=6, padx=20, pady=20)

#maingie
    vardsuzvards=tk.StringVar()
    instruments=tk.StringVar()
    cena=tk.StringVar()
    dienas=tk.StringVar()

    
    darbinieki = ttk.Combobox(logs1, textvariable=vardsuzvards,)
    darbinieki['state']='readonly'
    instrumenti = ttk.Combobox(logs1, textvariable=instruments)
    instrumenti['state']='readonly'
    nomascena = ttk.Combobox(logs1, textvariable=cena)
    nomascena['state']='readonly'
    nomasdiena = ttk.Entry(logs1, textvariable=dienas)

    darbinieki["values"] =("Kārlis Bērziņš", "Asafs Alpe", "Niks Močuļskis")
    instrumenti["values"] =("Lenova", "Asus", "Toshiba")
    nomascena["values"] =("450", "555", "1100")


    darbinieki.grid(column=3, row=3, padx=20, pady=20)
    instrumenti.grid(column=3, row=4, padx=20, pady=20)
    nomascena.grid(column=3, row=5, padx=20, pady=20)
    nomasdiena.grid(column=3, row=6, padx=20, pady=20)


    def rezultats():
        selected_item3=nomascena.get()
        value=int(nomasdiena.get())
        values={"450": 450,"555":555, "1100":1100}
        cena=values[selected_item3]
        result=value*cena
        result_label.config(text=f"Result: {result} eiro")

    btn2=tk.Button(logs1, text="apreķināt", command= lambda:rezultats())
    btn2.grid(row=11, column=1)
    result_label = tk.Label(logs1)
    result_label.grid(row=11,column=3)
    btn3=tk.Button(logs1, text="aizvērt", bd="10", command=logs1.destroy)
    btn3.grid(row=13, column=3 )



    


logs.mainloop()