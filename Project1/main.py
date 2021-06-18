import sys
import pygame

from random import randint
import time

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from star import Star
from game_statistic import GameStatistics
from button import Button
from scoreboard import Scoreboard

class AlienGame:

	def __init__(self):
		pygame.init()
		self.game_setting = Settings()
		self.my_statistics = GameStatistics(self)
		self.error = False
		self.screen = pygame.display.set_mode([self.game_setting.screen_width,self.game_setting.screen_height])
		self.game_setting.screen_width = self.screen.get_rect().width
		self.game_setting.screen_height = self.screen.get_rect().height

		self.title = pygame.display.set_caption(self.game_setting.title)
		self.screen_color = self.game_setting.screen_color

		self.game_ship = Ship(self)

		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()
		self.stars = pygame.sprite.Group()

		self.play_button = Button(self, "PLAY")
		self.score_board = Scoreboard(self)

		self._create_enemies()
		self._create_stars_random()

	def run_game(self):
		while not self.error:
			self._check_events()

			if self.my_statistics.game_active:
				self.game_ship.update()
				self._update_bullets()
				self._update_aliens()
				self._check_empty_aliens()

			self._update_frame()

			
	def _check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)

			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self._check_play_button(mouse_pos)

	def _check_keydown_events(self, event):
		if event.key == pygame.K_w:
			self.game_ship.moving_up = True
		elif event.key == pygame.K_a:
			self.game_ship.moving_left = True
		elif event.key == pygame.K_s:
			self.game_ship.moving_down = True
		elif event.key == pygame.K_d:
			self.game_ship.moving_right = True
		elif event.key == pygame.K_p:
			self._start_game()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()
		elif event.key == pygame.K_q:
			sys.exit()

	def _check_keyup_events(self, event):
		if event.key == pygame.K_w:
			self.game_ship.moving_up = False
		elif event.key == pygame.K_s:
			self.game_ship.moving_down = False
		elif event.key == pygame.K_d:
			self.game_ship.moving_right = False
		elif event.key == pygame.K_a:
			self.game_ship.moving_left = False

	def _start_game(self):
		status_game_active = self.my_statistics.game_active
		if not status_game_active:
			self.my_statistics.reset_statistics()
			self.my_statistics.game_active = True

			self.aliens.empty()
			self.bullets.empty()

			self._create_enemies()
			self.game_ship.reset_position_ship()
			pygame.mouse.set_visible(False)


	def _check_play_button(self, mouse_pos):
		button_clicked = self.play_button.rect.collidepoint(mouse_pos)
		status_game_active = self.my_statistics.game_active
		if button_clicked and not status_game_active:
			self.my_statistics.reset_statistics()
			self.game_setting.init_dynamic_settings()
			self.my_statistics.game_active = True
			self.score_board.show_score()
			self.score_board.show_level()
			self.score_board.show_ships()
			self.aliens.empty()
			self.bullets.empty()

			self._create_enemies()
			self.game_ship.reset_position_ship()
			pygame.mouse.set_visible(False)

	def _fire_bullet(self):
		if self.game_setting.bullets_limit > len(self.bullets):
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _update_bullets(self):
		self.bullets.update()
		for bullet in self.bullets.copy():
			if bullet.rect.bottom < 0:
				self.bullets.remove(bullet)

		collisionsP1 = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

		if collisionsP1:
			for aliens_hit in collisionsP1.values():
				self.my_statistics.score += self.game_setting.alien_points * len(aliens_hit)
			self.score_board.show_score()
			self.score_board.check_high_score()

		self._check_empty_aliens()

		if len(self.aliens) == 0:
			self.bullets.empty()
			self._create_enemies()
			self.game_setting.increase_speed()

	def _check_empty_aliens(self):
		if not self.aliens:
			self.bullets.empty()
			self._create_enemies()
			self.game_setting.increase_speed()

			self.my_statistics.level += 1
			self.score_board.show_level()

	def _create_enemies(self):
		alien = Alien(self)
		#alien_width = alien.rect.width
		alien_width, alien_height = alien.rect.size
		available_space_x = self.game_setting.screen_width - (2 * alien_width)
		number_aliens_x = available_space_x // (2 * alien_width)
 
		ship_height = self.game_ship.rect.height
		available_space_y = self.game_setting.screen_height - ship_height - (3 * alien_height)
		number_aliens_y = available_space_y // (2 * alien_height)
 
		for row_number in range(number_aliens_y):
			for every_alien in range(1,number_aliens_x):
				self._create_alien(every_alien, row_number)
		#print(alien.rect)

	def _create_alien(self, alien_number, row_number):
		alien = Alien(self)
		#alien_width = alien.rect.width
		alien_width, alien_height = alien.rect.size
		alien.y = alien_height + 2 * alien_height * alien_number
		alien.rect.y = alien.y
		alien.rect.x = alien.rect.width + (2 * alien.rect.width * row_number)
		self.aliens.add(alien)

	def _update_aliens(self):
		self._check_alien_army_edges()
		self.aliens.update()

		if pygame.sprite.spritecollideany(self.game_ship, self.aliens):
			self._ship_hit()
		self._check_alien_army_bottom()

	def _ship_hit(self):

		if self.my_statistics.my_shipP1_life > 0:
			self.my_statistics.my_shipP1_life -= 1
			self.score_board.show_ships()

			self.aliens.empty()
			self.bullets.empty()

			self._create_enemies()
			self.game_ship.reset_position_ship()

			time.sleep(0.5)
		else:
			self.my_statistics.game_active = False
			pygame.mouse.set_visible(True)

	def _check_alien_army_bottom(self):
		screen_rect = self.screen.get_rect()
		for alien in self.aliens.sprites():
			if alien.rect.right >= screen_rect.right:
				self._ship_hit()
				break

	def _check_alien_army_edges(self):
		for alien in self.aliens.sprites():
			if alien._check_edges():
				self._change_alien_army_direction()
				break

	def _change_alien_army_direction(self):
		for alien in self.aliens.sprites():
			alien.rect.x += self.game_setting.alien_army_drop_speed
		self.game_setting.alien_army_direction *= -1

	def _create_stars_regular(self):
		star = Star(self)
		star_width, star_height = star.rect.size
		available_space_x = self.game_setting.screen_width - (2 * star_width)
		number_star_x = available_space_x // (2 * star_width)

		available_space_y = self.game_setting.screen_height - (3 * star_height)
		number_star_y = available_space_y // (2 * star_height)

		for row_number in range(number_star_y):
			for every_star in range(1, number_star_x):
				star = Star(self)
				star.x = star_width + 2 * star_width * every_star
				star.rect.x = star.x
				star.rect.y = star.rect.height + (2 * star.rect.height * row_number)
				self.stars.add(star)

	def _create_stars_random(self):
		star = Star(self)
		star_width, star_height = star.rect.size
		number_stars = ((self.game_setting.screen_width * self.game_setting.screen_height) // (star_width*star_height)) // 33

		for every_star in range(number_stars):
			star = Star(self)
			star.rect.x = randint(0, self.game_setting.screen_width)
			star.rect.y = randint(0, self.game_setting.screen_height)
			self.stars.add(star)

	def _update_frame(self):
		self.screen.fill(self.screen_color)
		self.score_board.draw_score()
		#put your transform code here
		#self.screen.blit(self.bg_image, (0,0)) #imgae (gambar), (0,0) #position

		self.stars.draw(self.screen)
		self.game_ship.blitme()


		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.aliens.draw(self.screen)

		if not self.my_statistics.game_active:
			self.play_button._draw_button()

		pygame.display.flip() #frame dalam game jalan.

if __name__ == "__main__": #expression (true/false)
	theGame = AlienGame() #assignment (pengisian memori)
	theGame.run_game()

#variable -> attribute
#function -> method