# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 22:49:20 2022

@author: user
"""
from cl_persona import Persona, Error, NotALetterError, WrongLengthError, GenericError
from cl_docente import Docente
from cl_studente import Studente
import random
import string #for random password generator
import os
import pickle #per scrivere il dict codicefiscale : oggetto di ogni utente su file

# Metodo per Main
#ottimizzazione: applicare funzione setPath che prende due parametri (save_path e file_name) e 
#ritorna completename (risparmia due linee per classe che usa i picke)

def setPath(save_path_dir, type_file):
    save_path = f".\\Utenti\\{save_path_dir}"
    file_name = f"{type_file}.pickle"
    completename = os.path.join(save_path, file_name)
    return completename

def creaAdmin():
    utente = input("Nome Admin - dai 6 ai 12 caratteri, minimo 1 numero: ").strip()
    password = input("Password - dai 6 ai 12 caratteri, almeno 1 lettera, 1 numero e 1 carattere speciale: ").strip()
    oAdmin = Admin(utente, password)
    completename = setPath("Admin", utente)
    
    if os.path.exists(completename):
        print("Esiste già un Admin con questo username.")
        pass
    
    elif not os.path.exists(completename):
        with open(completename, "wb") as fpag:
            #if os.stat(completename).st_size == 0:
            print("Sto creando un nuovo Admin...")
            testo = {oAdmin.utente: oAdmin}
            pickle.dump(testo, fpag, protocol=pickle.HIGHEST_PROTOCOL)
            print(f"Ho creato l'Admin {oAdmin.utente}")


def delAdmin(utente):
    completename = setPath("Admin", utente)

    if os.path.exists(completename):
        print("Ho cancellato il file dell'Admin")
        os.remove(completename)
    elif not os.path.exists(completename):
        print("L'Admin non esiste")

def getAdmin(utente): #a differenza di getStudente e getDocente, ritorna l'oggetto
#e non il dizionario
    completename = setPath("Admin", utente)
    
    if os.path.exists(completename):
        with open(completename, "rb") as fpag:
            admindict = pickle.load(fpag)
            #print(admindict[utente])
        
        return admindict[utente]
    
    elif not os.path.exists(completename):
        print("L'Admin non esiste")
        pass

def getDatiAdmin(self, utente):
    admindict = self.getAdmin(utente)
    admin = admindict[utente]
    return admin.datiPersona()


#Amministrativo non richiama il costruttore di Persona, gli servono solo le func
class Admin(Persona):
    def __init__(self, utente: str, password: str):
        #property takes care dell'incapsulamento
        self.utente = utente
        self.password = password
    
    @property
    def utente(self):
        return self.__utente
    
    @utente.setter
    def utente(self, utente):
        if not isinstance(utente, str):
            utente = str(utente)
        try:
            if utente.isalpha():
                raise ValueError("il nome utente deve contenere almeno un numero")
            if not 6 <= len(utente) <=12:
                raise WrongLengthError("il nome utente deve essere compreso fra 6 e 12 caratteri")
        except ValueError as ve:
            print("Errore: " +str(ve))
            print("Aggiungo numeri al nome utente...")
            self.__utente = utente + str(random.randint(10, 100))
            print("Nome utente: "+ self.utente)
        except WrongLengthError as wle:
            print("Errore: " +str(wle))
        else:
            self.__utente = utente
    
    @utente.deleter
    def utente(self):
        print("Sto cancellando l'Utente...")
        del self.__utente
     
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, password):
        if not isinstance(password, str):
            password = str(password)
        try:
            if not 6 <= len(password) <=12:
                raise WrongLengthError("La password deve essere compresa fra 6 e 12 caratteri")
            if password.isdecimal():
                raise ValueError("la password non può contenere solo numeri")
            if password.isalpha():
                raise ValueError("la password non può contere solo lettere")
            if password.isalnum():
                raise ValueError("la password deve contenere almeno un carattere speciale")
            if " " in password:
                raise ValueError("la password non può contenere spazi")
        except (ValueError, WrongLengthError) as ve:
            print("Errore: "+ str(ve))
            print("\nSto creando una password valida")
            password = self.genValidPassword()
            self.__password = password
            print("Nuova password: "+self.password)
        else:
            self.__password = password
    
    @password.deleter
    def password(self):
        print("Sto cancellando la password...")
        del self.__password
    
    def genValidPassword(self):
        nums = str(random.randrange(10,99, 3) * random.randrange(10,99, 7))
        specialch01 = random.choice(string.punctuation)
        chars = "".join([random.choice(string.ascii_letters) for i in range(4)])
        specialch02 = random.choice(string.punctuation)
        
        validpassw = str(nums + specialch01 + chars + specialch02)
        return validpassw

    # Metodi
        
    def datiPersona(self):
        str_dati = f"Utente: {self.utente}" 
        str_dati += f"\nPassword: {self.password}"
        return str_dati

        # Metodi Studente:
            #crea oggetto studente e lo salva come dict codice fiscale : oggetto in 
            #un file pickle dedicato (provato multipli in uno, oggetti troppo grandi
            #per modulo pickle)
            
    def creaStudente(self, cognome: str, nome: str, codicefiscale: str, classe: str):
        if not isinstance(codicefiscale, str):
            codicefiscale = str(codicefiscale)
        save_path = ".\\Utenti\\Studenti"
        file_name = f"{codicefiscale}.pickle"
        completename = os.path.join(save_path, file_name)
        
        #se file esiste già, in questo modo lo sovrascrive con uno nuovo
        #serve discriminante os.path
        
        if os.path.exists(completename):
            print("Esiste già uno studente con questo CF.")
            pass
        elif not os.path.exists(completename):
            with open(completename, "wb") as fpag:
                #if os.stat(completename).st_size == 0:
                print("Sto creando un nuovo studente...")
                oStud = Studente(cognome, nome, codicefiscale, classe)
                testo = {oStud.codicefiscale: oStud}
                pickle.dump(testo, fpag, protocol=pickle.HIGHEST_PROTOCOL)
                print(f"Ho creato lo studente {codicefiscale}")
    
    def delStudente(self, codicefiscale):
        
        save_path = ".\\Utenti\\Studenti"
        file_name = f"{codicefiscale}.pickle"
        completename = os.path.join(save_path, file_name)

        if os.path.exists(completename):
            print("Sto cancellando il file dello studente")
            os.remove(completename)
        elif not os.path.exists(completename):
            print("Lo studente non esiste")
    
    #funzione per vedere gli studenti scritti nel file & i codici fiscali per accedervi
    def getStudente(self, codicefiscale: str):
        
        save_path = ".\\Utenti\\Studenti"
        file_name = f"{codicefiscale}.pickle"
        completename = os.path.join(save_path, file_name)
        if os.path.exists(completename):
            with open(completename, "rb") as fpag:
                studentdict = pickle.load(fpag)
    
            return studentdict
        elif not os.path.exists(completename):
            print("Lo studente non esiste")
            pass
    
    #assegnare voti - tramite classe studente
    def setVotoStudente(self, codicefiscale: str, materia: str, voto: str):
        completename = setPath("Studenti", codicefiscale)
        if not isinstance(codicefiscale, str):
            codicefiscale = str(codicefiscale)
        studentdict = self.getStudente(codicefiscale)
        
        if materia in studentdict[codicefiscale].voti.keys():
            print(f"Assegno {voto} a {materia}...")
            with open(completename, "wb") as fpag:
                #aggiorno il voto con una funzione senza valore di return
                studentdict[codicefiscale].setVoto(materia, voto)
                #dumpo il studentdict aggiornato nel pickle file dello studente
                pickle.dump(studentdict, fpag, protocol=pickle.HIGHEST_PROTOCOL)
                print("Ho assegnato il voto")
            return
        else:
            print("La materia non è in elenco")
            materia = input("Digita la materia a cui assegnare il voto: ")
            self.setVotoStudente(codicefiscale, materia, voto)
        
    #visualizzare i dati - tramite classe studente
    def getVotiStudente(self, codicefiscale):
        studentdict = self.getStudente(codicefiscale)
        
        return studentdict[codicefiscale].voti
    
    def getDatiStudente(self, codicefiscale):
        studentdict = self.getStudente(codicefiscale)
        student = studentdict[codicefiscale]
        return student.datiPersona()
    
    #modificare i dati - tramite classe studente
    def setDatiStudente(self, cognome, nome, classe, nuovocf, codicefiscale):
        save_path = ".\\Utenti\\Studenti"
        file_name = f"{codicefiscale}.pickle"
        completename = os.path.join(save_path, file_name)
        
        if not isinstance(nuovocf, str):
            nuovocf = str(nuovocf)
        if not isinstance(codicefiscale, str):
            codicefiscale = str(codicefiscale)
        if nuovocf != "":
            self.delStudente(codicefiscale)
            self.creaStudente(cognome, nome, nuovocf, classe)
            print("Nuovo studente - " + self.getDatiStudente(nuovocf))
        elif nuovocf == "":
            studentdict = self.getStudente(codicefiscale)
            with open(completename, "wb") as fpag:
                print("Update dei parametri studente in corso")
                student =studentdict[codicefiscale]
                student.cognome = cognome
                student.nome = nome
                student.classe = classe
                pickle.dump(studentdict, fpag, protocol=pickle.HIGHEST_PROTOCOL)
                print("Update dei parametri studente completato")

    
    #visualizzare pagella -tramite classe studente
    def getPagellaStudente(self, codicefiscale):
        studentdict = self.getStudente(codicefiscale)
        student = studentdict[codicefiscale]
        return student.stampaPagella()
        
        # Metodi Docente:
    
    def creaDocente(self, cognome: str, nome: str, codicefiscale:str, insegnamento: str):

        #se file esiste già, in questo modo lo sovrascrive con uno nuovo
        #serve discriminante os.path
        if not isinstance(codicefiscale, str):
            codicefiscale = str(codicefiscale)
        save_path = ".\\Utenti\\Docenti"
        file_name = f"{codicefiscale}.pickle"
        completename = os.path.join(save_path, file_name)
        
        if os.path.exists(completename):
            print("Esiste già un docente con questo CF.")
            pass
        elif not os.path.exists(completename):
            with open(completename, "wb") as fpag:
                #if os.stat(completename).st_size == 0:
                oDoc = Docente(cognome, nome, codicefiscale, insegnamento)
                docdict = {oDoc.codicefiscale: oDoc}
                pickle.dump(docdict, fpag, protocol=pickle.HIGHEST_PROTOCOL)
    
    
    def delDocente(self, codicefiscale):
        save_path = ".\\Utenti\\Docenti"
        file_name = f"{codicefiscale}.pickle"
        completename = os.path.join(save_path, file_name)

        if os.path.exists(completename):
            print("Sto cancellando il file del docente")
            os.remove(completename)
        elif not os.path.exists(completename):
            print("Il docente non esiste")
    
    
    def getDocente(self, codicefiscale: str):
        save_path = ".\\Utenti\\Docenti"
        file_name = f"{codicefiscale}.pickle"
        completename = os.path.join(save_path, file_name)
        if os.path.exists(completename):
            with open(completename, "rb") as fpag:
                teacherdict = pickle.load(fpag)
    
            return teacherdict
        elif not os.path.exists(completename):
            print("Il docente non esiste")
            pass
    
    #assegnare classi/classe -- tramite classe docente
    def setClassiDocente(self, codicefiscale, classi):
        #sovrascrive la lista classi se parametro "classi" è una lista più lunga
        #di un indice, altrimenti append
        save_path = ".\\Utenti\\Docenti"
        file_name = f"{codicefiscale}.pickle"
        completename = os.path.join(save_path, file_name)

        if not isinstance(codicefiscale, str):
            codicefiscale = str(codicefiscale)
        docentedict = self.getDocente(codicefiscale)
        with open(completename, "wb") as fpag:
            print("Update classi docente in corso")
            docente =docentedict[codicefiscale]
            if isinstance(classi, list) or classi == "":
                docente.classi = classi
                pickle.dump(docentedict, fpag, protocol=pickle.HIGHEST_PROTOCOL)
                print("Update lista classi docente completato")
            else:
                classe = classi
                docente.setClasse(classe)
                pickle.dump(docentedict, fpag, protocol=pickle.HIGHEST_PROTOCOL)
                print(f"Aggiunto {classe} a lista classi docente")
    
    #visualizzare i dati -- tramite classe docente
    def getDatiDocente(self, codicefiscale):
        docentedict = self.getDocente(codicefiscale)
        docente = docentedict[codicefiscale]
        return docente.datiPersona()

            
    #modificare i dati -- tramite classe docente
    def setDatiDocente(self, cognome, nome, insegnamento, nuovocf, codicefiscale):
        save_path = ".\\Utenti\\Studenti"
        file_name = f"{codicefiscale}.pickle"
        completename = os.path.join(save_path, file_name)
        
        if not isinstance(nuovocf, str):
            nuovocf = str(nuovocf)
        if not isinstance(codicefiscale, str):
            codicefiscale = str(codicefiscale)
        if nuovocf != "":
            self.delDocente(codicefiscale)
            self.creaDocente(cognome, nome, nuovocf, insegnamento)
            print("Nuovo studente - " + self.getDatiDocente(nuovocf))
        elif nuovocf == "":
            docentedict = self.getDocente(codicefiscale)
            with open(completename, "wb") as fpag:
                print("Update dei parametri docente in corso")
                docente =docentedict[codicefiscale]
                docente.cognome = cognome
                docente.nome = nome
                docente.insegnamento = insegnamento
                pickle.dump(docentedict, fpag, protocol=pickle.HIGHEST_PROTOCOL)
                print("Update dei parametri docente completato")

    #visualizzare scheda docente -- tramite classe docente
    def getSchedaDocente(self, codicefiscale):
        docentedict = self.getDocente(codicefiscale)
        docente = docentedict[codicefiscale]
        return docente.stampaScheda()
            
    