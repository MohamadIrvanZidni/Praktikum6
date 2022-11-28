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