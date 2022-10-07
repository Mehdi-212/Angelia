import sqlite3
import pathlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn import metrics


class Ia:
    # Création d'un dataframe à partir d'un fichier csv, définition de la target(popularity) et des différents paramètres à utiliser
    dataset = pd.read_csv("ressource\chansons.csv")
    X = dataset[['duration_ms', 'explicit', 'danceability', 'energy',
           'loudness', 'speechiness', 'acousticness', 'instrumentalness',
           'liveness', 'valence', 'tempo']]
    y = dataset['popularity']
    #Division du jeux de données en 2 jeux : train et test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
    #Entrainement de l'algorithme Decision Tree Regression
    regressor = DecisionTreeRegressor()
    regressor.fit(X_train, y_train)
    y_pred = regressor.predict(X_test)
    #Comparaison des données prédites et réelles
    df=pd.DataFrame({'Actual':y_test, 'Predicted':y_pred})
    #Nettoyage des données
    dataset = dataset[dataset.popularity != 0]
    dataset = dataset[dataset.duration_ms < 1000000]
    dataset = dataset[dataset.tempo != 0]

    #Deuxième algorithme : Logistic Regression
    #Choix des classes pour l(algorithme de classification
    y[y < 50]=0
    y[y >= 50]=1

    #Division du jeux de données en 2 jeux : train et test
    X_train,X_test, y_train,y_test = train_test_split(X,y,test_size = 0.20,random_state = 0)

    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    #Entrainement du second algorithme
    classifier = LogisticRegression()
    classifier.fit(X_train, y_train)

    y_pred = classifier.predict(X_test)

    #Vérification de la fiabilité de l'IA
    accuracy = accuracy_score(y_test, y_pred)
    print(accuracy)

    ConfusionMatrix = confusion_matrix(y_test, y_pred)
    print(confusion_matrix)

    dataset.loc[:,"popularity"].describe()
    print(dataset.loc)

    dataset.loc[:,"popularity"].plot.hist()
    print(dataset.loc)

    accuracy_array = np.array([0.1])
    print(accuracy_array)

    #Amélioration des prédiction de l'IA avec l'intégration de probabilité
    for i in range(12000):
        y_pred = classifier.predict_proba(X_test)[:,1]
        y_pred [y_pred >= (i/10000)]=1
        y_pred [y_pred < (i/10000)]=0
        cm = confusion_matrix(y_test, y_pred).ravel()
        accuracy = cm[3]/cm[3]+cm[1]*100
        accuracy_array = np.insert(accuracy_array, i , [accuracy],axis = 0)
    pd.DataFrame(accuracy_array).plot.line()

    accuracy = accuracy_score(y_test, y_pred)
    print(accuracy)


    #Utilisation de l'IA entrainée pour prédire de nouvelles musiques
    def calculate_popularity(self):

        my_song = f"{input()}.csv"
        X_my_song = my_song[['duration_ms', 'explicit', 'danceability', 'energy',
                             'loudness', 'speechiness', 'acousticness', 'instrumentalness',
                             'liveness', 'valence', 'tempo']]
        y_my_song = self.classifier.predict(X_my_song)
        print("Prediction for this song: {}".format(y_my_song))

        for x in y_my_song:
            if x > 0:
                print('The song will be a top 50 hit !!!')
            else:
                print('The song will not be in the top 50')
