# Projet Système (Physique Numérique)
Auteur : Joanny Magat <br>
Mail Etudiant : joanny.magat@etu.umontpellier.fr <br>
Mail Perso : joanny.magat@gmail.com <br>
Projet de M1 de l'UE Système à la Faculté des Sciences de Montpellier (Année 2025-2026) <br>


PRINCIPE DU SCRIPT <br>
Le but du script est d'analyser un fichier texte contenant le spectre d'une photodiode et d'en renvoyer un graphe. <br>
Concrètement, le fichier associe pour chaque longueur d'onde une intensité. <br> 
Le script récupère ces informations et, en demandant une taille de fenêtre de longueur d'onde et un intervalle à l'utilisateur, affiche le graphe des intensités moyennes en fonction de chaque plage de longueur d'onde sur l'intervalle demandé. <br>


UTILISATION DU SCRIPT <br>
Téléchargez tous les fichiers et mettez les dans le même dossier. <br>
Lancez le main.sh avec comme paramètres : <br>
- help ou -h pour avoir plus d'informations <br>
- le chemin du fichier texte ainsi que la taille de fenêtre de longueur d'onde (facultatif, par défaut 10nm) <br>

Entrez enfin l'intervalle demandé. Chaque borne doit être un multiple de la taille de fenêtre. <br>
Puisque le fichier texte contient des longueurs d'onde entre 339.67 et 1024.12 nm, il est conseillé de demander l'intervalle [0,2000] (à ajuster si 2000 n'est pas multiple de la taille de fenêtre) afin d'afficher tout le graphe. L'utilisateur pourra ensuite zoomer à sa convenance. <br>
