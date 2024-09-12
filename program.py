def menu():
	import os
	os.system("CLS")
	print("     SELAMAT DATANG DI PROGRAM PERDIG")
	print("Pilih daftar menu untuk mengakses program :\n")
	print("[1] Lihat Daftar Buku")
	print("[2] Cari Buku")
	print("[3] Tambah Data Buku")
	print("[4] Ubah Data Buku")
	print("[5] Hapus Data Buku")
	print("[6] Lihat Daftar Peminjam Buku")
	print("[7] Tambah Peminjam Buku")
	print("[8] Hapus Data Peminjam Buku")
	print("[9] Keluar")
	
	kode = int(input("\nMasukkan kode menu yang ingin diakses : "))
	pilihmenu(kode)
#-----------------------------------------------------------------------
def pilihmenu(p):
	if p==1:
		daftarbuku()
	elif p==2:
		caridata()
	elif p==3:
		tambahdata()
	elif p==4:
		ubahdata()
	elif p==5:
		hapusdata()
	elif p==6:
		daftarpeminjam()
	elif p==7:
		tambahpeminjam()
	elif p==8:
		hapuspeminjam()
	elif p==9:
		print("\n[Anda telah keluar dari program]")
	else:
		print("\n[Kode yang anda masukkan tidak valid!]")	
#-----------------------------------------------------------------------
def daftarbuku():
	import os
	os.system("CLS")
	print("\nDaftar buku yang tersedia : ")
	bukadata = open("daftarbuku.txt","r")
	isi = bukadata.readlines()
	isi.sort()
	if len(isi) == 0:
		print("\n[Data tidak tersedia]")
	else :
		i=1
		for data_buku in isi:
			pecah = data_buku.split(",")
			print("\n" + str(i) + ".",end=" ")
			print(pecah[0]+","+ pecah[1]+","+ pecah[2])
			i += 1
	print("\nTekan [ENTER] untuk kembali ke menu")
	bukadata.close()
	input()
	menu()
#-----------------------------------------------------------------------
def caridata():
	import os
	os.system("CLS")
	print("\n          - Pencarian Buku -")
	cari = input("\nMasukkan judul buku yang ingin dicari : ")
	bukadata = open("daftarbuku.txt","r")
	isi = bukadata.readlines()
	isi.sort()
	
	for data_buku in isi:
			pecah = data_buku.split(",")
			if pecah[0] == cari:
				print("\nJudul Buku	: "+pecah[0])
				print("Penulis		: "+pecah[1])
				print("Tahun Terbit	: "+pecah[2])
				
			
	print("\n\nTekan [ENTER] untuk kembali ke menu")
	bukadata.close()
	input()
	menu()
#-----------------------------------------------------------------------
def tambahdata():
	import os
	os.system("CLS")
	print("\n   - Tambah Buku -")
	print("\nMasukkan data buku baru")
	judul = input("Judul Buku	: ")
	penulis = input("Penulis Buku	: ")
	tahun = input("Tahun Terbit	: ")
	bukadata = open("daftarbuku.txt","a")
	bukadata.writelines([judul+","+penulis+","+tahun+ "\n"])
	print("\n[Data Buku Berhasil Ditambahkan]")
	bukadata.close()
	
	print("\nIngin menambahkan buku lagi? (Ya/Tidak)", end=" ")
	tmbhdata = input(" : ")
	if tmbhdata == "ya" or tmbhdata == "Ya":
		tambahdata()
	else :
		print("\nTekan [ENTER] untuk kembali ke menu")
		input()
		menu()
#-----------------------------------------------------------------------
def ubahdata():
	import os
	os.system("CLS")
	print("\n            - Ubah Data Buku -")
	baru = input("\nMasukkan judul buku yang ingin diperbarui : ")
	print("\nMasukkan data baru")
	judulbr = input("Judul Buku	: ")
	penulisbr = input("Penulis Buku	: ")
	tahunbr = input("Tahun Terbit	: ")
	bukadata = open("daftarbuku.txt")
	isi = bukadata.readlines()
	
	i=0
	for data_buku in isi:
			pecah = data_buku.split(",")
			if pecah[0] == baru:
				pecah[0] = judulbr
				pecah[1] = penulisbr
				pecah[2] = tahunbr+"\n"
				xg = ",".join(pecah)
				isi[i]=xg
			i += 1
			
	bukadata = open("daftarbuku.txt","w")
	isi = bukadata.writelines(isi)
	print("\n[Data Buku Berhasil Diubah]")
	bukadata.close()
	print("\nIngin mengubah data buku lagi? (Ya/Tidak)", end=" ")
	ubhdata = input(" : ")
	if ubhdata == "ya" or ubhdata == "Ya":
		ubahdata()
	else :
		print("\nTekan [ENTER] untuk kembali ke menu")
		input()
		menu()
#-----------------------------------------------------------------------
def hapusdata() :
	import os
	os.system("CLS")
	print("\n        - Hapus Data Buku -")
	bukadata = open("daftarbuku.txt")
	output = []
	str = input("\nMasukkan judul buku yang ingin dihapus : ")
	for hps in bukadata:
		if not hps.startswith(str):
			output.append(hps)
			
	bukadata = open("daftarbuku.txt.","w")
	bukadata.writelines(output)
	print("\n[Data Buku Telah Terhapus]")
	bukadata.close()
	print("\nIngin menghapus data buku lagi? (Ya/Tidak)", end=" ")
	hpsdata = input(" : ")
	if hpsdata == "ya" or hpsdata == "Ya":
		hapusdata()
	else :
		print("\nTekan [ENTER] untuk kembali ke menu")
		input()
		menu()
#-----------------------------------------------------------------------
def daftarpeminjam():
	import os
	os.system("CLS")
	print("\n\t- Daftar Peminjam Buku -")
	bukadata = open("daftarpeminjam.txt","r")
	isi = bukadata.readlines()
	isi.sort()
	if len(isi) == 0:
		print("\n[Data tidak tersedia]")
	else :
		print("\n=========================================")
		print("NO | NAMA | JUDUL BUKU | TGL.PEMINJAMAN |")
		print("=========================================")
		i=1
		for data_buku in isi:
			pecah = data_buku.split(",")
			print("\n" + str(i) + ".",end=" ")
			print("| "+pecah[0]+" | "+ pecah[1]+" | "+ pecah[2])
			i += 1
	print("\nTekan [ENTER] untuk kembali ke menu")
	bukadata.close()
	input()
	menu()
#-----------------------------------------------------------------------
def tambahpeminjam():
	import os
	os.system("CLS")
	print("\n   - Tambah Peminjam Buku -")
	print("\nMasukkan data peminjam buku")
	nama = input("Nama		   : ")
	judul = input("Judul Buku	   : ")
	tanggal = input("Tanggal Peminjaman : ")
	bukadata = open("daftarpeminjam.txt","a")
	bukadata.writelines([nama+","+judul+","+tanggal+ "\n"])
	print("\n[Data Buku Berhasil Ditambahkan]")
	bukadata.close()
	
	print("\nIngin menambahkan data peminjam lagi? (Ya/Tidak)", end=" ")
	tmbhpeminjam = input(" : ")
	if tmbhpeminjam == "ya" or tmbhpeminjam == "Ya":
		tambahpeminjam()
	else :
		print("\nTekan [ENTER] untuk kembali ke menu")
		input()
		menu()
#-----------------------------------------------------------------------
def hapuspeminjam():
	import os
	os.system("CLS")
	print("\n        - Hapus Data Peminjam Buku -")
	bukadata = open("daftarpeminjam.txt")
	output = []
	str = input("\nMasukkan Nama Peminjam yang Ingin Dihapus : ")
	for hps in bukadata:
		if not hps.startswith(str):
			output.append(hps)
			
	bukadata = open("daftarpeminjam.txt.","w")
	bukadata.writelines(output)
	print("\n[Data Peminjam Telah Terhapus]")
	bukadata.close()
	print("\nIngin menghapus data peminjam lagi? (Ya/Tidak)", end=" ")
	hpspeminjam = input(" : ")
	if hpspeminjam == "ya" or hpspeminjam == "Ya":
		hapuspeminjam()
	else :
		print("\nTekan [ENTER] untuk kembali ke menu")
		input()
		menu()
