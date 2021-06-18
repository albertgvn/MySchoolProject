import tkinter as tk 
from tkinter import messagebox as Msg
from PIL import Image, ImageTk

class PageLogin(tk.Frame):
	def __init__(self, parent, App):
		self.app = App
		self.settings = App.settings


		

		super().__init__(parent)
		self.configure(bg="#ff1a1a")
		self.grid(row=0, column=0, sticky="nsew")
		parent.grid_columnconfigure(0, weight=1)
		parent.grid_rowconfigure(0, weight=1)

		self.main_frame = tk.Frame(self, height=self.settings.height, width= self.settings.width,bg="#ff1a1a")
		self.main_frame.pack(expand=True)

		frame_w = self.settings.width//3
		frame_h = self.settings.height//5

		image = Image.open(self.settings.logo_path)
		i_w, i_h = image.size
		ratio = i_w/frame_w
		new_size = (int(i_w/ratio),int(i_h/ratio)) #(x,y)
		image = image.resize(new_size)

		self.logo = ImageTk.PhotoImage(image)
		self.label_Logo = tk.Label(self.main_frame, image=self.logo,bg="#ff1a1a")
		self.label_Logo.pack(fill="y", side="right", pady=90, padx=(100,0))

		self.label_Username = tk.Label(self.main_frame, text="Username :", bg="#ff1a1a", fg="white", font=("Arial", 18, "bold"))
		self.label_Username.pack(pady=5, padx=(0,139))

		self.entry_Username = tk.Entry(self.main_frame,font=("Arial", 18, "bold"))
		self.entry_Username.pack(pady=5)

		self.label_Password = tk.Label(self.main_frame, text="Password :", bg="#ff1a1a", fg="white", font=("Arial", 18, "bold"))
		self.label_Password.pack(pady=5, padx=(0,139))

		self.entry_password = tk.Entry(self.main_frame, font=("Arial", 18, "bold"), show="*")
		self.entry_password.pack(pady=5)


		self.btn_login = tk.Button(self.main_frame, text="LOGIN", command= lambda:self.app.change_page("appPage"),width=10, bd=0, font=("Arial", 12, "bold"))
		self.btn_login.pack(side="left")

		self.btn_exit = tk.Button(self.main_frame, text="EXIT", command= exit,width=10, bd=0, font=("Arial", 12, "bold"))
		self.btn_exit.pack(side="right")