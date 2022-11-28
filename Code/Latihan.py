daftarKontak = {"Nama":"Nomer Telpon"}
kontak       = {'Irpan':'081382330718', 'Zidni' : '085695783122', 'Panpane' : '081375927575'}

#print
print(30*"═")
print("    Nama    |  Nomor Telepon  ") #print daftarkontak
print(30*"-")
print("   # Irpan    | ", kontak['Irpan']) #print kontak Ayubi
print("   # Zidni   | ", kontak['Zidni']) #print kontak Andi
print("   # Panpane   | ", kontak['Panpane']) #print kontak Andi
print(30*"═")

#Tampilkan kontaknya Ayubi
print("Tampilkan kontaknya Ayubi")
print("    Irpan     | ", kontak['Irpan']) #print kontak Ayubi
print(30*"═")
#Tambah kontak baru dengan nama Albed, nomor 081212273539
print("Tambah kontak baru dengan nama Albed, nomor 081212273539")
kontak['Zidni'] = '081212273539'
print("    Zidni    | ", kontak['Zidni'])
print(30*"═")

#Ubah kontak Andi dengan nomor baru 0876780147825
print("Ubah kontak Andi dengan nomor baru 0876780147825")
kontak['Panpane'] = '0876780147825'
print("    Panpane    | ", kontak['Panpane'])
print(30*"═")

#Tampilkan semua Nama
print("Tampilkan semua Nama")
print(kontak.keys())
print(30*"═")

#Tampilkan semua Nomor
print("Tampilkan semua Nomor")
print(kontak.values())
print(30*"═")

#Tampilkan daftar Nama dan nomornya
print("Tampilkan daftar Nama dan nomornya")
print(kontak.items())
print(30*"═")

#MengHapus kontak Andi
print("Hapus kontak Panpane")
kontak.pop('Panpane')
print(kontak.items())
print(30*"═")