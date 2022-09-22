# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 22:55:52 2022

@author: user
"""
#from cl_persona import Persona, Error, NotALetterError, WrongLengthError
from cl_studente import Studente
from cl_docente import Docente
from cl_amministratore import Admin, delAdmin, getAdmin

#scheduled improvements: 
    # exception management sugli user
    # formattazione

def logmenu():
    print("Benvenuto/a/* all'Anagrafe Scuola.")
    while True:
        
        utente = input("Inserisci Nome Utente oppure 'exit' per uscire: \n")
        if utente.strip().lower() == 'exit':
            print("Grazie per aver usato l'Anagrafe Studenti")
            exit()
        
        elif getAdmin(utente):
        #for later: catturare attribute error e dare 3 tentativi per inserire utente corretto
            oAdmin = getAdmin(utente) #oAdmin = oggetto admin con username utente
            adminpw = oAdmin.password
            attempts = 0
            while attempts < 3:
                passw = input("Inserisci la Password: \n")
                if passw == adminpw:
                    print(f"Benvenuto {utente}!")
                    attempts = 0
                    mainmenu(oAdmin)
                else:
                    attempts += 1
                    print(f"Tentativo:{attempts} - Password Errata, riprova.\n")
            print("Hai esaurito i tentativi!")
            print("Arrivederci!")
            exit()
        
        else:
            print("Input e/o utenti non riconosciuti, riprova!")
            logmenu()
        

def mainmenu(doc: Admin):
    while True:
        choice = input("""
Digita 'Admin' per il riepilogo dei tuoi dati
Digita 'Cancel' per cancellare il tuo account
Digita 'Nuovo Studente' per creare un nuovo studente.
Digita 'Nuovo Docente' per creare un nuovo docente.
Premi 'S' per accedere al menu gestione studente.
Premi 'D' per accedere al menu gestione docente.
Premi 'O' [lettera] per fare il logout.
Input: """)
        
        if choice.strip().lower() == "admin":
            print(doc.datiPersona())
            mainmenu(doc)
        
        #da testare nel main
        if choice.strip().lower() == "cancel":
            print("Stai cancellando il tuo account.")
            delchoice = input("Sei davvero sicuro? [y/N]: ")
            if delchoice[0].lower().strip() == "n":
                print("Processo cancellazione interrotto.")
                mainmenu(doc)
            elif delchoice[0].lower().strip() == "y":
                print("Cancellazione profilo Admin in corso...")
                delAdmin(doc.utente)
                logmenu()
        
        if choice.strip().lower() == "nuovo studente":
            cognome = input("Cognome nuovo studente: ")
            nome = input("Nome nuovo studente: ")
            while True:
                codicefiscale = input("Codice fiscale - 16 caratteri: ")
                if len(codicefiscale) == 16:
                    break
            classe = input("Classe - 1 numero e 1 lettera, e.g. 2A: ")
            doc.creaStudente(cognome, nome, codicefiscale, classe)
            menuchoice = input("Vuoi continuare nel menu gestione studente? [Y/n]: ")
            if menuchoice[0].lower() == 'y':
                oStud = doc.getStudente(codicefiscale)
                studente = oStud[codicefiscale]
                menustudente(doc, studente)
            else:
                mainmenu(doc)
        
        if choice.strip().lower() == "nuovo docente":
            cognome = input("Cognome nuovo docente: ")
            nome = input("Nome nuovo docente: ")
            while True:
                codicefiscale = input("Codice fiscale - 16 caratteri: ")
                if len(codicefiscale) == 16:
                    break
            insegnamento = input("Insegnamento: ")
            doc.creaDocente(cognome, nome, codicefiscale, insegnamento)
            menuchoice = input("Vuoi continuare nel menu gestione docente? [Y/n]: ")
            if menuchoice[0].lower() == 'y':
                oDocente = doc.getDocente(codicefiscale)
                docente = oDocente[codicefiscale]
                menudocente(doc, docente)
            else:
                mainmenu(doc)
            
        if choice[0].lower() == "s":
            print("Hai selezionato il menu studente.")
            codf = input("Inserisci il codice fiscale dello studente desiderato: ")
            studentdict = doc.getStudente(codf)
            studente = studentdict[codf] #ritorna oggetto studente
            menustudente(doc, studente)
        
        elif choice[0].lower() == "d":
            print("Hai selezionato il menu docente.")
            codf = input("Inserisci il codice fiscale del docente desiderato: ")
            teacherdict = doc.getDocente(codf)
            docente = teacherdict[codf]
            menudocente(doc, docente)
        
        elif choice[0].lower() == "o":
            print("Sto effettuando il logout...")
            logmenu()
        
        else:
            print("L'input non corrisponde a nessun comando")
            mainmenu(doc)


def menustudente(admin: Admin, studente: Studente):
    #print("Sei dentro il menu studenti")
    while True:
        choice = input("""
Digita 'Dati' per anagrafica studente.
Digita 'Pagella' per stampare la pagella dello studente.
Digita 'Modifica' per modificare i dati dello studente.
Digita 'Assegna Voto' per assegnare un voto allo studente.
Digita 'Back' per tornare al menu principale.
""")    
        if choice.strip().lower() == 'dati':
            print("==DATI STUDENTE ==")
            print(admin.getDatiStudente(studente.codicefiscale))
            menustudente(admin, studente)
        
        elif choice.strip().lower() == 'pagella':
            print("==STAMPA PAGELLA==")
            print(admin.getPagellaStudente(studente.codicefiscale))
            menustudente(admin, studente)
        
        elif choice.strip().lower() == 'modifica':
            risp = input("Vuoi modificare il cognome? [Y/n]: ")
            if risp[0].lower() == "y":
                cognome = input("Digita il nuovo cognome: ")
            else:
                cognome = studente.cognome
            
            risp =input("Vuoi modicare il nome? [Y/n]: ")
            if risp[0].lower() == "y":
                nome = input("Digita il nuovo nome: ")
            else:
                nome = studente.nome 
            
            risp =input("Vuoi modicare la classe? [Y/n]: ")
            if risp[0].lower() == "y":
                classe = input("Digita la nuova classe (e.g. '2A'): ")
            else:
                classe = studente.classe
            
            risp =input("Vuoi aggiornare il codice fiscale? [Y/n]: ")
            if risp[0].lower() == "y":
                while True:
                    nuovocf = input("Digita il nuovo codice fiscale: ")
                    if len(nuovocf) == 16:
                        break
            else:
                nuovocf = ""
            
            codf = studente.codicefiscale
            admin.setDatiStudente(cognome, nome, classe, nuovocf, codf)
            menustudente(admin, studente)
            
        
        elif choice.strip().lower() == 'assegna voto':
            materia = input("Digita la materia a cui assegnare il voto: ")
            voto = input("Digita che voto vuoi assegnare da 1 a : ")
            admin.setVotoStudente(studente.codicefiscale, materia, voto)
            menustudente(admin, studente)
        
        elif choice.strip().lower() == 'back':
            print("Torno al menu principale...")
            mainmenu(admin)
        
        else:
            print("L'input non corrisponde a nessun comando")
            menustudente(admin, studente)

def menudocente(admin: Admin, docente: Docente):
    #print("Sei dentro il menu docenti")
    while True:
        choice = input("""
Digita 'Dati' per anagrafica docente.
Digita 'Scheda' per stampare la Scheda Docente.
Digita 'Modifica' per modificare i dati del Docente.
Digita 'Classi' per modifica l'elenco classi del Docente.
Digita 'Back' per tornare al menu principale.
""")
        
        if choice.strip().lower() == 'dati':
            print("==DATI DOCENTE ==")
            print(admin.getDatiDocente(docente.codicefiscale))
            menudocente(admin, docente)
        
        elif choice.strip().lower() == 'back':
            print("Torno al menu principale...")
            mainmenu(admin)
        
        elif choice.strip().lower() == 'scheda':
            print("==STAMPA SCHEDA==")
            print(admin.getSchedaDocente(docente.codicefiscale))
            menudocente(admin, docente)
        
        elif choice.strip().lower() == 'modifica':
            risp = input("Vuoi modificare il cognome? [Y/n]: ")
            if risp[0].lower() == "y":
                cognome = input("Digita il nuovo cognome: ")
            else:
                cognome = docente.cognome
            
            risp =input("Vuoi modicare il nome? [Y/n]: ")
            if risp[0].lower() == "y":
                nome = input("Digita il nuovo nome: ")
            else:
                nome = docente.nome 
            
            risp =input("Vuoi modicare l'insegnamento'? [Y/n]: ")
            if risp[0].lower() == "y":
                insegnamento = input("Digita il nuovo insegnamento (e.g. 'Storia'): ")
            else:
                insegnamento = docente.insegnamento
            
            risp =input("Vuoi aggiornare il codice fiscale? [Y/n]: ")
            if risp[0].lower() == "y":
                while True:
                    nuovocf = input("Digita il nuovo codice fiscale: ")
                    if len(nuovocf) == 16:
                        break
            else:
                nuovocf = ""
            
            codf = docente.codicefiscale
            admin.setDatiDocente(cognome, nome, insegnamento, nuovocf, codf)
            menudocente(admin, docente)
        
        elif choice.strip().lower() == 'classi':
            risp = input("Vuoi aggiungere 1 classe o resettare? [Ag/res]: ")
            if risp[:2].lower() == "ag":
                while True:
                    classe = input("Digita la classe - e.g. 3C: ")
                    admin.setClassiDocente(docente.codicefiscale, classe)
                    risp = input("Vuoi aggiungere un'altra classe? [Y/n]: ")
                    if risp[0].lower() == "y":
                        continue
                    else:
                        break
                        menudocente(admin, docente)
            elif risp[:3].lower() == "res":
                classi = []
                print("Resetto la lista classi...")
                admin.setClassiDocente(docente.codicefiscale, classi)
                print("Classi resettate")
                menudocente(admin, docente)
            else: 
                print("Input non riconosciuto. Ritoro al menu...")
                menudocente(admin, docente)
        
        else:
            print("L'input non corrisponde a nessun comando")
            menudocente(admin, docente)

