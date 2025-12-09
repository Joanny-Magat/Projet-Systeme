#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auteur : Joanny Magat

"""
Script qui prend en entré le fichier Spectre_photoluminescence.txt
(contenant l'intensité de chaque longueur d'onde) et la taille de fenêtres pour les longueurs d'onde.
Il renvoie un dictionnaire de liste dont la clée est la plages de longueurs d'onde et
la valeur une liste contenant le nombre d'intensité par plage, le minimum d'intensité pour la plage,
la moyenne et le maximum. 
"""
#Exemple de ce qu'il faut taper sur le terminal pour ouvrir ce script :
#python3 intensite.py /home/e20210012399/Documents/M1/SYSTEME/PROJET/Dossier-Git/Spectre_photoluminescence.txt

import sys, re

def help():
    #Initialisation des paramètres d'entrée

    if len(sys.argv)==2 :
        cheminFichier = sys.argv[1]
        tailleFenetre = 10.0
        if open(cheminFichier) == 0:
            print("ERREUR : le fichier ne renvoie aucune information")
            exit()
    elif len(sys.argv)==3 :
        cheminFichier = sys.argv[1]
        tailleFenetre = float(sys.argv[2])
        if open(cheminFichier) == 0:
            print("ERREUR : le fichier ne renvoie aucune information")
            exit()
        if tailleFenetre <=0 :
            print("ERREUR : la taille de fenêtre de longueur d'onde doit être > 0")
            exit()
    else :
        print("ERREUR : il faut 1 ou 2 paramètres en entré du fichier : au moins le fichier .txt.")
        print("En second paramètre, on peut aussi mettre la taille de fenêtres pour les longueurs d'onde (10 par défaut)")
        exit()
    return cheminFichier,tailleFenetre


def DicoListe(cheminFichier,tailleFenetre):
    #Ouverture du fichier et séparation des lignes.
    #Les lignes sont séparées en longueur et en intensité.
    #Les données sont stockées dans un premier dictionnaire de clée plage de longueur
    #et de valeur la liste des intensités dans cette plage


    #Initialisation du dico
    dico1 = {}
    if tailleFenetre.is_integer():
        plageMin=0
        plageMax= plageMin + int(tailleFenetre)
    else :
        plageMin = 0.0 #début de la plage en cours 
        plageMax = plageMin + tailleFenetre
    plage = f"{str(plageMin)}-{str(plageMax)}nm" #str est facultatif mais c'est plus explicite
    dico1[plage]=[]


    #Détermination du nombre de décimal de tailleFenetre si celui-ci n'est pas entier:
    nbDecimal=0
    tailleFenetreEntier=tailleFenetre
    while not tailleFenetreEntier.is_integer():
        tailleFenetreEntier=tailleFenetreEntier*10**nbDecimal
        nbDecimal+=1


    fd=open(cheminFichier)
     
    lignes = fd.readlines()
        
    for ligne in lignes :
            
        res=re.search("(^\d+\.\d+).(-?\d+\.\d+)",ligne)
        #le ^ c'est pour le début, \d c'est pour un chiffre, le + c'est une répétition du terme d'avant, . c'est pour n'importe quel caractère, le ? c'est pour optionnel
            
        if res : #Permet de ne sélectionner que les lignes avec les données 
                
            longueur=float(res.group(1))
            intensite=float(res.group(2))
                

            if plageMin <= longueur and longueur < plageMax : #On est dans la plage donc la clée est déjà créé
                dico1[plage].append(intensite)
                

            elif longueur >= plageMax :                                   #On sort de la plage mais on n'est pas forcément dans la plage suivante !
                while not(plageMin <= longueur and longueur < plageMax) : #Tant qu'on n'est pas dans la plage...
                    plageMin = plageMax                                   #La plage min devient l'ancienne plage max
                    if tailleFenetre.is_integer():                        #On rajoute le pas à la plage max et on nomme la nouvelle plage
                        plageMax += int(tailleFenetre)                    #Entier pour l'encodage du dico 
                        plage = f"{str(plageMin)}-{str(plageMax)}nm"                   
                    else :
                        plageMax += tailleFenetre
                        plage = f"{str(round(plageMin,nbDecimal))}-{str(round(plageMax,nbDecimal))}nm" 
                    dico1[plage]=[]                                       #On crée l'entrée du dico pour cette plage avec une valeur vide
                #A la sortie du while, la clée est créée pour la longueur actuelle
                dico1[plage].append(intensite)


            else : # longueur < plageMin ce qui est normalement impossible
                print("ERREUR : longueur < plageMin à la ligne :")
                print(ligne)

    return dico1


def DicoStat(dico1):
    #Création du deuxième dictionnaire avec les statistiques

    dico2={}

    for plage in dico1:
        
        liste=dico1[plage] #Liste des intensités pour cette plage
        liste.sort()
        nombre=len(liste)
        
        if nombre != 0 :
            minimum=liste[0]
            moyenne=sum(liste)/nombre
            maximum=liste[-1]

        else : #Pour les listes vides ex la plage 0-10nm si tailleFenetre=10
            minimum=None
            moyenne=None
            maximum=None
            #J'ai choisi de mettre None quand il n'y a pas de donnée car 0 est en soi une intensité donc physiquement c'est faux

        dico2[plage]=[nombre,minimum,moyenne,maximum]

    return dico2

help()
#Le help() sert ici lorsque ce script est lancé seul. Il vérifie juste que les paramètres d'entrée soit bon même si en soit il ne renvoie rien