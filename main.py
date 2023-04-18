from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import sqlite3


def ajouter():
    matricule = entrermatricule.get()
    nom = entrernom.get()
    prenom = entrerPrenom.get()
    age = entrerage.get()
    adresse = entreradresse.get()
    telephone = entrertelephone.get()
    remarque = entrerremarque.get()

    # Creeon la connexion
    con = sqlite3.connect('hopital.db')
    cuser = con.cursor()
    cuser.execute("insert into patient('code','nom','prenom','age','adresse','telephone','remarque') values (?,?,?,?,?,?,?)",
                  (matricule, nom, prenom, age, adresse, telephone, remarque))
    con.commit()
    con.close()
    messagebox.showinfo("Patient ajouter")

    # afficher
    con = sqlite3.connect('hopital.db')
    cuser = con.cursor()
    select = cuser.execute("select *from patient order by code desc")
    select = list(select)
    table.insert('', END, values=select[0])
    con.close()


def modifier():
    matricule = entrermatricule.get()
    nom = entrernom.get()
    prenom = entrerPrenom.get()
    age = entrerage.get()
    adresse = entreradresse.get()
    telephone = entrertelephone.get()
    remarque = entrerremarque.get()

    # Creeon la connexion
    con = sqlite3.connect('hopital.db')
    cuser = con.cursor()
    cuser.execute(
        "update patient set nom=?,prenom=?,age=?,adresse=?,telephone=?,remarque=? where code=?",
        (nom, prenom, age, adresse, telephone, remarque, matricule))
    con.commit()
    con.close()
    messagebox.showinfo("Patient Modifier")

    # afficher
    con = sqlite3.connect('hopital.db')
    cuser = con.cursor()
    select = cuser.execute("select * from patient order by code desc")
    select = list(select)
    table.insert('', END, values=select[0])
    con.close()


def supprimer():
    codeSelectionner = table.item(table.selection())['values'][0]
    con = sqlite3.connect("hopital.db")
    cuser = con.cursor()
    delete = cuser.execute(
        "delete from patient where code = {}".format(codeSelectionner))
    con.commit()
    table.delete(table.selection())


# titre general
root = Tk()
root.title("Gestion des patient ")
root.geometry("1300x700")


# Ajouter le titre
lbltitre = Label(root, bd=20, relief=RIDGE, text="GESTION DES PATIENTS CHEZ JBDEVHOPITAL95", font=(
    "Arial", 30), bg="darkblue", fg="white")
lbltitre.place(x=0, y=0, width=1365)

# Liste des patients
lblListePatient = Label(root, text="LISTES DES PATIENTS ", font=(
    "Arial", 16), bg="darkblue", fg="white")
lblListePatient.place(x=600, y=100, width=760)


# text matricule
lblmatricule = Label(root, text="Matricule Patient",
                     font=("Arial", 16), bg="black", fg="white")
lblmatricule.place(x=0, y=100, width=200)
entrermatricule = Entry(root)
entrermatricule.place(x=200, y=100, width=160, height=30)

# text nom
lblnom = Label(root, text="Nom Patient", font=(
    "Arial", 16), bg="black", fg="white")
lblnom.place(x=0, y=150, width=200)
entrernom = Entry(root)
entrernom.place(x=200, y=150, width=200, height=30)

# text prenom
lblPrenom = Label(root, text="Prenom Patient", font=(
    "Arial", 16), bg="black", fg="white")
lblPrenom.place(x=0, y=200, width=200)
entrerPrenom = Entry(root)
entrerPrenom.place(x=200, y=200, width=200, height=30)

# text age
lblage = Label(root, text="Age Patient", font=(
    "Arial", 16), bg="black", fg="white")
lblage.place(x=0, y=250, width=200)
entrerage = Entry(root)
entrerage.place(x=200, y=250, width=100, height=30)

# text adresse
lbladresse = Label(root, text="Adresse Patient",
                   font=("Arial", 16), bg="black", fg="white")
lbladresse.place(x=0, y=300, width=200)
entreradresse = Entry(root)
entreradresse.place(x=200, y=300, width="300", height=30)

# text Telephone
lbltelephone = Label(root, text="Telephone Patient",
                     font=("Arial", 16), bg="black", fg="white")
lbltelephone.place(x=0, y=350, width=200)
entrertelephone = Entry(root)
entrertelephone.place(x=200, y=350, width=200, height=30)

# text remarque
lblremarque = Label(root, text="Remarque Patient",
                    font=("Arial", 16), bg="black", fg="white")
lblremarque.place(x=0, y=400, width=200)
entrerremarque = Entry(root)
entrerremarque.place(x=200, y=400, width=300, height=30)


# Enregistrer
btnenregistrer = Button(root, text="Enregistrer", font=(
    "Arial", 16), bg="darkblue", fg="yellow", command=ajouter)
btnenregistrer.place(x=30, y=450, width=200)

# modifier
btnmodofier = Button(root, text="Modifier", font=(
    "Arial", 16), bg="darkblue", fg="yellow", command=modifier)
btnmodofier.place(x=270, y=450, width=200)

# Supprimer
btnSupprimer = Button(root, text="Supprimer", font=(
    "Arial", 16), bg="darkblue", fg="yellow", command=supprimer)
btnSupprimer.place(x=150, y=500, width=200)


# Table
table = ttk.Treeview(root, columns=(1, 2, 3, 4, 5, 6, 7),
                     height=5, show="headings")
table.place(x=600, y=150, width=760, height=450)

# Entete
table.heading(1, text="CODE")
table.heading(2, text="NOM")
table.heading(3, text="PRENOM")
table.heading(4, text="AGE")
table.heading(5, text="ADRESSE")
table.heading(6, text="TELEPHONE")
table.heading(7, text="REMARQUE")

# definir les dimentions des colonnes
table.column(1, width=50)
table.column(2, width=150)
table.column(3, width=150)
table.column(4, width=50)
table.column(5, width=150)
table.column(6, width=100)
table.column(7, width=150)

# afficher les informations de la table
con = sqlite3.connect('hopital.db')
cuser = con.cursor()
select = cuser.execute("select * from patient")
for row in select:
    table.insert('', END, value=row)
con.close()


root.mainloop()
