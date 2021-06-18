import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


class AppPage(tk.Frame):

	def __init__(self, parent, App):
		self.app = App
		self.settings = App.settings
		self.current_contact = self.settings.contacts[0]
		self.last_current_contact_index = 0
		self.update_mode = False
		self.contacts_index = []

		super().__init__(parent) # window.conteiner
		self.grid(row=0, column=0, sticky="nsew")

		parent.grid_rowconfigure(0, weight=1)
		parent.grid_columnconfigure(0, weight=1)

		self.create_left_frame()
		self.create_right_frame()
		self.config_left_right_frame()



	def create_left_frame(self):
		self.left_frame = tk.Frame(self, bg="pink")
		self.left_frame.grid(row=0, column=0, sticky="nsew")
		self.create_left_header()
		self.create_left_content()

	def create_right_frame(self):
		self.right_frame = tk.Frame(self, bg="#cc8800", width=2*self.settings.width//3)
		self.right_frame.grid(row=0, column=1, sticky="nsew")
		self.create_right_header()
		self.create_right_content()
		self.create_right_footer()

	def config_left_right_frame(self):
		self.grid_columnconfigure(0, weight=1) # 1/3
		self.grid_columnconfigure(1, weight=2) # 2/3
		self.grid_rowconfigure(0, weight=1)

	def create_left_header(self):
		frame_w = self.settings.width//3
		frame_h = self.settings.height//5
		self.left_header = tk.Frame(self.left_frame, width=frame_w, height=frame_h, bg="#cc8800")
		self.left_header.pack()

		image = Image.open(self.settings.logo)
		i_w, i_h = image.size
		ratio = i_w/frame_w
		new_size = (int(i_w/ratio),int(i_h/ratio)) #(x,y)
		image = image.resize(new_size)
		self.logo = ImageTk.PhotoImage(image)

		self.label_logo = tk.Label(self.left_header, image=self.logo, bg="white")
		self.label_logo.pack()

		self.searchbox_frame = tk.Frame(self.left_header, bg="#cc8800", width=frame_w, height=frame_h//4)
		self.searchbox_frame.pack(fill="x")

		self.entry_search_var = tk.StringVar()
		self.entry_search = tk.Entry(self.searchbox_frame, bg="white", fg="black", font=("Arial", 14), textvariable=self.entry_search_var)
		self.entry_search.grid(row=0, column=0)

		self.button_search = tk.Button(self.searchbox_frame, bg="orange", fg="#804000", font=("Arial", 14), text="Find", command=self.clicked_search_btn)
		self.button_search.grid(row=0, column=1)

		self.searchbox_frame.grid_columnconfigure(0, weight=3) # 3/4
		self.searchbox_frame.grid_columnconfigure(1, weight=1) # 1/4

	def show_current_contacts_index_in_listbox(self):
		self.contact_listBox.delete(0, 'end')
		contacts = self.settings.contacts
		for index in self.contacts_index:
			contact = contacts[index]
			for key, value in contact.items():
				full_name = f"{value['f_name']}"
				self.contact_listBox.insert("end", full_name)

	def show_all_contacts_in_listbox(self):
		self.contact_listBox.delete(0, 'end')
		contacts = self.settings.contacts
		self.contacts_index =[]
		index_counter = 0
		for contact in contacts:
			self.contacts_index.append(index_counter)
			index_counter += 1
		for index in self.contacts_index:
			contact = contacts[index]
			for key, value in contact.items():
				full_name = f"{value['f_name']}"
				self.contact_listBox.insert("end", full_name)

	def create_left_content(self):
		frame_w = self.settings.width//3
		frame_h = 4*self.settings.height//5

		self.left_content = tk.Frame(self.left_frame, width=frame_w, height=frame_h, bg="#cc8800")
		self.left_content.pack(fill="x")

		self.contact_listBox = tk.Listbox(self.left_content, bg="#cc8800", fg="white", font=("Arial", 12), height=frame_h)
		self.contact_listBox.pack(side="left", fill="both", expand=True)

		self.contacts_scroll = tk.Scrollbar(self.left_content)
		self.contacts_scroll.pack(side="right", fill="y")

		self.show_all_contacts_in_listbox()

		self.contact_listBox.configure(yscrollcommand=self.contacts_scroll.set)
		self.contacts_scroll.configure(command=self.contact_listBox.yview)

		self.contact_listBox.bind("<<ListboxSelect>>", self.clicked_item_in_Listbox)

	def clicked_item_in_Listbox(self, event):
		if not self.update_mode:
			selection = event.widget.curselection()
			try:
				index_listbox = selection[0]	
			except IndexError:
				index_listbox = self.last_current_contact_index
			index = self.contacts_index[index_listbox]
			self.last_current_contact_index = index
			self.current_contact = self.settings.contacts[index]
			for phoneNumber, info in self.current_contact.items():
				phone = phoneNumber
				full_name = info['f_name']
				tanggal = info['tanggal']
				jam = info['jam']

			self.full_name_label.configure(text=full_name)
			self.table_info[0][1].configure(text=phone)
			self.table_info[1][1].configure(text=tanggal)
			self.table_info[2][1].configure(text=jam)


	def create_right_header(self):
		frame_w = 2*self.settings.width//3
		frame_h = self.settings.height//5

		self.right_header = tk.Frame(self.right_frame, width=frame_w, height=frame_h, bg="#cc8800")
		self.right_header.pack()
		self.create_detail_right_header()

	def create_detail_right_header(self):
		frame_w = 2*self.settings.width//3
		frame_h = self.settings.height//5

		self.detail_header = tk.Frame(self.right_header, width=frame_w, height=frame_h, bg="#cc8800")
		self.detail_header.grid(row=0, column=0, sticky="nsew")

		data = list(self.current_contact.values())[0]
		full_name = f"{data['f_name']}"
		self.virt_img = tk.PhotoImage(width=1, height=1)
		self.full_name_label = tk.Label(self.detail_header, text=full_name, font=("Arial", 30), width=frame_w, height=frame_h, image=self.virt_img, compound="c", bg="#cc8800")
		self.full_name_label.pack()

		self.right_header.grid_columnconfigure(0, weight=1)
		self.right_header.grid_rowconfigure(0, weight=1)

	def create_right_content(self):
		frame_w = 2*self.settings.width//3
		frame_h = 3*(4*self.settings.height//5)//4 

		self.right_content = tk.Frame(self.right_frame, width=frame_w, height=frame_h, bg="#cc8800")
		self.right_content.pack(expand=True)
		self.create_detail_right_content()

	def create_detail_right_content(self):
		frame_w = 2*self.settings.width//3
		frame_h = 3*(4*self.settings.height//5)//4 

		self.detail_content = tk.Frame(self.right_content, width=frame_w, height=frame_h, bg="#cc8800")
		self.detail_content.grid(row=0, column=0, sticky="nsew")

		for phoneNumber, info in self.current_contact.items():
			info = [
				['Nomor Tiket :', phoneNumber],
				['Tanggal :', info['tanggal']],
				['Jam :', info['jam']]
			]

		self.table_info = []

		rows , columns = len(info), len(info[0])
		for row in range(rows):
			aRow = []
			for column in range(columns):
				label = tk.Label(self.detail_content, text=info[row][column], font=("Arial", 12), bg="#cc8800")
				aRow.append(label)
				if column == 0:
					sticky = "e"
				else:
					sticky = "w"
				label.grid(row=row, column=column, sticky=sticky)
			self.table_info.append(aRow)



		self.right_content.grid_columnconfigure(0, weight=1)
		self.right_content.grid_rowconfigure(0, weight=1)


	def create_right_footer(self):
		frame_w = 2*self.settings.width//3
		frame_h = (4*self.settings.height//5)//4 

		self.right_footer = tk.Frame(self.right_frame, width=frame_w, height=frame_h, bg="#cc8800")
		self.right_footer.pack()
		self.create_detail_right_footer()

	def create_detail_right_footer(self):
		frame_w = 2*self.settings.width//3
		frame_h = (4*self.settings.height//5)//4 

		self.detail_footer = tk.Frame(self.right_footer, width=frame_w, height=frame_h, bg="#cc8800")
		self.detail_footer.grid(row=0, column=0, sticky="nsew")

		features = ['Update', 'Delete', 'Add New']
		commands = [self.clicked_update_btn, self.clicked_delete_btn, self.clicked_add_new_btn]
		self.buttons_features = []
		for feature in features:
			button = tk.Button(self.detail_footer, text=feature, bg="#cc8800", fg="white", font=("Arial", 12, "bold"), bd=0) #, command=commands[features.index(feature)]
			button.grid(row=0, column=features.index(feature), sticky="nsew", padx=20, pady=(0, 10))
			self.buttons_features.append(button)

		self.buttons_features[0].configure(command=commands[0])
		self.buttons_features[1].configure(command=commands[1])
		self.buttons_features[2].configure(command=commands[2])

		self.right_footer.grid_columnconfigure(0, weight=1)
		self.right_footer.grid_rowconfigure(0, weight=1)

	def recreate_right_frame_and_listbox(self):

		self.detail_header.destroy()
		self.detail_update_content.destroy()
		self.detail_update_footer.destroy()

		#RECREATE HEADER
		self.create_detail_right_header()

		#RECREATE CONTENT
		self.create_detail_right_content()

		#RECREATE FOOTER
		self.create_detail_right_footer()

		self.contact_listBox.delete(0, 'end')
		self.show_all_contacts_in_listbox()

	def recreate_right_frame_and_listbox_after_delete(self):

		self.detail_header.destroy()
		self.detail_content.destroy()
		self.detail_footer.destroy()

		#RECREATE HEADER
		self.create_detail_right_header()

		#RECREATE CONTENT
		self.create_detail_right_content()

		#RECREATE FOOTER
		self.create_detail_right_footer()

		self.contact_listBox.delete(0, 'end')
		self.show_all_contacts_in_listbox()

	def recreate_right_frame_and_listbox_after_add_new(self):

		self.detail_add_new_header.destroy()
		self.detail_add_new_content.destroy()
		self.detail_add_new_footer.destroy()

		#RECREATE HEADER
		self.create_detail_right_header()

		#RECREATE CONTENT
		self.create_detail_right_content()

		#RECREATE FOOTER
		self.create_detail_right_footer()

		self.contact_listBox.delete(0, 'end')
		self.show_all_contacts_in_listbox()

	def clicked_update_btn(self):
		self.update_mode = True
		frame_w = 2*self.settings.width//3
		frame_h = 3*(4*self.settings.height//5)//4 

		self.detail_content.destroy()
		self.detail_footer.destroy()

		self.detail_update_content = tk.Frame(self.right_content, width=frame_w, height=frame_h, bg="#cc8800")
		self.detail_update_content.grid(row=0, column=0, sticky="nsew")

		for phoneNumber, info in self.current_contact.items():
			info = [
				['Plat :', info['f_name']],
				['Nomor Tiket :', phoneNumber],
				['Tanggal :', info['tanggal']],
				['Jam :', info['jam']]
			]

		self.table_info = []
		self.entry_update_contact_vars = []
		rows , columns = len(info), len(info[0])
		for row in range(rows):
			aRow = []
			for column in range(columns):
				if column == 0:
					label = tk.Label(self.detail_update_content, text=info[row][column], font=("Arial", 12), bg="#cc8800")
					aRow.append(label)
					sticky = "e"
					label.grid(row=row, column=column, sticky=sticky)
				else:
					entryVar = tk.StringVar()
					entry = tk.Entry(self.detail_update_content, font=("Arial", 12), bg="white", textvariable=entryVar)
					entry.insert(0, info[row][column])
					self.entry_update_contact_vars.append(entryVar)
					aRow.append(entry)
					sticky = "w"
					entry.grid(row=row, column=column, sticky=sticky)
				
			self.table_info.append(aRow)


		self.right_content.grid_columnconfigure(0, weight=1)
		self.right_content.grid_rowconfigure(0, weight=1)

		frame_w = 2*self.settings.width//3
		frame_h = (4*self.settings.height//5)//4 

		self.detail_update_footer = tk.Frame(self.right_footer, width=frame_w, height=frame_h, bg="#cc8800")
		self.detail_update_footer.grid(row=0, column=0, sticky="nsew")

		features = ['Save', 'Cancel']
		commands = [self.clicked_save_btn, self.clicked_cancel_btn]
		self.buttons_features = []
		for feature in features:
			index = features.index(feature)
			button = tk.Button(self.detail_update_footer, text=feature, bg="#cc8800", fg="white", font=("Arial", 12, "bold"), bd=0, command=commands[index]) #, command=commands[features.index(feature)]
			button.grid(row=0, column=index, sticky="nsew", padx=20, pady=(0, 10))
			self.buttons_features.append(button)


		self.right_footer.grid_columnconfigure(0, weight=1)
		self.right_footer.grid_rowconfigure(0, weight=1)


	def clicked_delete_btn(self):
		self.update_mode = True

		confirm = messagebox.askyesnocancel("Konfirmasi Tiket", "Apakah anda yakin untuk menghapus Tiket ini ?")
		index = self.last_current_contact_index
		if confirm:
			self.settings.contacts.pop(index)
			self.settings.save_data_to_json()
			self.last_current_contact_index = 0
			self.current_contact = self.settings.contacts[0]

			self.recreate_right_frame_and_listbox_after_delete()


		self.update_mode = False

	def clicked_add_new_btn(self):
		self.update_mode = True

		self.detail_header.destroy()
		self.detail_content.destroy()
		self.detail_footer.destroy()

		frame_w = 2*self.settings.width//3
		frame_h = self.settings.height//5

		self.detail_add_new_header = tk.Frame(self.right_header, width=frame_w, height=frame_h, bg="#cc8800")
		self.detail_add_new_header.grid(row=0, column=0, sticky="nsew")

		self.virt_img = tk.PhotoImage(width=1, height=1)
		self.title_header_label = tk.Label(self.detail_add_new_header, text="Tambah Tiket Baru", font=("Arial", 30), width=frame_w, height=frame_h, image=self.virt_img, compound="c", bg="#cc8800")
		self.title_header_label.pack()

		self.right_header.grid_columnconfigure(0, weight=1)
		self.right_header.grid_rowconfigure(0, weight=1)

		frame_w = 2*self.settings.width//3
		frame_h = 3*(4*self.settings.height//5)//4 

		self.detail_add_new_content = tk.Frame(self.right_content, width=frame_w, height=frame_h, bg="#cc8800")
		self.detail_add_new_content.grid(row=0, column=0, sticky="nsew")

		info = [
			['Plat :', None],
			['Nomor Tiket :', None],
			['Tanggal :', None],
			['Jam :', None]
		]

		self.table_info = []
		self.entry_update_contact_vars = []
		rows , columns = len(info), len(info[0])
		for row in range(rows):
			aRow = []
			for column in range(columns):
				if column == 0:
					label = tk.Label(self.detail_add_new_content, text=info[row][column], font=("Arial", 12), bg="#cc8800")
					aRow.append(label)
					sticky = "e"
					label.grid(row=row, column=column, sticky=sticky)
				else:
					entryVar = tk.StringVar()
					entry = tk.Entry(self.detail_add_new_content, font=("Arial", 12), bg="white", textvariable=entryVar)
					self.entry_update_contact_vars.append(entryVar)
					aRow.append(entry)
					sticky = "w"
					entry.grid(row=row, column=column, sticky=sticky)
				
			self.table_info.append(aRow)


		self.right_content.grid_columnconfigure(0, weight=1)
		self.right_content.grid_rowconfigure(0, weight=1)

		frame_w = 2*self.settings.width//3
		frame_h = (4*self.settings.height//5)//4 

		self.detail_add_new_footer = tk.Frame(self.right_footer, width=frame_w, height=frame_h, bg="#cc8800")
		self.detail_add_new_footer.grid(row=0, column=0, sticky="nsew")

		features = ['Save', 'Cancel']
		commands = [self.clicked_save_add_new_btn, self.clicked_cancel_add_new_btn]
		self.buttons_features = []
		for feature in features:
			index = features.index(feature)
			button = tk.Button(self.detail_add_new_footer, text=feature, bg="#cc8800", fg="white", font=("Arial", 12, "bold"), bd=0, command=commands[index]) #, command=commands[features.index(feature)]
			button.grid(row=0, column=index, sticky="nsew", padx=20, pady=(0, 10))
			self.buttons_features.append(button)


		self.right_footer.grid_columnconfigure(0, weight=1)
		self.right_footer.grid_rowconfigure(0, weight=1)


	def clicked_save_btn(self):
		self.update_mode = False

		confirm = messagebox.askyesnocancel("Konfirmasi Tiket", "Apakah anda yakin untuk meng-update info Tiket ?")

		if confirm:
			f_name = self.entry_update_contact_vars[0].get()
			phone = self.entry_update_contact_vars[1].get()
			tanggal = self.entry_update_contact_vars[2].get()
			jam = self.entry_update_contact_vars[3].get()
			self.settings.contacts[self.last_current_contact_index] = {
				phone : {
					'f_name' : f_name,
					'tanggal' : tanggal,
					'jam' : jam
				}
			}
			self.settings.save_data_to_json()
			self.current_contact = self.settings.contacts[self.last_current_contact_index]

		self.recreate_right_frame_and_listbox()


	def clicked_cancel_btn(self):
		self.update_mode = False

		self.recreate_right_frame_and_listbox()


	def clicked_search_btn(self):
		item_search = self.entry_search_var.get()
		contacts = self.settings.contacts
		self.contacts_index = []
		index_counter = 0
		if item_search:
			for contact in contacts:
				for phoneNumber, info in contact.items():
					if item_search in phoneNumber:
						self.contacts_index.append(index_counter)
					elif item_search in info['f_name']:
						self.contacts_index.append(index_counter)
				index_counter += 1
			self.show_current_contacts_index_in_listbox()
		else:
			self.show_all_contacts_in_listbox()

	def clicked_save_add_new_btn(self):
		self.update_mode = False

		confirm = messagebox.askyesnocancel("Konfirmasi Tiket", "Apakah anda yakin untuk menambah Daftar Tiket ?")

		if confirm:
			f_name = self.entry_update_contact_vars[0].get()
			phone = self.entry_update_contact_vars[1].get()
			tanggal = self.entry_update_contact_vars[2].get()
			jam = self.entry_update_contact_vars[3].get()
			new_contact = {
				phone : {
					'f_name' : f_name,
					'tanggal' : tanggal,
					'jam' : jam
				}
			}
			self.settings.contacts.append(new_contact)
			self.settings.save_data_to_json()
			index = len(self.settings.contacts) - 1
			self.last_current_contact_index = index
			self.current_contact = self.settings.contacts[index]

		self.recreate_right_frame_and_listbox_after_add_new()

	def clicked_cancel_add_new_btn(self):
		self.update_mode = False

		self.recreate_right_frame_and_listbox_after_add_new()




