import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('donnes_luc.csv',sep=',',header=96)
file=open('donnes_luc.csv','r')
chaine_cols=file.readlines()[:96]
ligne_propre=[]
def compteur_espace(str):
    compteur=0
    for j in range(len(str)):
        if str[j]==":":
            while str[j+compteur+1]==" ":
                compteur+=1
            break
    return ":" + compteur*" "
for ligne in chaine_cols[3:-1] :
    ligne = ligne.strip()
    ligne = ligne.replace("# COLUMN ","")
    ligne=ligne.replace(compteur_espace(ligne),":")
    ligne_propre.append(ligne)
correspondance=[ligne.split(":") for ligne in ligne_propre]
for nom_colonne in correspondance:
    df.rename(columns={nom_colonne[0] : nom_colonne[1]}, inplace=True)
df