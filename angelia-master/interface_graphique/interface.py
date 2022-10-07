from tkinter import *

from database.sql_class.Database import Database
import matplotlib.pyplot as plt

from interface_graphique.pages.Home import Home


# genere la ppage tkinter de l'application avec les information de la fenetre et creer la page Home via sa class afin de
# l'initialiser en envoyant des infos de la window qui a ete creer sa taille le primary background
class Main:
    primary_bg = "#d4d4d4"
    window = Tk()
    window.title("Angelia")
    window.geometry("1400x800")
    window.minsize(480, 360)
    window.iconbitmap("ressource\image\logo.ico")
    window.config(background=primary_bg)
    width = window.winfo_width()
    height = window.winfo_height()

    home = Home(window, width, height)

    def start(self):
        self.home.start()






    #
    # INUTILE juste du memotechnique
    # def new_window(self):
    #     self.frame_container.destroy()
    #     self.frame_container.config(bg=self.primary_bg, width=self.width, height=self.height)
    #     self.frame_container.pack(expand=True)
    #     print(self.frame_container)

    # plt.xlabel("duration")
    # plt.ylabel("popularity")
    # plt.scatter(Database.songs.get_duration(), Database.songs.get_popularity(), color="blue")
    # plt.savefig('plot1.png')
    #
    # width = 400
    # height = 300
    #
    # image = PhotoImage(file="plot1.png").zoom(31).subsample(50)
    #
    # frame_canvas = Canvas(frame_data, width=width, height=height, bg=primary_bg, bd=1, relief=SOLID)
    # frame_canvas.create_image(width / 2, height / 2, image=image)
    # frame_canvas.pack(expand=YES)
    #
    # plt.close()
