# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 22:52:55 2022

@author: user
"""

from cl_persona import Persona, Error, NotALetterError, WrongLengthError, GenericError
import os

      
class Docente(Persona):
    def __init__(self, cognome: str, nome: str, codicefiscale: str, insegnamento: str):
        Persona. __init__(self, cognome, nome, codicefiscale)
        self.insegnamento = insegnamento
        self.classi = [] #lista in quanto ci si aspetta non sia troppo lunga
        #e ogni classe è un singolo parametro. Un dizionario sarebbe stato meglio
        #se avessimo voluto aggiungere come valori della key "classe" tutti gli studenti
        #che la frequentano, ma a quel punto converrebbe creare una class "Classe"
        #e rendere ogni classe un'istanza/oggetto.
        
    #Proprietà:
    @property
    def insegnamento(self):
        return self.__insegnamento
    
    @insegnamento.setter
    def insegnamento(self, insegnamento: str):
        try:
            if not insegnamento.isalpha():
                raise ValueError("Il nome insegnamento può contenere solo lettere: ")
            if not 3 <= len(insegnamento) <=25:
                raise WrongLengthError(" il nome insegnamento deve essere compreso fra 3 e 25 caratteri")
        except ValueError as ve:
            print(str(ve) + "elimino caratteri superflui")
            insegnamento = "".join([char for char in insegnamento if char.isalpha()])
            self.__insegnamento = insegnamento
        except WrongLengthError as wle:
            print("Errore: " + str(wle))
            self.__insegnamento = ""
        else:
            insegnamento = str(insegnamento.title())
            self.__insegnamento = insegnamento
    
    @insegnamento.deleter
    def insegnamento(self):
        print("Sto cancellando l'insegnamento")
        del self.__insegnamento
    
    @property
    def classi(self):
        return self.__classi
    
    @classi.setter
    #da implementare: check che i singoli elementi di classi rispettino i 
    #parametri di setClasse
    def classi (self, classi: list):
        try:
            if type(classi) is not list:
                raise TypeError(f"{classi} deve essere una lista")
        except TypeError as te:
            print("Errore: " + str(te))
            pass
        else:
            self.__classi = classi
    
    @classi.deleter
    def classi(self):
        self.__classi = []
        
    
    # Metodi:
    
    def datiPersona(self):
        #usa polimorfismo parent
        str_dati = super().datiPersona()
        str_dati += f"\nInsegnamenti: {self.insegnamento}"
        return str_dati
     
    def setClasse(self, classe: str):
        if not isinstance(classe, str):
            classe = str(classe)
        try: 
            if len(classe) != 2:
                raise WrongLengthError("la classe deve essere composta da due caratteri")
            if classe in self.classi:
                raise GenericError("la classe è già presente nell'elenco")
            if not classe[0].isdigit():
                raise ValueError("il primo carattere deve essere un numero")
            if not classe[1].isalpha():
                raise NotALetterError("il secondo carattere deve essere una lettera")
        except (WrongLengthError) as wle:
            print("Errore: "+ str(wle))
            pass
        except (GenericError) as ge:
            print("Errore: "+ str(ge))
            pass
        except (ValueError) as ve:
            print("Errore: "+ str(ve))
            pass
        except (NotALetterError) as nle:
            print("Errore: "+ str(nle))
            pass
        else:
            classe = classe.title()
            self.classi.append(classe)
    
    def removeClasse(self, classe: str):
        if not isinstance(classe, str):
            classe = str(classe)
        try:
            if classe not in self.classi:
                raise ValueError("la classe non è presente nell'elenco")
        except ValueError as ve:
            print("Errore: "+str(ve))
        else:
            self.classi.remove(classe)
    
    def stampaScheda(self):
        testo = f"Docente: {self.cognome} {self.nome}\n"
        testo += f"Insegnamento: {self.insegnamento}\n\n"
        testo += "CLASSI\n"
        for classe in self.classi:
            testo += "\n" + classe
        
        save_path = ".\\SchedeDocenti"
        file_name = f"SchedaDocente_{self.codicefiscale}.txt"
        completename = os.path.join(save_path, file_name)
        
        with open(completename, "w") as fpag:
            fpag.write(testo)

        return testo #permette la visualizzazione e la associa al salvataggio delle nuove modifiche
