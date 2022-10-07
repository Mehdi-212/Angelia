from tkinter import *


# TTemplate des fenetres/pages afin de pouvoir y ajouter des function communes tel que la creation dune nouvelle ligne--
# --ou colonne grace a un grid implementer un header ou encore l'implementation des boutons d'accees aux pages
class Template:
    def __init__(self):
        self.top_ten = None
        self.row = None
        self.primary_bg = None
        self.spotify = None
        self.frame_canvas = None

    def Button_topten(self):
        self.frame_canvas.destroy()
        self.top_ten.start()

    def Button_spotify(self):
        self.frame_canvas.destroy()
        self.spotify.start()

    def Button_deezer(self):
        self.frame_canvas.destroy()
        self.spotify.start()

    def Button_youtube(self):
        self.frame_canvas.destroy()
        self.spotify.start()

    def header(self):
        div = self.new_row()
        label_title = Label(div, text="Bienvenue sur Angelia", font=("Courrier", 36), bg=self.primary_bg, padx=30)
        label_title.pack(expand=True, side=BOTTOM)
        div = self.new_row()
        label_subtitle = Label(div, text="IA de prediction de popularité des musiques", font=("Courrier", 22),
                               bg=self.primary_bg, padx=30)
        label_subtitle.pack(expand=True, side=BOTTOM)

    def new_row(self):
        self.column = 0
        grid = Frame(self.frame_canvas, bg=self.primary_bg, pady=15)
        grid.grid(row=self.row, column=self.column)
        self.row += 1
        return grid

    def new_column(self):
        self.column += 1
        grid = Frame(self.frame_canvas, bg=self.primary_bg)
        grid.grid(row=self.row, column=self.column)
        return grid
