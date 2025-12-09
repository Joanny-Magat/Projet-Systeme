#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auteur : Joanny Magat

"""
Script qui demande en input à l'utilisateur un intervalle de longueur d'onde
(sachant que le fichier .txt et la taille de fenêtre de longueur d'onde est demandé en paramètre du script)
et affiche le plot de l'intensité en fonction de la longueur d'onde sur l'intervalle demandé.
""" 

#Exemple de ce qu'il faut taper sur le terminal pour ouvrir ce script :
#python3 recherche_plot.py /home/e20210012399/Documents/M1/SYSTEME/PROJET/Dossier-Git/Spectre_photoluminescence.txt

import matplotlib.pyplot as plt 
import intensite

cheminFichier,tailleFenetre = intensite.help()
dico=intensite.deuxiemeDico(intensite.premierDico(cheminFichier,tailleFenetre))


def demandeIntervalle(tailleFenetre):
    #Demande de l'intervalle respectant la taille de fenêtre de longueur d'ondes

    print("Quel intervalle voulez-vous ? (Doit respecter la taille des fenêtres de longueur d'onde)")
    intervallePasBon = True
    while intervallePasBon :
        
        intervalleMin=float(input("Borne inférieur de l'intervalle :"))
        intervalleMax=float(input("Borne supérieur de l'intervalle :"))

        tailleFenetreEntier=tailleFenetre #Si la tailleFenetre n'est pas entière
        iTailleFenetre=0 #Compteurs permettant de savoir combien de fois on a multiplié tailleFenetre par 10 jusqu'à avoir un entier

        while not tailleFenetreEntier.is_integer():
            tailleFenetreEntier=tailleFenetreEntier*10**iTailleFenetre
            iTailleFenetre+=1

        if intervalleMin*10**iTailleFenetre % int(tailleFenetreEntier) == 0 and intervalleMax*10**iTailleFenetre % int(tailleFenetreEntier) == 0 and 0<=intervalleMin<intervalleMax :
            #On a testé si les bornes étaient multiples de tailleFenetre pour avoir les bonnes plages par la suite
            intervallePasBon = False

        else :
            print("Bornes invalides par rapport à la taille des fenêtres de longueurs d'ondes")

    # #Arrondi des intervalles pour qu'ils correspondent à la taille de fenêtres de longueur d'onde à la place ?

    return intervalleMin,intervalleMax



def abscisse(tailleFenetre,intervalleMin,intervalleMax):
    x=[]
    
    #Détermination du nombre de décimal de tailleFenetre si celui-ci n'est pas entier :
    nbDecimal=0
    tailleFenetreEntier=tailleFenetre
    while not tailleFenetreEntier.is_integer():
        tailleFenetreEntier=tailleFenetreEntier*10**nbDecimal
        nbDecimal+=1

    #Détermination du nombre de valeur dans la liste des abscisses :
    nbValeurs=(intervalleMax-intervalleMin)/tailleFenetre #Nombre de valeurs entre la borne inf et sup avec la pas choisis
    if not nbValeurs.is_integer():
        nbValeurs = 1 + int(nbValeurs) #Exemple : si intervalle [0,10.2] avec pas de 0.1 permet d'avoir [10.1-10.2]
    
    #Ajout des valeurs dans x :
    for borneInf in [intervalleMin+n*tailleFenetre for n in range(0,int(nbValeurs))]:
        #Puisque le pas peut être un float, on ne pouvait pas faire un simple range d'où la solution ci-dessus
        if tailleFenetre.is_integer():
            x.append(f"{int(borneInf)}-{int(borneInf+tailleFenetre)}")
        else :
            x.append(f"{round(borneInf,nbDecimal)}-{round(borneInf+tailleFenetre,nbDecimal)}")
    return x


def ordonnee(dico,abscisse):
    y=[]
    for plage in abscisse:
        if f"{plage}nm" in dico:
            y.append(dico[f"{plage}nm"][2]) #2 correpond à la moyenne
        else :
            y.append(None)
    return y

def incertitude(dico,abscisse):
    y_inc=[]
    for plage in abscisse:
        if f"{plage}nm" in dico:
            minimum=dico[f"{plage}nm"][1]
            maximum=dico[f"{plage}nm"][3]
            if minimum != None and maximum != None :
                y_inc.append((maximum-minimum)/2**0.5)
            else :
                y_inc.append(None)
        else :
            y_inc.append(None)
    return y_inc

def suppressionNone(x,y,y_inc): #Pas parfait car supprime le nom de l'abscisse aussi
    x_co=[]
    y_co=[]
    y_inc_co=[]
    for i in range(len(x)):
        if y[i] != None :
            x_co.append(x[i])
            y_co.append(y[i])
            y_inc_co.append(y_inc[i])
    return x_co,y_co,y_inc_co


#Affichage du plot :

intervalleMin,intervalleMax = demandeIntervalle(tailleFenetre)

x=abscisse(tailleFenetre,intervalleMin,intervalleMax)
y=ordonnee(dico,x)
y_inc=incertitude(dico,x)

x,y,y_inc=suppressionNone(x,y,y_inc)

plt.title("Intensité moyenne en fonction des plages de longueurs d'onde en nm avec incertitude")
plt.xlabel("Plage de longueurs d'ondes en nm")
plt.ylabel("Intensité moyenne")

#Gestion de la graduation de l'abscisse pour éviter les chevauchements
positions = range(len(x))
graduationMax=100 #Nombre de graduation arbitraire pour que les graduations ne se chevauchent pas 
pasAbscisse = max(1,len(x)//graduationMax)
plt.xticks(positions[::pasAbscisse],rotation=90) #Tourne les abscisses et affiche 1 abscisse sur log(len(x)) 

plt.plot(x,y,'g-', label="Courbe reliant les points") #label est la description de la légende
plt.errorbar(x,y,yerr=y_inc,fmt='o',capsize=5,ecolor='red',label="Points d'intensité moyenne avec leur incertitude") #fmt=style de point, capsize=taille des barres horizontales au bout des incertitudes, ecolor=couleur des barres d'erreur 

plt.legend(loc="best")
plt.tight_layout() #Ajuste automatiquement les marges
plt.show()