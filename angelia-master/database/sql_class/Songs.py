from database.sql_class.Song import Song


class Songs:
    songs: list[Song] = []

    def get_duration(self):
        res = []
        for song in self.songs:
            res.append(song.duration*0.00001666666666666666)
        return res

    def get_popularity(self):
        res = []
        for song in self.songs:
            res.append(song.popularity)
        return res

    

