#Ce script lance simplement recherche_plot.py avec les bons paramètres d'entrée (la vérification des paramètres se font dans intensite.py)
#Ce sript affiche également une aide si on met en argument help ou -h

clear

#Exemple de ce qu'il faut taper sur le terminal pour ouvrir ce script :
#chmod a+o+r+x main.sh
#./main.sh /home/e20210012399/Documents/M1/SYSTEME/PROJET/Dossier-Git/Spectre_photoluminescence.txt

if [[ $# == 0 || $# > 2 ]] #le $# renvoie le nombre de paramètre mis en entrée
then
    echo "ERREUR : le script doit avoir un ou deux paramètres d'entrée !"
    echo "Mettre en paramètre help ou -h pour plus d'informations"
    exit
fi

if [[ $1 == "help" || $1 == "-h" ]]
then
    echo "HELP :"
    echo "Ce sript a pour objectif d'afficher un graphe reliant pour chaque plage de longueur d'onde l'intensité moyenne associé émie par une photodiode."
    echo "Il prend en premier argument le chemin d'un fichier texte associant pour chaque longueur d'onde une intensité (généralement le fichier Spectre_photoluminescence.txt)"
    echo "Il prend en second argument un réel correspondant à la taille de fenètre de longueur d'onde souhaitée"
    echo "Le script demande alors l'intervalle de longueur d'onde à afficher dans le graphe (qui doit idéalement être un multiple de la taille de fenètre choisie)"
    echo "Le script affiche enfin le graphe souhaité"
    exit
fi

if [[ $# == 1 ]]
then
    python3 recherche_plot.py "$1"
fi

if [[ $# == 2 ]]
then
    python3 recherche_plot.py "$1" "$2"
fi