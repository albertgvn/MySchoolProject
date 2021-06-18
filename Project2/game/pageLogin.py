import tkinter as tk
from PIL import Image, ImageTk

class PageLogin(tk.Frame):

	def __init__(self, parent, App):
		self.app = App
		self.config = App.config

		super().__init__(parent)
		self.configure(bg="#54A7AC")
		self.grid(row=0, column=0, sticky="nsew")
		parent.grid_columnconfigure(0, weight=1)
		parent.grid_rowconfigure(0, weight=1)


		self.main_frame = tk.Frame(self, height=self.config.height, width=self.config.width,bg="#54A7AC")
		self.main_frame.pack(expand=True)

		image = Image.open(self.config.logo_path)
		image_w, image_h = image.size
		ratio = (image_w/self.config.width)
		image = image.resize((int(image_w//ratio)//2, int(image_h//ratio)//2))
		
		self.logo = ImageTk.PhotoImage(image)
		self.label_Logo = tk.Label(self.main_frame, image=self.logo)
		self.label_Logo.pack(pady=5)

		self.label_username = tk.Label(self.main_frame, text="Username", bg="#54A7AC", fg="white", font=("Arial", 16, "bold"))
		self.label_username.pack(pady=5)

		self.nameVar = tk.StringVar()
		self.entry_username = tk.Entry(self.main_frame, font=("Arial", 16, "bold"), textvariable=self.nameVar)
		self.entry_username.pack(pady=5)

		self.label_password = tk.Label(self.main_frame, text="Password", bg="#54A7AC", fg="white", font=("Arial", 16, "bold"))
		self.label_password.pack(pady=5)

		self.passwordVar = tk.StringVar()
		self.entry_password = tk.Entry(self.main_frame, font=("Arial", 16, "bold"), show="*", textvariable=self.passwordVar)
		self.entry_password.pack(pady=5)		

		self.btn_login = tk.Button(self.main_frame, text="LOGIN", width=10, height=2, command=lambda:self.app.change_page("board"))
		self.btn_login.pack(pady=10)

