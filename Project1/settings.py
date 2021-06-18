import pygame

class Settings:

	def __init__(self):
		self.screen_width = 800
		self.screen_height = 600
		self.title = "*Alien Invasion*"
		self.screen_color = [255, 255, 255]

		#setting ship
		self.ship_speed = 1
		self.ship_life = 5
		self.rocket_speed = 1

		#setting bullet
		self.bullet_speed = 1.0
		self.bullet_width = 15
		self.bullet_height = 3
		self.bullet_color = (60, 60, 60)
		self.bullets_limit = 5

		#setting alien
		#self.alien_speed = 0.5
		self.alien_army_drop_speed = 5.0
		#self.alien_army_direction = 1 # 1 right , -1 left

		#scaling level
		self.speedup_level = 1.5
		self.score_scale = 2.0

		self.init_dynamic_settings()

	def init_dynamic_settings(self):
		self.ship_speed = 2
		self.bullet_speed = 1.0
		self.alien_speed = 1.0
		self.alien_points = 50

		self.alien_army_direction = 1 #1 right, -1 left

	def increase_speed(self):
		self.ship_speed *= self.speedup_level
		self.bullet_speed *= self.speedup_level
		self.alien_speed *= self.speedup_level