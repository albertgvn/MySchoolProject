from json import load, dump
from os import system 
from time import sleep
from getpass import getpass
from datetime import datetime

fileUser = 'phoneUser.json'

fileDaftar = 'phoneData.json'

user = {}

daftar = {}

def abcd():
	global user, daftar

	with open(fileUser) as abc:
		user = load(abc)

	with open(fileDaftar) as abc:
		daftar = load(abc)

	return True

def manusio():
	global user, daftar

	with open(fileUser, "w") as f:
		dump(user, f)

	with open(fileDaftar, 'w') as f:
		dump(daftar, f)

	return True

def useer():
	counter = 1
	name = input("Enter Username : ")
	dtw = getpass("Enter Pass : ")
	data = False
	login = False
	if name in user:
		data = True
		login = (user[name] == dtw)
	else:
		data = False
		login = False

	while not data and not login:
		counter += 1
		if counter > 3:
			return False
		print("Incorrect")
		name = input("Enter Username : ")
		dtw = getpass("Enter Pass : ")
		if name in user:
			data = True
			login = (user[name] == dtw)
		else:
			data = False
			login = False
	else:
		print("Anda Berhasil")
		return True

def pilihan():
	print("Hello, Welcome to Contact Machine ")
	print(".")
	print("look. Lihat kontak yang sudah ditambah")
	print("more. Tambah kontak")
	print("find. Mencari kontak")
	print("delete. Menghapus kontak")
	print("exit. Keluar dari program")

def lihat():
	if len(daftar) > 0:
		no = 1
		for info in daftar:
			print("=======================================================")
			print(f"{no} | {info} | {daftar[info][0]}  |       {daftar[info][1]}")
			no += 1

	else:
		print("Kontak kosong")

def tambah():
	print("Tambah kontak\n")
	time = datetime.now()
	isi = input("User : ")
	number = input("Nomor : ")
	dates = ("%s/%s/%s" % (time.day, time.month, time.year))
	daftar.update({isi:[number,dates]})
	manusio()
	print("Saving...")
	sleep(1.5)
	print("Data Saved.")

def cari():
	print("Mencari kontak\n")
	isi = input("User: ")

	if isi in daftar:
		print(f"{isi}\t | Nomor: {daftar[isi][0]}")
	else:
		print(f"{isi} tidak ada di bag")

def hapus():
	print("Penghapusan Data")
	if len(daftar) > 0:
		for isi in daftar:
			print(f"User \t: {isi}\t")

	pilih = input("Pilih kontak: ")

	if pilih in daftar:
		del daftar[pilih]

		manusio()
		print("Menghapus...")
		sleep(1.5)
		print("Menghapus Selesai")
	else:
		print("Tidak ada")