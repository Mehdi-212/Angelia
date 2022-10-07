from tkinter import *

# decommenter pour generer la base de données
from database.sql_class.Database import Database
from interface_graphique.pages.Spotify import Spotify
from interface_graphique.pages.Template import Template
from interface_graphique.pages.Top_ten import Top_ten
from interface_graphique.pages.Youtube import Youtube


class Home(Template):
    primary_bg = "#d4d4d4"

    def __init__(self, window, width, height):
        super().__init__()
        self.top_ten = Top_ten(window, width, height)
        self.youtube = Youtube(window, width, height)
        self.spotify = Spotify(window, width, height)
        self.window = window
        self.width = width
        self.height = height
        self.image = PhotoImage(file="background.png")
        self.image.zoom(8, 8)
        self.frame_canvas = Canvas(self.window, bg=self.primary_bg, width=self.width, height=self.height)
        self.frame_canvas.create_image(self.image.width() / 2, self.image.height() / 2, image=self.image)

        ressource_data = "ressource\Sources_data.db"

        # decommenter pour generer la base de données qui vas creer des class song et artist afin de pouvoir reutiliser
        # les données plus facilement sans avoir a resoliciter la bdd a chaque fois
        # database = Database(ressource_data)


        self.row = 0
        self.column = 0


    def start(self):
        self.row = 0
        self.column = 0

        # self.frame_image.pack()
        self.frame_canvas.pack(expand=YES, fill="both", side=BOTTOM)
        self.header()

        div = self.new_row()
        button_Top_ten = Button(div, text="Potentiel top 50", font=("Arial", 20), bg='white', fg='black', command=self.Button_topten)
        button_Top_ten.pack(expand=YES, side=LEFT, padx=15)

        button_spotifiy = Button(div, text="Spotify stats", padx=15, font=("Arial", 20), bg='white', fg='black', command=self.Button_spotify)
        button_spotifiy.pack(expand=YES, side=LEFT, padx=15)

        # for song in self.database.songs.songs:
        #     div = header.new_row()
        #     label_title = Label(div, text=song.popularity, font=("Courrier", 36), bg=self.primary_bg, padx=30)
        #     label_title.pack(expand=YES)
        self.window.mainloop()

        # permet de creer un tableau sur tkinter avec les infos de la database via les classe qui ont ete créee au prealable

        # colones_for_table_interface = ["name", "popularity", "artists"]
        # l = 0 # futur usation for grid or canvas for table
        # c = 0 # futur usation for grid or canvas for table
        # for colone in colones_for_table_interface:
        #     data_colone = Frame(frame_data, bg=primary_bg, bd=1, relief=SOLID)
        #     colone_value = Label(data_colone, text=colone, font=("Arial", 10), bg=primary_bg)
        #     colone_value.pack(side=TOP, expand=YES)
        #     for song in database.songs:
        #         data_line = Frame(data_colone, bg=primary_bg, bd=1, relief=SOLID)
        #         if colone == "artists":
        #             for artist in song.artists:
        #                 colone_value = Label(data_line, text=f"({artist.name})", font=("Arial", 10), bg=primary_bg)
        #                 colone_value.pack(side=LEFT, expand=YES)
        #         else:
        #             colone_value = Label(data_line, text=getattr(song, colone), font=("Arial", 10), bg=primary_bg)
        #             colone_value.pack(side=LEFT, expand=YES)
        #         data_line.pack(expand=YES)
        #     data_colone.pack(side=LEFT, expand=YES)

        # def new_label(self, label):
        #    label.pack(expand=YES)



