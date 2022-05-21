import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import asksaveasfile

def save(random):
    files = [('Fichier Texte', '.txt')]
    file = asksaveasfile(filetypes = files, defaultextension = files)
    file.write(random)
    file.close

def choice(array):
    frame = tk.Tk()
    frame.title("Exercice Math")
    lbl = tk.Label(frame, text = "Combien d'élèves voulez vous tirer au sort ?")
    lbl.pack()
    inputtxt = tk.Text(frame,
                    height = 5,
                    width = 20)
    inputtxt.pack()
    def printInput1():
        x = int(inputtxt.get(1.0, "end-1c"))
        random = str(np.random.choice(array, size=x, replace=False))
        frame.destroy()
        if x > len(array):
            frm = ttk.Frame(tk.Tk(), padding=10)
            frm.grid()
            tk.Label(frm, text="Vous avez mis une valeur supérieur au nombre d'élèves, veuilez mettre un nombre entre 1 et " + str(len(array))).grid(column=0, row=0)
            choice(array)
        elif x < 1:
            frm = ttk.Frame(tk.Tk(), padding=10)
            frm.grid()
            tk.Label(frm, text="Vous ne pouvez pas mettre moins qu'un élève, ça serait bête :(").grid(column=0, row=0)
            choice(array)
        elif x == 1:
            frm = ttk.Frame(tk.Tk(), padding=10)
            frm.grid()
            tk.Label(frm, text="L'élève tiré au sort est: " + random).grid(column=0, row=0)
            tk.Button(frm, text = "Sauvegarder l'élève", command = lambda : save(random)).grid(column=0, row=1) 
        else:
            
            frm = ttk.Frame(tk.Tk(), padding=10)
            frm.grid()
            tk.Label(frm, text="Les élèves tirés au sort sont: " + random).grid(column=0, row=0)  
            tk.Button(frm, text = 'Sauvegarder les élèves', command = lambda : save(random)).grid(column=0, row=1) 
            
    printButton = tk.Button(frame,
                        text = "Tirage au sort", 
                        command = printInput1)
    printButton.pack()
    frame.mainloop()

def main():
    frame = tk.Tk()
    frame.title("Exercice Math")
    lbl = tk.Label(frame, text = "Bonjour Mr. Guary :)\nComment se nomme vos nouveaux élèves ?")
    lbl.pack()
    inputtxt = tk.Text(frame,
                        height = 5,
                        width = 20)
    inputtxt.pack()
    def printInput():
        array = list(map(str, inputtxt.get(1.0, "end-1c").strip().split()))
        frame.destroy()
        if not array: 
            frm = ttk.Frame(tk.Tk(), padding=10)
            frm.grid()
            tk.Label(frm, text="Veuillez entrer au moins 1 élèves").grid(column=0, row=0)
            main()
        else: 
            choice(array)

    printButton = tk.Button(frame,
                        text = "Continuer", 
                        command = printInput)
    printButton.pack()
    frame.mainloop()
main()
