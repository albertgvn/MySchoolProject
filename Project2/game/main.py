import tkinter as tk
import sys
import time
import pygame
from config import Config
from board import Board
from ship import Ship
from player import Player
from pageLogin import PageLogin
from tkinter import messagebox as Msg 
class Window(tk.Tk):

	def __init__(self, Game):
		self.game = Game
		self.config = Game.config # (langsung ke Battleship)

		super().__init__()
		self.title(self.config.title)
		self.geometry(self.config.screen)

		self.create_container()

		self.pages = {}
		self.create_board()
		self.create_login()

	def create_container(self):
		self.containter = tk.Frame(self, bg="white")
		self.containter.pack(fill="both", expand=True)

	def create_board(self):
		self.pages['board'] = Board(self.containter, self.game)

	def create_login(self):
		self.pages['pageLogin'] = PageLogin(self.containter, self.game)



class Battleship:

	def __init__(self):
		pygame.mixer.init()
		self.config = Config()
		self.ship = Ship(self)
		self.player = Player()
		self.window = Window(self)

	def is_button_board_clicked(self, pos_x, pos_y):
		self.player.current_location(pos_x, pos_y)
		if self.ship.location == self.player.location:
			pygame.mixer.init()
			self.window.pages['board'].button_board[pos_x][pos_y].configure(image=self.window.pages['board'].win_img_btn)

			Msg.showinfo('Congratulations','!!! YOU WIN !!!')	
			sys.exit()	
		else:
			self.window.pages['board'].button_board[pos_x][pos_y].configure(image=self.window.pages['board'].final_img_btn)


	def change_page(self, page):
		page = self.window.pages['board']
		page.tkraise()

	def run(self):
		pygame.mixer.music.load(self.config.music)
		pygame.mixer.music.set_volume(0.3)
		pygame.mixer.music.play()
		self.window.mainloop()



if __name__ == '__main__':
	my_battleship = Battleship()
	my_battleship.run()