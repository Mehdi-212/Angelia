# angelia
le futur de la musique

Angelia est une intelligence artificielle qui prédit si un titre a une chance d'être dans le TOP 50 ou pas.

Pour utiliser cette IA, il vous faudra les données d'une musique qui respecte certains paramètres.

C'est paramètre sont : Energy,duration,explicit,dancability,loudness, speechness,accoustisness,instrumentalness,liveness,valence,tempo.

Ces données devront être dans un Fichier CSV.

En ayant complété les conditions, l'IA vous prédira si vos chansons ont une chance d'être dans le TOP 50 ou pas.

IMPORTANT ! 

Cette IA n'a pas un taux de réussite à 100 % ce qui signifie qu'il y a une marge d'erreur.

Pour créer cette IA, nous avons :

Analyse des Données

Fait une Visualisation avec les paramètres Popularity et Followers de l'artiste

Création de la heatmap grâce à Seaborn

Nous avons testé trois algorithmes pour l'IA.

2 Algorithmes de Régression et 

1 de classification

Arbre de Régression multiple

Régression linéaire multiple

Régression Logistique

Résultat obtenu : R squared: 0.21

accuracy 0.87

Pour utiliser cette IA, il faut les paramètres demander dans un fichier CSV

Librairie utilisé :pandas,numpy,matplotlib,sklearn,seaborn,tkinter,sqlite3.
