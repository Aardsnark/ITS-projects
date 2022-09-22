# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 15:06:32 2022

@author: user
"""
from cl_amministratore import creaAdmin
from menus import logmenu
import os

# Profili Utenti Test:
#     Admin --> user: Marco24 ; pw: Mario123!
#     Studente --> codicefiscale: rossjohn12345678
#     Docente --> codicefiscale: rossliza12345678

def checkdirectories():
    if not os.path.exists(".\\Utenti"):
        os.mkdir(".\\Utenti") #directory pickle files per Studenti, Docenti e Admins
    if not os.path.exists(".\\Utenti\\Studenti"):
        os.mkdir(".\\Utenti\\Studenti")
    if not os.path.exists(".\\Utenti\\Docenti"):
        os.mkdir(".\\Utenti\\Docenti")
    if not os.path.exists(".\\Utenti\\Admin"):
        os.mkdir(".\\Utenti\\Admin")
    if not os.path.exists(".\\Pagelle"):
        os.mkdir(".\\Pagelle") #check path e funzione
    if not os.path.exists(".\\SchedeDocenti"):
        os.mkdir(".\\SchedeDocenti") #check path e funzione

def main():
    print("==== ANAGRAFE SCUOLA ====")
    
    checkdirectories()
    
    risp = input("Benvenuto/a/*, Utente. Possiedi già un profilo admin? [Y/n]: ")
    if risp[0].lower() == "y":
        print("Accesso al menu di login...")
        logmenu()
    elif risp[0].lower() == "n":
        print("Creazione profilo Admin...")
        creaAdmin()


if __name__ == "__main__":
    main()