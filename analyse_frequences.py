#! /usr/bin/env python3

"""fonctions pour l'analyse des fréquence des caractères d'un texte"""

import os
import sys
import csv
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def lire_fichier(fichier):
    pass
    
def lire_csv(path):
    fichier = open(path, encoding="utf-8")
    lecteur=csv.reader(fichier, delimiter=";")
    data = list(lecteur)
    fichier.close()
    return data

fichier = lire_csv("letter_frequency.csv")  
print(fichier)

def lire_stdin():
    pass
    
def structurer_reference_freqs(data) :
    langues = []
    freqs = []
    ref = {}
    for i, langue in enumerate(data[0]):
        if i>0 : 
            langues.append(langue)
            freqs.append({})
    for l in range(1, len(data)):
        lettre = data[l][0]
        for f in range (1, len(data[l])):
            freqs[f-1][lettre] = float(data[l][f].strip("%*"))/100
    for i, langue in enumerate(langues):
        ref[langue] = freqs[i]
    return ref
dossier = structurer_reference_freqs(fichier)
print(dossier)
    
def enrichir_reference_freqs(ref,langue, chemin):
    pass
    
def compter_occurrences(texte):
    pass
    
def normaliser_occurrences(d, nb):
    pass

if __name__ == "__main__":
    pass

