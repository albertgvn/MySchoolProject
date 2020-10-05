from json import load, dump
from os import system 
from time import sleep

import phoneFeature

status = phoneFeature.abcd()

system("cls")

#ini Toko Roti

if status :
	#print()
	dtw = phoneFeature.useer()
	if dtw:
		print("Selamat datang")
		sleep(1.99)
		system("cls")
		opsi = ""
		
		while opsi != "exit":
			system("cls")
			phoneFeature.pilihan()
			opsi = input("Pilih command dibawah ini : ").lower()

			if opsi == "look":
				system("cls")
				print("No | Nama   |     Nomor     |     Tanggal Regristrasi")
				phoneFeature.lihat()
				input("ENTER TO EXIT")

			elif opsi == "more":
				phoneFeature.tambah()
				input("ENTER TO EXIT")

			elif opsi == "find":
				phoneFeature.cari()
				input("ENTER TO EXIT")

			elif opsi == "delete":
				phoneFeature.hapus()
				input("ENTER TO EXIT")

			elif opsi == "exit":
				break

			else:
				print("Input command yang Benar!")
				input("ENTER untuk keluar")





	else:
		print("Anda gagal")
else:
	print("Ini Rusak")