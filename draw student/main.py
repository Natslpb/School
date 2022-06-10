from email.quoprimime import decode
import numpy as np
import tkinter as tk
from tkinter import Button, ttk
from tkinter import filedialog as fd

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
        random = ", ".join(np.random.choice(array, size=x, replace=False))
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

def save(random):
    files = [('Fichier Texte', '.txt')]
    file = fd.asksaveasfile(filetypes = files, defaultextension = files)
    file.write(random)
    file.close
    
def select_file():
    filetypes = (
        ('Fichier texte', '*.txt'),
    )
    filename = fd.askopenfilename(
        title='Séléctionné un fichier',
        initialdir='/',
        filetypes=filetypes)

    def tirage(): 
        def remove():
            file = open(filename).read()
            if file.find(",") != -1:
                return open(filename).read().replace(",", "")
            else: 
                return file
            
            
        array = list(map(str, remove().strip().split()))
        if not array: 
            frm = ttk.Frame(tk.Tk(), padding=10)
            frm.grid()
            tk.Label(frm, text="Votre fichier ne contient rien").grid(column=0, row=0)
            select_file()
        else: 
            choice(array)
    tirage()

def jsp():
    
    frame = tk.Tk()
    frame.title("Exercice Math")
    lbl = tk.Label(frame, text = "Du comment se nomme vos nouveaux élèves ?")
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

def main():
    frm = tk.Tk()
    def ikd():
        frm.destroy()
        jsp()
    def ok():
        frm.destroy()
        select_file()
    frm.grid()
    tk.Label(frm, text="Bonjour Mr. Guary :)\nVoulez vous récupérer les élèves à partir d'un fichier\nOu bien de les écrire vous même").grid(column=0, row=0)
    file = ttk.Button(frm, text="Sélectionner un fichier", command=ok).grid(column=1, row=0)
    name = ttk.Button(frm, text="Entrer les noms", command=ikd).grid(column=1, row=1)
    ttk.Button(frm, text="Quitter", command=exit).grid(column=1, row=2)
    frm.mainloop()
main()
