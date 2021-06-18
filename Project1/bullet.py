import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

	def __init__(self, info_game):
		super().__init__()
		self.screen = info_game.screen
		self.game_setting = info_game.game_setting
		self.color = self.game_setting.bullet_color

		self.rect = pygame.Rect(0,0, self.game_setting.bullet_width, self.game_setting.bullet_height)

		self.rect.midleft = info_game.game_ship.rect.midleft

		self.x = float(self.rect.x)

	def update(self):
		self.x -= self.game_setting.bullet_speed

		self.rect.x = self.x


	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect)