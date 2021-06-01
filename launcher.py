class Launcher:
    def __init__(self):
        self.logique = Logique()
        # #### initialisation de la fenetre tkinter #####
        self.root = Tk()
        self.root.geometry("800x600")
        self.root.minsize(800, 600)
        self.root.maxsize(800, 600)
        self.root.title("genie")
        self.rep = None
        self.photo = PhotoImage(file="bann.png").zoom(19).subsample(22)
        self.constructeur(self.root, self.photo)
        self.fermeture()
        self.entry = None
        self.label = None

    def valider(self):
        try:
            valeur_entree = int(self.entry.get())
            valeur = self.logique.kernel(valeur_entree)
            self.label["text"] = valeur
        except ValueError:
            self.label["text"] = 'valeur non pris en charge'

    def valider2(self, event):
        try:
            valeur_entree = int(self.entry.get())
            valeur = self.logique.kernel(valeur_entree)
            self.label["text"] = valeur
        except ValueError:
            self.label["text"] = 'valeur non pris en charge'


    def constructeur(self, root, photo):
        ext = '''
nous vous proposons un petit application
qui peut facilement vous permettre,
non seulement de connaître mais aussi de maitriser,
les adjectifs cardinaux/ordinaux
Pour ce faire, nous vous proposons une interface
dans lequel vous entrez votre nombre(en chiffre)
compris entre 0 et 9999
et le logiciel s'occupera devous l'afficher en lettre 
                                
Amusez-vous !                       
                '''
        largeur = 800
        longeur = 280
        fram1 = Frame(root, bg="black", relief=SUNKEN)
        can = Canvas(root, width=largeur, height=longeur, bg='black')
        can.create_image(largeur / 2, longeur / 2, image=photo)
        can.place(relwidth=1)
        fram2 = Frame(root, bg='yellow', relief=SUNKEN)
        Label(fram2, text='APROPOS', fg='blue', bg='yellow', font=('bold', 20)).place(x=125, y=5)
        Label(fram2, text=ext, bg='white', fg='black', font=('red', 11)).place(x=2, y=70, width=480, relx=-0.1)
        fram2.place(relheight=0.28, width=400, height=520, y=290)
        fram3 = Frame(root, bg='black', relief=SUNKEN)
        fram3.place(relheight=0.28, width=800, height=520, y=290, x=400)
        Label(fram3, text='entrez ici le nombre :            x').place(x=10, y=20)
        Label(fram3, text='votre resultat devrez afficher ici bas', fg='black', bg='white', font=('',8)).place(x=5, y=100, width=390)
        self.entry = Entry(fram3, bg='white')
        self.entry.place(x=10, y=50, width=200, height=35)
        self.entry.bind("<Return>", self.valider2)
        self.label = Label(fram3, text="", bg='white',fg='blue', font=('', 14))
        self.label.place(x=20, y=180)

        boutton2 = Button(fram3, text='valider ', bg='black', fg='blue', command=self.valider)
        boutton2.place(x=250, y=50, width=140, height=35)
        Button(fram3, text='Quitter', bg='black', fg='red', command=self.com_ok).place(x=10, y=270, width=380)
        # construction du frame dans lequel on mettra nos bouttons
        fram1.place(height=longeur, x=0, y=0)

    def launcher_game(self):
        print("hello")

    def com_ok(self):
        self.rep = askokcancel("confirmer la fermeture ", "voulez vraiment quitter?")
        if self.rep:
            self.root.quit()

    def fermeture(self):
        self.root.protocol("WM_DELETE_WINDOW", self.com_ok)
        self.root.mainloop()


# prorgramme principal
if __name__ == '__main__':
    from tkinter import *
    from tkinter.messagebox import askokcancel
    from application import Logique
    genie = Launcher()

