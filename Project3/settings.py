from json import load, dump
class Settings:

	def __init__(self):

		#App Conf
		self.title = "Parking Ticket App"


		#Window Conf
		base = 50
		ratio = (16, 9)
		self.width = base*ratio[0]
		self.height = base*ratio[1]
		self.screen = f"{self.width}x{self.height}"

		self.logo_path ="img/kunci.png"


		#Img Conf
		self.logo = "img/logo2.png"
		#self.music = "mp3/lagu.mp3"

		#Contacts Dummy
		self.contacts = None
		self.load_data_from_json()

	def load_data_from_json(self):
		with open("data/contacts.json", "r") as file_json:
			self.contacts = load(file_json)
	def save_data_to_json(self):
		with open("data/contacts.json", "w") as file_json:
			dump(self.contacts, file_json)