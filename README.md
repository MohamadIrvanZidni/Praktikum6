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

3. Untuk menambah kontak baru riko gunakan format :

        dictionary['riko']='087654544'

4. Untuk mengubah nomor kontak dina dengan nomor baru gunakan format :

        dictionary['dina']='088999776'

5. Untuk menampilkan semua nama gunakan format :

        p(dictionary.keys())

6. Untuk menampilkan semua data dictionary (daftar nama dan kontak) gunakan format :

        p(dictionary)

7. Untuk menghapus kontak dina gunakan format :

        del dictionary['dina']    

## Tugas