from os import system
from time import sleep
from datetime import datetime
 
def print_menu():
	system("cls")
	print("""
	Penyimpanan Kontak Sederhana
	[1]. Lihat Tiket
	[2]. Menambahkan Tiket
	[3]. Mencari Informasi Tiket
	[4]. Menghapus Tiket
	[5]. Mengupdate Tiket 
	[Q]. Keluar
			""")
 
def print_header(msg):
	system("cls")
	print(msg)
 
def not_empty(container):
	if len(container) != 0:
		return True
	else:
		return False
 
def verify_ans(char):
	if char.upper() == "Y":
		return True
	else:
		return False
 
def print_data(id_ticket=None,Studio=True,Waktu_Tayang=True,Judul_film=True,Harga=True,Nomor_Kursi=True,all_data=False):
	if id_ticket != None and all_data == False:
		print(f"ID : {id_ticket}")
		print(f"NOMOR_PESANAN : {Tickets[id_ticket]['Nomor Pesanan']}")
		print(f"STUDIO : {Tickets[id_ticket]['Studio']}")
		print(f"WAKTU_TAYANG : {Tickets[id_ticket]['Waktu Tayang']}")
		print(f"JUDUL_FILM : {Tickets[id_ticket]['Judul film']}")
		print(f"HARGA : {Tickets[id_ticket]['Harga']}")
		print(f"NOMOR_KURSI : {Tickets[id_ticket]['Nomor Kursi']}")
	elif Waktu_Tayang == False and all_data == False:
		print(f"ID : {id_ticket}")
		print(f"NOMOR_PESANAN : {Tickets[id_ticket]['Nomor Pesanan']}")
		print(f"STUDIO : {Tickets[id_ticket]['Studio']}")
		print(f"JUDUL_FILM : {Tickets[id_ticket]['Judul film']}")
		print(f"HARGA : {Tickets[id_ticket]['Harga']}")
		print(f"NOMOR_KURSI : {Tickets[id_ticket]['Nomor Kursi']}")
	elif all_data == True:
		for id_ticket in Tickets: # lists, string, dict
			Nomor_Pesanan = Tickets[id_ticket]["Nomor Pesanan"]
			Studio = Tickets[id_ticket]["Studio"]
			Waktu_Tayang = Tickets[id_ticket]["Waktu Tayang"]
			Judul_film = Tickets[id_ticket]["Judul film"]
			Harga = Tickets[id_ticket]["Harga"]
			Nomor_Kursi = Tickets[id_ticket]["Nomor Kursi"]
			print(f"ID : {id_ticket} - NOMOR PESANAN : {Nomor_Pesanan} - STUDIO : {Studio} - WAKTU TAYANG : {Waktu_Tayang} - JUDUL FILM : {Judul_film} - HARGA : {Harga} - NOMOR KURSI : {Nomor_Kursi}")
 
def view_ticket():
	print_header("DAFTAR KONTAK TERSIMPAN")
	if not_empty(Tickets):
		print_data(all_data=True)
	else:
		print("MAAF BELUM ADA KONTAK TERSIMPAN")
	input("Tekan ENTER untuk kembali ke MENU")
 
def create_id_ticket(order_number, STUDIO):
	hari_ini = datetime.now()
	tahun = hari_ini.year
	bulan = hari_ini.month
	hari = hari_ini.day
 
	counter = len(Tickets) + 1
	first = order_number[0].upper()
	last_4 = STUDIO[-4:]
 
	id_ticket = ("%04d%02d%02d-C%03d%s%s" % (tahun, bulan, hari, counter, first, last_4))
	return id_ticket
 
 
 
def add_ticket():
	print_header("MENAMBAHKAN KONTAK BARU")
	Nomor_Pesanan = input("NOMOR PESANAN \t: ")
	Studio = input("STUDIO \t: ")
	Waktu_Tayang = input("WAKTU TAYANG \t: ")
	Judul_film = input("JUDUL FILM \t: ")
	Harga = input("HARGA \t: ")
	Nomor_Kursi = input("NOMOR KURSI \t: ")
	respon = input(f"Apakah yakin ingin menyimpan Tiket : {Nomor_Pesanan} ? (Y/N) ")
	if verify_ans(respon):
		id_ticket = create_id_ticket(order_number=Nomor_Pesanan, STUDIO=Studio)
		Tickets[id_ticket] = {
			"Nomor Pesanan" : Nomor_Pesanan,
			"Studio" : Studio,
			"Waktu Tayang" : Waktu_Tayang,
			"Judul film" : Judul_film,
			"Harga" : Harga,
			"Nomor Kursi" : Nomor_Kursi
		}
		print("Tiket Tersimpan.")
	else:
		print("Tiket Batal Disimpan")
	input("Tekan ENTER untuk kembali ke MENU")
 
def searching_by_order_number(Ticket):
	for id_ticket in Tickets:
		if Tickets[id_ticket]['Nomor Pesanan'] == Ticket:
			return id_ticket
	else:
		return False
 
def find_tiket():
	print_header("MENCARI TIKET")
	Nomor_Pesanan = input("Nomor Pesanan Tiket yang Dicari : ")
	exists = searching_by_order_number(Nomor_Pesanan)
	if exists:
		print("Tiket Ditemukan")
		print_data(id_ticket=exists)
	else:
		print("Tiket Tidak Ada")
	input("Tekan ENTER untuk kembali ke MENU")
 
def delete_tiket():
	print_header("MENGHAPUS TIKET")
	Nomor_Pesanan = input("Nama Pesanan Tiket yang akan Dihapus : ")
	exists = searching_by_order_number(Nomor_Pesanan)
	if exists:
		print_data(id_ticket=exists)
		respon = input(f"Yakin ingin menghapus {Nomor_Pesanan} ? (Y/N) ")
		if verify_ans(respon):
			del Tickets[exists]
			print("Data Kontak Telah Dihapus")
		else:
			print("Data Kontak Batal Dihapus")
	else:
		print("Data Tidak Ada")
	input("Tekan ENTER untuk kembali ke MENU")
 
def update_nomor_pesanan(id_ticket):
	print(f"Nomorn Pesanan lama : {Tickets[id_ticket]['Nomor Pesanan']}")
	new_order_number = input("Masukkan Nomor Pesanan Terbaru : ")
	respon = input("Apakah yakin data ingin diubah (Y/N) : ")
	result = verify_ans(respon)
	if result :
		Tickets[id_ticket]['Nomor Pesanan'] = new_order_number
		print("Data Telah di simpan")
		print_data(id_ticket)
	else:
		print("Data Batal diubah")
 
def update_studio(id_ticket):
	print(f"Studio Lama : {Tickets[id_ticket]['Studio']}")
	new_studio = input("Masukkan Studio Terbaru : ")
	respon = input("Apakah yakin data ingin diubah (Y/N) : ")
	result = verify_ans(respon)
	if result :
		Tickets[id_ticket]['Studio'] = new_studio
		print("Data Telah di simpan")
		print_data(id_ticket)
	else:
		print("Data Batal diubah")
 
def update_waktu_tayang(id_ticket):
	print(f"Waktu Tayang lama : {Tickets[id_ticket]['Waktu Tayang']}")
	new_time_show = input("Masukkan Waktu Tayang Terbaru : ")
	respon = input("Apakah yakin data ingin diubah (Y/N) : ")
	result = verify_ans(respon)
	if result :
		Tickets[id_ticket]['Waktu Tayang'] = new_time_show
		print("Data Telah di simpan")
		print_data(id_ticket)
	else:
		print("Data Batal diubah")
 
def update_judul_film(id_ticket):
	print(f"Judul film Lama : {Tickets[id_ticket]['Judul film']}")
	new_film_title = input("Masukkan judul film terbaru : ")
	respon = input("Apakah yakin data ingin diubah (Y/N) : ")
	result = verify_ans(respon)
	if result :
		Tickets[id_ticket]['Judul film'] = new_film_title
		print("Data Telah di simpan")
		print_data(id_ticket)
	else:
		print("Data Batal diubah")

def update_harga(id_ticket):
	print(f"Studio Lama : {Tickets[id_ticket]['Harga']}")
	new_price = input("Masukkan Harga terbaru : ")
	respon = input("Apakah yakin data ingin diubah (Y/N) : ")
	result = verify_ans(respon)
	if result :
		Tickets[id_ticket]['Harga'] = new_price
		print("Data Telah di simpan")
		print_data(id_ticket)
	else:
		print("Data Batal diubah")

def update_nomor_kursi(id_ticket):
	print(f"Studio Lama : {Tickets[id_ticket]['Nomor Kursi']}")
	new_chair_number = input("Masukkan Nomor Kursi Terbaru : ")
	respon = input("Apakah yakin data ingin diubah (Y/N) : ")
	result = verify_ans(respon)
	if result :
		Tickets[id_ticket]['Nomor Kursi'] = new_chair_number
		print("Data Telah di simpan")
		print_data(id_ticket)
	else:
		print("Data Batal diubah")

def update_tiket():
	print_header("MENGUPDATE INFO TIKET")
	Nomor_Pesanan = input("Nomor Pesanan Tiket yang akan di-update : ")
	exists = searching_by_order_number(Nomor_Pesanan)
	if exists:
		print_data(exists)
		print("EDIT FIELD [1] NOMOR PESANAN - [2] STUDIO - [3] WAKTU TAYANG - [4] JUDUL FILM -[5] HARGA - [6] NOMOR KURSI")
		respon = input("MASUKAN PILIHAN (1/2/3/4/5) : ")
		if respon == "1":
			update_nomor_pesanan(exists)
		elif respon == "2":
			update_studio(exists)
		elif respon == "3":
			update_waktu_tayang(exists)
		elif respon == "4":
			update_judul_film(exists)
		elif respon == "5":
			update_harga(exists)
		elif respon == "6":
			update_nomor_kursi(exists)
	else:
		print("Data Tidak Ada")
	input("Tekan ENTER untuk kembali ke MENU")
 
 
def check_user_input(char):
	char = char.upper()
	if char == "Q":
		print("BYE!!!")
		return True
	elif char == "1":
		view_ticket()
	elif char == "2":
		add_ticket()
	elif char == "3":
		find_tiket()
	elif char == "4":
		delete_tiket()
	elif char == "5":
		update_tiket()
	elif char == "6":
		pass
 
Tickets = {
	"20201007-C001A0812" : {
		"Nomor Pesanan" : "1087",
		"Studio" : "3",
		"Waktu Tayang" : "13.00-15.00",
		"Judul film" : "The Banana 2",
		"Harga" : "Rp 50.000",
		"Nomor Kursi" : "5A"
	},
	"20201008-C002B0813" : {
		"Nomor Pesanan" : "1088",
		"Studio" : "3",
		"Waktu Tayang" : "13.00-15.00",
		"Judul film" : "The Banana 2",
		"Harga" : "Rp 50.000",
		"Nomor Kursi" : "5B"
	}
}
#flag/sign/tanda menyimpan sebuah kondisi
stop = False
 
while not stop:
	print_menu()
	user_input = input("Pilihan : ")
	stop = check_user_input(user_input)