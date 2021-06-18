import tkinter as tk
#import pygame
import sys

from tkinter import messagebox
from settings import Settings
from appPage import AppPage
from PageLogin import PageLogin


class Window(tk.Tk):

	def __init__(self, App):
		self.app = App
		self.settings = App.settings

		super().__init__()
		self.title(self.settings.title)
		self.geometry(self.settings.screen)
		self.resizable(0,0)

		self.create_menu()

		self.create_container()


		self.pages = {}
		self.create_appPage()
		self.create_loginPage()

	def create_menu(self):
		self.menu_bar = tk.Menu(self)
		self.configure(menu=self.menu_bar)

		self.file_menu = tk.Menu(self.menu_bar, tearoff=False)
		self.file_menu.add_command(label="New Ticket", command=self.app.p)
		self.file_menu.add_command(label="Exit", command=self.app.exit)

		self.help_menu = tk.Menu(self.menu_bar, tearoff=False)
		self.help_menu.add_command(label="About", command=self.app.dtw)

		self.menu_bar.add_cascade(label='File', menu=self.file_menu)
		self.menu_bar.add_cascade(label='Help', menu=self.help_menu)

	def create_container(self):
		self.container = tk.Frame(self)
		self.container.pack(fill="both", expand=True)

	def create_appPage(self):
		self.pages["appPage"] = AppPage(self.container, self.app)

	def create_loginPage(self):
		self.pages["PageLogin"] = PageLogin(self.container, self.app)


class ContactApp:

	def __init__(self):
		#pygame.mixer.init()
		self.settings = Settings()
		self.window = Window(self)

	def exit(self):
		respond = messagebox.askyesnocancel("Exit Program", "Are you sure to close the program ?")
		if respond:
			sys.exit()

	def change_page(self, page):
		page = self.window.pages["appPage"]
		page.tkraise()

	def p(self):
		self.window.pages["appPage"].clicked_add_new_btn()

	def dtw(self):
		a = messagebox.showinfo("About App", "Vers.1.0")
		

	def run(self):
		#pygame.mixer.music.load(self.settings.music)
		#pygame.mixer.music.set_volume(0.3)
		#pygame.mixer.music.play()
		self.window.mainloop()



if __name__ == '__main__':
	myContactApp = ContactApp()
	myContactApp.run()