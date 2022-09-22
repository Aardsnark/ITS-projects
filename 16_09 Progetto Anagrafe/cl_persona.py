# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 15:47:48 2022

@author: user
"""
#create test file per acchiappare gli errori

class Error(Exception):
    pass

class NotALetterError(Error):
    pass

class WrongLengthError(Error):
    pass

class GenericError(Error):
    pass


class Persona:
    def __init__(self, cognome: str, nome: str, codicefiscale: str ):
        
    #ogni attributo chiama il proprio property setter, dove l'attributo viene incapsulato.
        self.cognome = cognome 
        self.nome = nome
        self.codicefiscale = codicefiscale
        
      
    @property
    def cognome(self):
        return self.__cognome
    
    @cognome.setter  #se viene catturato un errore, il parametro rimane vuoto per evitare l'Attribute Error
    def cognome(self, cognome):
        try:
            if not isinstance(cognome, str):
                raise TypeError("deve essere una stringa")
            if any((char < "A") or (char > "z") for char in cognome):
                raise(NotALetterError("non può contenere spazi o caratteri speciali - inclusi i numeri"))
            if ((len(cognome) >20) or (len(cognome)<2)):
                raise(WrongLengthError("lungezza deve essere fra 2 e 19 lettere"))
        except (NotALetterError) as notlete:
            print("Non siamo riusciti a creare il cognome: "+ str(notlete))
            self.__cognome = ""
        except (WrongLengthError) as wle:
            print("Non siamo riusciti a creare il cognome: "+ str(wle))
            self.__cognome = ""
        except (TypeError) as te:
            print("Non siamo riusciti a creare il cognome: "+ str(te))
            self.__cognome = ""
        else:
            self.__cognome = cognome.title()
        
    @cognome.deleter #va chiamato con del self.cognome
    def cognome(self): #
        print("Sto cancellando il cognome...")
        del self.__cognome
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        try:
            if not isinstance(nome, str):
                raise TypeError("deve essere una stringa")
            if any((char < "A") or (char > "z") for char in nome):
                raise(NotALetterError("non può contenere spazi o caratteri speciali - inclusi i numeri"))
            if ((len(nome) >20) or (len(nome)<2)):
                raise(WrongLengthError("lungezza deve essere fra 2 e 19 lettere"))
        except (NotALetterError) as notlete:
            print("Non siamo riusciti a creare il nome: "+ str(notlete))
            self.__nome = ""
        except (WrongLengthError) as wle:
            print("Non siamo riusciti a creare il nome: "+ str(wle))
            self.__nome = ""
        except (TypeError) as te:
            print("Non siamo riusciti a creare il nome: "+ str(te))
            self.__nome = ""
        else:
            self.__nome = nome.title()
    
    @nome.deleter
    def nome(self):
        print("Sto cancellando il nome...")
        del self.__nome
    
    @property
    def codicefiscale(self):
        return self.__codicefiscale
    
    @codicefiscale.setter #For later: aggiungere altri controlli per cf, per stavolta erano troppi
    def codicefiscale(self, codicefiscale):
        
        try:
            if not isinstance(codicefiscale, str):
                raise TypeError("deve essere una stringa")
            if len(codicefiscale) != 16:
                raise(ValueError("il codice fiscale deve avere sedici caratteri"))
        except(ValueError) as ve:
            print("Non siamo riusciti a creare il codice fiscale: " +str(ve))
            self.__codicefiscale = ""
        except (TypeError) as te:
            print("Non siamo riusciti a creare il nome: "+ str(te))
            self.__codicefiscale = ""
        else:
            codicefiscale = codicefiscale.lower()
            self.__codicefiscale = codicefiscale
    
    @codicefiscale.deleter
    def codicefiscale(self):
        print("Sto cancellando il codice fiscale...")
        del self.__codicefiscale
    
    # Metodi
    
    def datiPersona(self):
        str_dati = f"Cognome: {self.cognome} Nome: {self.nome}" 
        str_dati += f"\nCodice Fiscale: {self.codicefiscale}"
        return str_dati
