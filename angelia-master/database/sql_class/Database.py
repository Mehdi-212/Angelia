import sqlite3

from database.sql_class.Artist import Artist
from database.sql_class.Song import Song
from database.sql_class.Songs import Songs


class Database:
    songs: Songs = Songs()

    def __init__(self, ressource_data):
        self.ressource_data = ressource_data
        self.init_data()

    def init_data(self):


        sql_song = "SELECT id, name, popularity, duration_ms, explicit, id_artists, release_date, energy, acousticness  FROM chansons ORDER BY popularity DESC LIMIT 50;"

        try:

            # fait une requete au .db afin de recuper la base de données et enregistrer dans les class les informations
            conn = sqlite3.connect(self.ressource_data)
            cur = conn.cursor()
            print("Base de données crée est correctement connectée à SQLite")
            cur.execute(sql_song)
            res = cur.fetchall()
            print("Données class created")
            song_data_temp: list = res

            for data in song_data_temp:
                artists = []
                for artist in data[5][2:-2].split("', '"):
                    # fait une requete au .db afin de recuperer les artists a partir des id recuperer dans les chansons
                    sql_artist = f"SELECT id, name, popularity, followers FROM artistes WHERE id = '{artist}';"
                    cur.execute(sql_artist)
                    artist_data_temp = cur.fetchall()
                    artists.append(Artist(artist_data_temp[0][0], artist_data_temp[0][1], artist_data_temp[0][2],
                                          artist_data_temp[0][3]))

                self.songs.songs.append(Song(data[0], data[1], data[2], data[3],
                                             data[4], artists, data[6],
                                             data[7], data[8]))

            cur.close()
            conn.close()
            print("La connexion SQLite est fermée")

        except sqlite3.Error as error:
            print("Erreur lors de la connexion à SQLite", error)


    def create_connection(self, sql):
        try:
            conn = sqlite3.connect(self.ressource_data)
            cur = conn.cursor()
            print("Base de données crée est correctement connectée à SQLite")
            cur.execute(sql)
            res = cur.fetchall()
            print("Données class created")
            # for p in res:
            #    print(f"{p}\n")
            cur.close()
            conn.close()
            print("La connexion SQLite est fermée")
            return res
        except sqlite3.Error as error:
            print("Erreur lors de la connexion à SQLite", error)
