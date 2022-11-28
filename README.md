# Praktikum6

Repository ini digunakan untuk memenuhi Tugas Bahasa Pemrograman Pertemuan-10

Nama    : Mohamad Irvan Zidni

NIM     : 312210308

Kelas   : TI.22.A.3

## Latihan

1. Pertama buat daftar kontak awal dengan menggunakan dictionar, dengan format key (nama) dan value (nomor telpon)

        //tipe data / variabel dictionary untuk menyimpan data dari dictionary
        dictionary = {'ari':'085267888','dina':'087677776'}
        
        //tipe data / variabel p untuk deklarasi sebagai perintah untuk print agar lebih mudah
        p('Kontak awal')
        p('==============================')
        p('#    nama    |   nomor telepon')
        p('==============================')
        p('#    ari     |   085267888','\n#    dina    |   087677776')

2. Untuk menampilkan kontak pada dictionary gunakan format :

        p(dictionary['ari'])

![Foto](Foto/Tampil%20kontak.png)


3. Untuk menambah kontak baru riko gunakan format :

        dictionary['riko']='087654544'

![Foto](Foto/Tambah%20kontak.png)

4. Untuk mengubah nomor kontak dina dengan nomor baru gunakan format :

        dictionary['dina']='088999776'

![Foto](Foto/Ubah%20nomor.png)

5. Untuk menampilkan semua nama dan nomor gunakan format :

        p(dictionary.keys())

![Foto](Foto/Tampil%20semua%20nama%20dan%20nomor.png)

6. Untuk menampilkan semua data dictionary (daftar nama dan kontak) gunakan format :

        p(dictionary)

![Foto](Foto/Tampil%20semua%20data.png)

7. Untuk menghapus kontak dina gunakan format :

        del dictionary['dina']

![Foto](Foto/Hapus%20kontak%20dina.png)

## Tugas

### Flowchart

Buat flowchart terlebih dahulu untuk memudahkan alur program

![Foto](Foto/Flowchart%20Tugas.png)

### Code

1. Buat dictionary kosong terlebih dahulu

        dataMhs = {}

2. Buat perulangan while-true untuk membuat looping agar program terus berjalan hingga selesai

        def menu():
            print("\n")
            print("====================================================")
            print("      \t\t Program input nilai       ")
            print("====================================================\n")

            x = input("[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar]: ")
            print("\n")

            if x == 'L':
                show()
            elif x == 'T':
                add()
            elif x == 'U':
                update()
            elif x == 'H':
                delete()
            elif x == 'C':
                search()
            elif x == 'K':
                print("==========================================================================")
                print('\n')
                print("> You exit the code                        ")
                print("\n")
                print("==========================================================================")

                exit()

            else:
                print("            KODE YANG ANDA MASUKKAN TIDAK VALID !!!!!!!!!!!")

        while True:
            menu()

3. Buat fungsi untuk memanggil menu

menu tambah data

        def add():
            print("Tambah Data")
            nama = input("Nama\t : ")
            nim = input("NIM\t : ")
            uts = int(input("Nilai UTS\t : "))
            uas = int(input("Nilai UAS\t : "))
            tugas = int(input("Nilai Tugas\t : "))
            akhir = (tugas * 30 / 100) + (uts * 35 / 100) + (uas * 35 / 100)
            mahasiswa[nama] = nim, tugas, uts, uas, akhir

Output : 


menu ubah data

        def update():
            print("Ubah Data")
            nama = input("Masukkan Nama : ")
            if nama in mahasiswa.keys():
                nim = input("NIM\t : ")
                uts = int(input("Nilai UTS\t : "))
                uas = int(input("Nilai UAS\t : "))
                tugas = int(input("Nilai Tugas\t : "))
                akhir = (tugas * 30 / 100) + (uts * 35 / 100) + (uas * 35 / 100)
                mahasiswa[nama] = nim, tugas, uts, uas, akhir

            else:
                print("Nama tidak ditemukan ")

menu cari data

        def search():
            print("Cari Data")
            a = input("Masukkan Nama : ")
            if a in mahasiswa.keys():
                print("===========================================================================")
                print("|      Nama      |     NIM     |  Tugas  |   UTS   |   UAS   |    Akhir   |")
                print("===========================================================================")
                print("| {0:14s} | {1:11s} | {2:7d} | {3:7d} | {4:7d} |     {5:6.2f} |"
                    .format(a, mahasiswa[a][0], mahasiswa[a][1], mahasiswa[a][2], mahasiswa[a][3], mahasiswa[a][4]))
                print("===========================================================================")

            else:
                print("=================================================================================")
                print("| No |      Nama      |     NIM     |  Tugas  |   UTS   |   UAS   |    Akhir    |")
                print("=================================================================================")
                print("|                          DATA TIDAK DITEMUKAN                                 |")
                print("=================================================================================")

menu hapus data

        def delete():
            print("Hapus Data")
            nama = input("Masukkan Nama : ")

            if nama in mahasiswa.keys():
                del mahasiswa[nama]

            else:
                print("Nama tidak ditemukan")

menu lihat data

        def show():
            if mahasiswa.items():
                print("Daftar Nilai")
                print("=================================================================================")
                print("| No |      Nama      |     NIM     |  Tugas  |   UTS   |   UAS   |    Akhir    |")
                print("=================================================================================")
                i = 0
                for a in mahasiswa.items():
                    i += 1
                    print("| {no:2d} | {0:14s} | {1:11s} | {2:7d} | {3:7d} | {4:7d} |      {5:6.2f} |"
                        .format(a[0][: 14], a[1][0], a[1][1], a[1][2], a[1][3], a[1][4], no=i))
                print("=================================================================================")

            else:
                print("Daftar Nilai")
                print("=================================================================================")
                print("| No |      Nama      |     NIM     |  Tugas  |   UTS   |   UAS   |    Akhir    |")
                print("=================================================================================")
                print("|                                TIDAK ADA DATA                                 |")
                print("=================================================================================")