
class Config:


	def __init__(self):

		#GAME CONFIG
		self.title = "Lucky Test Game"
		self.row = 5
		self.column = 5


		#WINDOW CONFIG
		base  = 100
		ratio = 5
		self.width = ratio*base
		self.height = ratio*base
		self.side = base*ratio
		self.screen = f"{self.side}x{self.side}+500+500"


		#IMG PATH
		self.init_img = "img/init_img.png"
		self.final_img = "img/final_img.png"
		self.win_img = "img/win_img.png"
		self.dtw_img = "img/final_img2.png"	

		self.app_title = "My App"

		#WINDOW_CONFIG
		base = 100
		w_ratio = 3
		h_ratio = 4

		self.logo_path = "img/lock_image.jpg"
		self.username = "ADMIN"
		self.password = "12345"

		self.music = "mp3/song.wav"