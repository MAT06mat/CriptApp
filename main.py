import tkinter as tk
from tkinter import PhotoImage
from random import randrange



class App():
    
    def __init__(self):
        # chemin d'accès au data
        self.chemin_data = "data"
        
        # définir les couleurs et les polices d'écriture
        self.couleur = {"nero": "#252627",
                        "vert": "#34b297", "blanc": "#FFFFFF"}
        self.font = "ExtraCondensed 15"

        # definit la fenêtre
        self.app = tk.Tk()
        self.app.title("CriptApp")
        self.app.config(bg=self.couleur['blanc'])
        self.app.geometry("400x600")
        self.app.iconbitmap("data\\logo.ico")

        self.page = "ACCUEIL"
        self.Etat_navbar = False

        # charge les images
        self.navIcon = PhotoImage(
            file="data\\menu.png")
        self.closeIcon = PhotoImage(
            file="data\\croix.png")
        self.flechesIcon = PhotoImage(file="data\\traduire.png")
        
        # initialisation var
        self.keypass = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRST"
        self.key = ""
        
        
        # ----------------------------
        #  initialisation des widgets
        # ----------------------------
        
        # bar du haut
        self.Frame_bar_menu = tk.Frame(self.app, bg=self.couleur['vert'])
        self.Texte_nom_page = tk.Label(self.Frame_bar_menu, text=self.page, font=self.font,
                                     bg=self.couleur['vert'], fg=self.couleur['blanc'], height=2, padx=20)
        self.Boutton_ouvrir_navbar = tk.Button(self.Frame_bar_menu, image=self.navIcon,
                                   bg=self.couleur['vert'], bd=0, padx=20, activebackground=self.couleur['vert'], command=self.switchNavbar)
        

        # ----- dans les pages -----
        
        # Page "Accueil" 
        self.Texte_page_accueil = tk.Label(self.app, text="\nBienvenue !\n\nVous pouvez cripter des textes dans \ncette aplication à partir de clés.\nCes clés doivent avoir les caractétistique \nsuivantes :\n\n- Contenir 46 caractères                  \n- Ne pas contenir 2 fois le même      \ncaractère                                   \n- Les caractères doivent être           \ncompris entre a-z et A-T              ",
                                       font=self.font, bg=self.couleur['blanc'], fg=self.couleur['nero'])
        
        # Page "Gérer les clés"
        self.Frame_page_gerer = tk.Frame(self.app, bg=self.couleur['blanc'], pady=10)
        self.Boutton_generer = tk.Button(self.Frame_page_gerer, text="Générer", command=self.generer_cle, bd=1, font=self.font, bg=self.couleur['vert'], fg=self.couleur['blanc'], activebackground=self.couleur['vert'])
        self.Boutton_ajouter = tk.Button(self.Frame_page_gerer, text="Ajouter", command=self.ajouter_cle, bd=1, font=self.font, bg=self.couleur['vert'], fg=self.couleur['blanc'], activebackground=self.couleur['vert'])
        self.Frame_entry_1 = tk.Frame(self.app, bg=self.couleur['blanc'], pady=10)
        self.Entry_page_gerer = tk.Entry(self.Frame_entry_1, width=99999)
        self.Texte_test_cle_2 = tk.Label(self.Frame_page_gerer, bg=self.couleur['blanc'])
                
        # Page "Utiliser une clé"
        self.Frame_texte_choisir_cle = tk.Frame(self.app, bg=self.couleur['blanc'])
        self.Texte_cle = tk.Label(self.Frame_texte_choisir_cle, text="Choisir une clé :", font=self.font, pady=8, bg=self.couleur['blanc'], fg=self.couleur['nero'])
        self.Texte_test_cle = tk.Label(self.Frame_texte_choisir_cle, font="ExtraCondensed 10", bg=self.couleur['blanc'], fg=self.couleur['nero'])
        self.Frame_page_utiliser = tk.Frame(self.app, bg=self.couleur["blanc"])
        self.Frame_entry_2 = tk.Frame(self.Frame_page_utiliser, bg=self.couleur["blanc"])
        self.Entry_page_utiliser = tk.Entry(self.Frame_entry_2, font="ExtraCondensed 9", width=500, bg=self.couleur['blanc'], fg=self.couleur['nero'])
        self.Boutton_utiliser_cle = tk.Button(self.Frame_page_utiliser, pady=2, padx=5, command=self.tester_cle_et_utiliser, text="Ok", bd=1, font="ExtraCondensed 6", bg=self.couleur['vert'], fg=self.couleur['blanc'], activebackground=self.couleur['vert'])
        
        
        # Page "Traduire un texte"
        self.Frame_page_traduire = tk.Frame(self.app, bg=self.couleur['blanc'])
        self.Texte_nom_cle = tk.Label(self.Frame_page_traduire, font="ExtraCondensed 8", bg=self.couleur['blanc'], fg=self.couleur['vert'])
        self.Boutton_page_traduire = tk.Button(self.Frame_page_traduire, command=self.traduire, image=self.flechesIcon, bd=0, font="ExtraCondensed 10", bg=self.couleur['blanc'], activebackground=self.couleur['blanc'])
        self.Frame_page_traduire_2 = tk.Frame(self.app, bg='gray50', bd=1)
        self.Texte_a_traduire = tk.Text(self.Frame_page_traduire_2, bd=0, font="ExtraCondensed 10")
        
        # ----- fin des pages -----
        
        
        # bar côté gauche
        self.Frame_navbar = tk.Frame(self.app, bg="gray30", width=250, height=50000)
        # - options dans la bar côté gauche
        self.Boutton_accueil =  tk.Button(self.Frame_navbar, text="ACCUEIL", font=self.font, bg="gray30", bd=0,
                                    fg=self.couleur['blanc'], activebackground="gray30", command=lambda: self.changer_page("ACCUEIL"))
        self.Boutton_gerer = tk.Button(self.Frame_navbar, text="GÉRER LES CLÉS", font=self.font, bg="gray30", bd=0,
                                     fg=self.couleur['blanc'], activebackground="gray30", command=lambda: self.changer_page("GÉRER LES CLÉS"))
        self.Boutton_utiliser = tk.Button(self.Frame_navbar, text="UTILISER UNE CLÉ", font=self.font, bg="gray30", bd=0,
                                   fg=self.couleur['blanc'], activebackground="gray30", command=lambda: self.changer_page("UTILISER UNE CLÉ"))
        self.Boutton_traduire = tk.Button(self.Frame_navbar, text="TRADUIRE UN TEXTE", font=self.font, bg="gray30", bd=0,
                                    fg=self.couleur['blanc'], activebackground="gray30", command=lambda: self.changer_page("TRADUIRE UN TEXTE"))
        # - bandeau vert au dessus de la navbar pour garder le bandeau du menu
        self.bandeau_vert_navbar = tk.Label(self.Frame_navbar, font=self.font, bg=self.couleur['vert'], fg="black", width=300, height=2, padx=20)
        # - boutton fermer bar
        self.Boutton_fermer_navbar = tk.Button(self.Frame_navbar, image=self.closeIcon,
                                  bg=self.couleur['vert'], bd=0, padx=20, activebackground=self.couleur['vert'], command=self.switchNavbar)

        
    def traduire(self):
        if self.key == "":
            return
        
        index = self.Texte_a_traduire.index('insert')
        
        # créer la table de comparaison 
        liste1 = ("w", "J", "}", 'x', '&', 'd', '"', 'r', ';', 'v', 't', '~', 'b', '#', "'", 'n', "u", 'j', '(', 'k', '*', 'l',
          'e', '$', 'q', '_', 'c', 'm', 'h', 'Q', 'i', ')', 'o', '=', '1', '!', '2', 'y', '3', 'g', '4', 'Z', '5', 'U', '6', 'R')
        liste2 = ('7', 'Y', '8', 'I', '9', 'O', '0', 'P', 'T', 'E', 'A', 'p', 'S', 'D', 'f', 'G', 'H', ']', 'K', 'L', 'M', 'W',
          'X', 'C', 'a', 'B', 'N', '?', '.', '/', '%', '<', '>', '{', '[', '|', '`', '\\', '^', 'F', 's', '@', ' ', '-', '+', 'V')
        
        comparaison_table = []
        for caractere_in_key in self.key:
            indexliste1 = self.key.index(caractere_in_key)
            indexliste2 = self.keypass.index(caractere_in_key)

            comparaison_table.append((liste1[indexliste1], liste2[indexliste2]))
        
        text = self.Texte_a_traduire.get(1.0, "end")
        
        # transforme grâce à la table de comparaison le "text" en "text2"
        text2 = ''
        for caractere_in_texte in text:

            t = 0

            for y in comparaison_table:

                if caractere_in_texte == y[0]:

                    text2 = text2 + y[1]
                    t = 1

                if caractere_in_texte == y[1]:

                    text2 = text2 + y[0]
                    t = 1

            if t == 0:

                text2 = text2 + caractere_in_texte
        
        self.Texte_a_traduire.delete(1.0, "end")
        self.Texte_a_traduire.insert(1.0, text2)
        self.Texte_a_traduire.focus_set()
        self.Texte_a_traduire.mark_set(tk.INSERT, index)

    
    def generer_cle(self):
        key = ""
        keypass = []
        
        for x in self.keypass:
            keypass.append(x)
        
        for i in range(46):
            index = randrange(0, len(keypass))
            key = key + keypass[index]
            del keypass[index]
                
        self.Entry_page_gerer.delete(0, "end")
        self.Entry_page_gerer.insert(0, key)
        
    
        
    def page_gerer_tester_cle(self):
        key = self.Entry_page_gerer.get()
        
        if len(key) != 46:
            self.Texte_test_cle_2.config(text="La clé n'est pas valide :\nIl faut 46 caractères")
            return False

        test = []
        for z in key:
            if z in test:
                self.Texte_test_cle_2.config(text="La clée n'est pas valide :\nUne fois chaque caractère")
                return False
            if z not in self.keypass:
                self.Texte_test_cle_2.config(text="La clé n'est pas valide :\nCaractères requis entre a-z et A-T")
                return False
            test.append(z)
        self.Texte_test_cle_2.config(text="")
        return True


    def ajouter_cle(self):
        if not self.page_gerer_tester_cle():
            return
        key = self.Entry_page_gerer.get()
        file = open("data\\data")
        data = file.read()
        file.close()
        data = data + "\n" + key
        file = open("data\\data","w")
        file.write(data)
        file.close()
        
        

        

    def tester_cle_et_utiliser(self):
        key = self.Entry_page_utiliser.get()
        
        if len(key) != 46:
            self.Texte_test_cle.config(text="La clé n'est pas valide :\nIl faut 46 caractères")
            return

        test = []
        for z in key:
            if z in test:
                self.Texte_test_cle.config(text="La clée n'est pas valide :\nUne fois chaque caractère")
                return
            if z not in self.keypass:
                self.Texte_test_cle.config(text="La clé n'est pas valide :\nCaractères requis entre a-z et A-T")
                return
            test.append(z)
        self.Texte_test_cle.config(text="")
        self.key = key
        self.changer_page("TRADUIRE UN TEXTE")


    def switchNavbar(self):
        # fonction switch bar côté gauche
        if self.Etat_navbar:
            # créer une fermeture animée de la bar côté gauche
            for x in range(64):
                self.Frame_navbar.place(x=-x*4, y=0)
                self.Frame_bar_menu.update()
            self.Etat_navbar = False
        else:
            # créer une ouverture animée de la bar côté gauche
            for x in range(-64, 0):
                self.Frame_navbar.place(x=x*4, y=0)
                self.Frame_bar_menu.update()
            self.Etat_navbar = True


    def changer_page(self, new_page):
        self.page = new_page
        
        # change le texte en haut à droite
        self.Texte_nom_page.config(text = self.page)
        
        # delete les Entry
        self.Entry_page_utiliser.delete(0, "end")
        
        if self.Etat_navbar:
            self.switchNavbar()
        
        self.charger_fenetre()


    def charger_bar_menu(self):
        # créer la bar du haut
        self.Frame_bar_menu.pack(side="top", fill=tk.X)
        self.Texte_nom_page.pack(side="right")
        self.Boutton_ouvrir_navbar.place(x=7.5, y=7.5)


    def charger_bar_gauche(self):
        # paramètre bar côté gauche
        self.Frame_navbar.place(x=-250, y=0)
        self.bandeau_vert_navbar.place(x=0, y=0)

        # Positionnement des options dans la bar côté gauche
        self.Boutton_accueil.place(x=20, y=80)
        self.Boutton_gerer.place(x=20, y=120)
        self.Boutton_utiliser.place(x=20, y=160)
        self.Boutton_traduire.place(x=20, y=200)

        # Parametrage bouton fermeture de la bar côté gauche
        self.Boutton_fermer_navbar.place(x=210, y=7.5)


    def liste_cles_in_data(self):
        file = open("data\\data")
        data_brut = file.read()
        data = data_brut.split("\n")
        data.pop(-1)
        mes_objets = []
        for text in data:
            mes_objets.append(tk.Label(self.app, bd=2, text=text).pack())
        
        

    
    def charger_fenetre(self):
        # désaffiche toutes les frames
        self.Texte_page_accueil.pack_forget()
        self.Frame_texte_choisir_cle.pack_forget()
        self.Frame_page_traduire.pack_forget()
        self.Frame_page_traduire_2.pack_forget()
        self.Frame_page_utiliser.pack_forget()
        self.Frame_page_gerer.pack_forget()
        self.Frame_entry_1.pack_forget()
        
        
        if self.page == "ACCUEIL":
            self.Texte_page_accueil.pack(side="top") # il faut pack_forget

        if self.page == "GÉRER LES CLÉS":
            self.Frame_page_gerer.pack(side="top", fill=tk.X) # il faut pack_forget
            self.Boutton_ajouter.pack(side='left', padx=10) # in Frame
            self.Boutton_generer.pack(side='left') # in Frame
            self.Frame_entry_1.pack(side="top", fill=tk.X) # il faut pack_forget
            self.Entry_page_gerer.pack(padx=10) # in frame
            self.Texte_test_cle_2.pack(side='right') # in Frame
            self.liste_cles_in_data()

        if self.page == "UTILISER UNE CLÉ":
            self.Frame_texte_choisir_cle.pack(side="top", fill=tk.X, padx=10, pady=10) # il faut pack_forget
            self.Texte_test_cle.pack(side="right") # in Frame
            self.Texte_cle.pack(side="left") # in Frame
            self.Frame_page_utiliser.pack(anchor='center', padx=10) # il faut pack_forget
            self.Boutton_utiliser_cle.pack(side="left", expand='YES') # in Frame
            self.Frame_entry_2.pack(side="left", expand="YES", padx=10) # in Frame
            self.Entry_page_utiliser.pack() # in Frame

        if self.page == "TRADUIRE UN TEXTE":
            self.Frame_page_traduire.pack(side="top", fill=tk.X, padx=10, pady=10) # il faut pack_forget
            self.Texte_nom_cle.pack(side="left") # in Frame
            self.Texte_nom_cle.config(text="Clé utilisé : "+self.key) # in Frame
            self.Texte_a_traduire.pack(expand="YES", fill=tk.BOTH) # in Frame
            self.Frame_page_traduire_2.pack(anchor="center", expand="YES", padx=10, pady=10, fill=tk.BOTH) # il faut pack_forget
            self.Boutton_page_traduire.pack(side="right") # in Frame
        
        self.charger_bar_gauche()


    def main(self):
        # placer bar menu
        self.charger_bar_menu()
        
        # placer la page "Accueil"
        self.charger_fenetre()
        
        # fait tourner l'App
        self.app.mainloop()


App().main()


'''
# ---------- à modifier ---------- #
file_acces = 'C:\\Users\\matth\\Documents\\Python\\Cript_V1\\pr2.txt'
key = 'dRezPbcpMgtvCGiaJumIBlKyLNsrTxQEDwFfhHOnAoqjkS'
# -------------------------------- #
# key par défaut = key pass


# set Les listes
keypass = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRST"
liste1 = ("w", "J", "}", 'x', '&', 'd', '"', 'r', ';', 'v', 't', '~', 'b', '#', "'", 'n', "u", 'j', '(', 'k', '*', 'l',
          'e', '$', 'q', '_', 'c', 'm', 'h', 'Q', 'i', ')', 'o', '=', '1', '!', '2', 'y', '3', 'g', '4', 'Z', '5', 'U', '6', 'R')
liste2 = ('7', 'Y', '8', 'I', '9', 'O', '0', 'P', 'T', 'E', 'A', 'p', 'S', 'D', 'f', 'G', 'H', ']', 'K', 'L', 'M', 'W',
          'X', 'C', 'a', 'B', 'N', '?', '.', '/', '%', '<', '>', '{', '[', '|', '`', '\\', '^', 'F', 's', '@', ' ', '-', '+', 'V')


# vérifie la clée
if len(key) != 46:
    print("\nLa clé n'est pas valide :\nIl faut 46 caractères")
    exit(1)

test = []
for z in key:
    if z in test:
        print("\nLa clée n'est pas valide :\nVous avez mis deux fois le même caractère")
        exit(1)
    if z not in keypass:
        print("\nLa clé n'est pas valide :\nVous ne pouvez mettre que ces caractères :", keypass)
        exit(1)
    test.append(z)


# créé la table de comparaison
comparaison_table = []
for caractere_in_key in key:
    indexliste1 = key.index(caractere_in_key)
    indexliste2 = keypass.index(caractere_in_key)

    comparaison_table.append((liste1[indexliste1], liste2[indexliste2]))


# récupère le texte se trouvant dans le fichier pour le mettre dans "text"
try:
    file = open(file_acces, "r")
except:
    print("\nL'accès au fichier n'est pas valide")
    exit(2)

text = file.read()
file.close()


# transforme grâce à la table de comparaison le "text" en "text2"
text2 = ''
for caractere_in_texte in text:

    t = 0

    for y in comparaison_table:

        if caractere_in_texte == y[0]:

            text2 = text2 + y[1]
            t = 1

        if caractere_in_texte == y[1]:

            text2 = text2 + y[0]
            t = 1

    if t == 0:

        text2 = text2 + caractere_in_texte


# clear le fichier puis ajoute le "text2"
file = open(file_acces, "w")
file.write(text2)
file.close()
'''