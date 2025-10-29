from tkinter import *
import tkinter as tk
#information de l'interface
window = Tk()
window.geometry("250x250")
window.title("Calculatrice")
window.minsize(250, 250)
window.maxsize(250, 400)

#creation des bouttons et affichage
var = tk.StringVar()
entry = Entry(window, textvariable=var, font=("Arial", 18))
entry.grid(row=0, column=0, columnspan=4, padx=0, pady=0)
# les bouttons et la fonction de sortie
def deleteCe():
    entry.delete(0, END)
def delete():
    entry.delete(0, 1)
def ajouter(element):
    var.set(var.get() + element)
button1= Button(window, text='1', width=5, height=2, command=lambda: ajouter("1")).grid(row=1, column=0, padx=0)
button2= Button(window, text='2', width=5, height=2, command=lambda: ajouter("2")).grid(row=1, column=1, padx=0)
button3= Button(window, text='3', width=5, height=2, command=lambda: ajouter("3")).grid(row=1, column=2, padx=0)
button_addition= Button(window, text='+', width=5, height=2, command=lambda: ajouter("+")).grid(row=1, column=3, padx=0)
button4= Button(window, text='4', width=5, height=2, command=lambda: ajouter("4")).grid(row=2, column=0, padx=0)
button5= Button(window, text='5', width=5, height=2, command=lambda: ajouter("5")).grid(row=2, column=1, padx=0)
button6= Button(window, text='6', width=5, height=2, command=lambda: ajouter("6")).grid(row=2, column=2, padx=0)
button_soustraction= Button(window, text='-', width=5, height=2, command=lambda: ajouter("-")).grid(row=2, column=3, padx=0)
button7= Button(window, text='7', width=5, height=2, command=lambda: ajouter("7")).grid(row=3, column=0, padx=0)
button8= Button(window, text='8', width=5, height=2, command=lambda: ajouter("8")).grid(row=3, column=1, padx=0)
button9= Button(window, text='9', width=5, height=2, command=lambda: ajouter("9")).grid(row=3, column=2, padx=0)
button_multiplication= Button(window, text='*', width=5, height=2, command=lambda: ajouter("*")).grid(row=4, column=0, padx=0)
button0= Button(window, text='0', width=5, height=2, command=lambda: ajouter("0")).grid(row=4, column=1, padx=0)
button_division= Button(window, text='/', width=5, height=2, command=lambda: ajouter("/")).grid(row=4, column=2, padx=0)
button_effacer= Button(window, text='effacer', width=5, height=2, command=delete).grid(row=4, column=3, padx=0)
button_effacerce= Button(window, text='CE', width=5, height=2, command=deleteCe).grid(row=5, column=1, padx=0)
# sortie du resultat
def resultat():
    recup = var.get()
    try:
      resultat= eval(recup)
      entry.delete(0, END)
      entry.insert(0, resultat)
    except:
        texte = "impossible"
        entry.delete(0, END)
        entry.insert(0, texte)


button_egalite_resultat= Button(window, text='=', width=5, height=2, command=resultat).grid(row=3, column=3, padx=0)
window.mainloop()
# jz veux juste apprendre à mieux coder
