import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

	def __init__(self, info_game):
		super().__init__()
		self.screen = info_game.screen
		self.settings = info_game.game_setting
		self.image = pygame.image.load('objek/aliens.png')
		self.rect = self.image.get_rect()

		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		self.y = float(self.rect.y)

	def update(self):
		self.y -= self.settings.alien_speed * self.settings.alien_army_direction
		self.rect.y = self.y

	def _check_edges(self):
		screen_rect = self.screen.get_rect()
		if (self.rect.bottom >= screen_rect.bottom) or (self.rect.top <= screen_rect.top):
			return True