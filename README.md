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

            while True:
                c = input("\n(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar: ")

3. Buat percabangan if-else untuk memilih menu

menu tambah data

        if (c.lower() == 't'):
            print('\nTambah Data Mahasiswa Baru')
            nama= input("Masukkan Nama\t\t: ")
            nim= input("Masukkan NIM\t\t: ")
            nilaiTugas= int(input("Masukkan Nilai Tugas\t: "))
            nilaiUts= int(input("Masukkan Nilai UTS\t: "))
            nilaiUas= int(input("Masukkan Nilai UAS\t: "))
            nilaiAkhir= (0.30 * nilaiTugas) + (0.35 * nilaiUts) + (0.35 * nilaiUas)
            dataMhs[nama]= nim, nilaiTugas, nilaiUts, nilaiUas, nilaiAkhir
            print("\nData Berhasil Ditambahkan!")

menu ubah data

        elif (c.lower() == 'u'):
            print('\nMengedit Data Mahasiswa')
            nama = input("Masukkan Nama: ")
            if nama in dataMhs.keys():
                nim= input("Masukkan NIM Baru\t: ")
                nilaiTugas= int(input("Masukkan Nilai Tugas\t: "))
                nilaiUts= int(input("Masukkan Nilai UTS\t: "))
                nilaiUas= int(input("Masukkan Nilai UAS\t: "))
                nilaiAkhir= (0.30 * nilaiTugas) + (0.35 * nilaiUts) + (0.35 * nilaiUas)
                dataMhs[nama] = nim, nilaiTugas, nilaiUts, nilaiUas, nilaiAkhir
                print("\nData Berhasil Di Update!")
            else:
                print("Data tidak ditemukan!")

menu cari data

        elif (c.lower() == 'c'):
            print('\nCari Data Mahasiswa')
            nama = input("Masukan Nama:  ")
            if nama in dataMhs.keys():
                print("\n                   DAFTAR NILAI MAHASISWA                   ")
                print("==============================================================")
                print("|     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
                print("==============================================================")
                print("| {0:12s} | {1:9s} | {2:5} | {3:5} | {4:5} | {5:6} |".format(nama, nim, nilaiTugas, nilaiUts, nilaiUas, nilaiAkhir))
                print("==============================================================")
            else:
                print("Datanya {0} Tidak Ada ".format(nama))

menu hapus data

        elif (c.lower() == 'h'):
            nama = input("Masukkan Nama:  ")
            if nama in dataMhs.keys():
                del dataMhs[nama]
                print("Data Telah dihapus!")
            else:
                print("Data Mahasiswa Tidak Ada".format(nama))

menu lihat data

        elif (c.lower() == 'l'):
            if dataMhs.items():
                print("\n                      DAFTAR NILAI MAHASISWA                    ")
                print("==================================================================")
                print("| No |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
                print("==================================================================")
                i = 0
                for x in dataMhs.items():
                    i += 1
                    print("| {6:2} | {0:12s} | {1:9s} | {2:5} | {3:5} | {4:5} | {5:6} |".format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))
                print("==================================================================")
            else:
                print("\n                      DAFTAR NILAI MAHASISWA                    ")
                print("==================================================================")
                print("| No |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
                print("==================================================================")
                print("|                          TIDAK ADA DATA!                       |")
                print("==================================================================")

menu exit

        elif (c.lower() == 'k'):
            print('\n')
            print(21*'=')
            print("Nama\t: Rini Ariza\nKelas\t: TI.22.A3\nNIM\t: 312210337")
            print(21*'=')
            break