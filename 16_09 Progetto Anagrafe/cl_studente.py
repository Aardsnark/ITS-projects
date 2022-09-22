# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 22:52:10 2022

@author: user
"""

from cl_persona import Persona, Error, NotALetterError, WrongLengthError, GenericError
#import numbers
import os

class Studente(Persona):
    def __init__(self, cognome: str, nome: str, codicefiscale: str, classe: str):
        Persona. __init__(self, cognome, nome, codicefiscale)
        self.classe = classe
        self.voti = {"Letteratura" : "1", "Storia": "", "Grammatica": "", "Filosofia": "", "Matematica": "", "Fisica": "", "Chimica": "", "Biologia": "" }
    # Proprietà:
    @property
    def classe(self):
        return self.__classe
    
    @classe.setter
    def classe(self, classe):
        try:
            if not isinstance(classe, str):
                raise TypeError("deve essere una stringa")
            if len(classe) != 2:
                raise WrongLengthError("la classe deve essere composta da due caratteri.")
            if not classe[0].isdigit():
                raise ValueError("il primo carattere deve essere un numero.")
            if not classe[1].isalpha():
                raise NotALetterError("il secondo carattere deve essere una lettera.")
        except (WrongLengthError) as wle:
            print("Parametro 'classe' creato vuoto: "+ str(wle) +"\nRicordati di assegnarlo.")
            self.__classe = ""
        except (ValueError) as ve:
            print("Parametro 'classe' creato vuoto: "+ str(ve) +"\nRicordati di assegnarlo.")
            self.__classe = ""
        except (NotALetterError) as nle:
            print("Parametro 'classe' creato vuto: "+ str(nle) +"\nRicordati di assegnarlo.")
            self.__classe = ""
        except (TypeError) as te:
            print("Parametro 'classe' creato: "+ str(te))
            self.__classe = ""
        else:
            classe[1].upper()
            self.__classe = classe
    
    @classe.deleter
    def classe(self):
        del self.__classe
    
    @property
    def voti(self):
        return self.__voti
    
    @voti.setter
    def voti(self, voti: dict):
        try:
            if type(voti) is not dict:
                raise TypeError(f"{voti} deve essere un dict")
        except (TypeError) as te:
            print("Errore: " + str(te))
            pass #non empty dict, altrimenti basterebbe un qualunque set per 
            #azzerare il dict standard
        else:
            self.__voti = voti
    
    @voti.deleter
    def voti(self):
        self.__voti = {}
        
    def getVoto(self, materia: str):
        try:
            if materia not in self.__voti.keys():
                raise AttributeError(f"{materia} non è una materia insegnata")
            if self.__voti[materia] == "":
                print(f"{materia} non ha ancora un voto assegnato")
        except (AttributeError) as ae:
            print("Errore: "+ str(ae))
            pass
        else:
            return self.__voti.get(f"{materia}")
        
    def setVoto(self, materia: str, voto: str):
        if not isinstance(voto, str):
            voto = str(voto)
        try: 
            if materia not in self.__voti.keys():
                raise AttributeError(f"{materia} non è una materia insegnata")
            if not voto.isdigit():
                raise TypeError(f"{voto} non è un numero")
            if int(voto) < 0 or int(voto) > 10:
                raise ValueError("il voto deve essere compreso fra 0 e 10")
        except (AttributeError) as ae:
            print("Errore: "+ str(ae))
            pass
        except TypeError as ve:
            print("Errore: " + str(ve))
            pass
        except ValueError as ve:
            print("Errore: " +str(ve))
            pass
        else:
            self.__voti[materia] = voto
    
    def delVoto(self, materia: str):
        try:
            if materia not in self.__voti.keys():
                raise AttributeError(f"{materia} non è una materia insegnata")
        except (AttributeError) as ae:
            print("Errore: "+ str(ae))
            pass
        else:
            print(f"Sto eliminando il voto di {materia}")
            self.__voti[materia] = ""
    
    
    
    # Metodi:
        
    def delMateria(self, materia: str):
        try:
            if materia not in self.__voti.keys():
                raise AttributeError(f"{materia} non è una materia insegnata")
        except (AttributeError) as ae:
            print("Errore: "+ str(ae))
            pass
        else:
            del self.voti[materia]
    
    # Permette all'Amministratore di modificare più coerentemente l'elenco degli insegnamenti
    def addMateria(self, materia: str):
        try:
            if not materia.isalpha():
                raise ValueError("il nome materia può contenere solo lettere")
        except ValueError as ve:
            print("Errore: "+str(ve))
            pass
        else:
            materia = str(materia.title())
            self.voti[materia] = ""
 
    # Niente Metodo setMateria perchè andrebbe a creare solo confusione vista l'unicità delle keys dei dizionari
    def stampaPagella(self):
        #genera una stringa con in testa nome e cognome e classe e poi l’elenco delle materie una per riga con i relativi voti e salva il tutto su un file di testo il cui nome sarà
        #Pagella_<codicefiscale>.txt
        testo = f"Studente: {self.cognome} {self.nome}\n"
        testo += f"Classe: {self.classe}\n\n"
        testo += "MATERIA\t\t\t\tVoto\n"
        for key in self.voti.keys():
            testo += "\n" + key + "\t\t\t" + self.voti[key]
        
        save_path = ".\\Pagelle"
        file_name = f"Pagella_{self.codicefiscale}.txt"
        completename = os.path.join(save_path, file_name)
        
        with open(completename, "w") as fpag:
            fpag.write(testo)

        return testo
    
    def datiPersona(self):
        #usa polimorfismo parent
        str_dati = super().datiPersona()
        str_dati += f"\nClasse: {self.classe}"
        return str_dati