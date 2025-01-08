# Project UAS
## Konsep Modular Dan OOP

Nama: Manuel Johansen Dolok Saribu

Kelas: Ti.24.A5

Nim: 312410493

Dosen Pengampu: Agung Nugroho, S.Kom., M.Kom.

Mata Kuliah: Bahasa Pemograman

### Link Video Youtube
https://www.youtube.com/watch?si=J06UW7cVw4TLdvwD&v=iYgHP3Nvr6I&feature=youtu.be
### 1. Class Mahasiswa
```python
class Mahasiswa:
```
- class adalah kata kunci untuk mendefinisikan sebuah blueprint (kerangka) objek di Python.
- Class Mahasiswa merepresentasikan data dan fungsi yang berhubungan dengan seorang mahasiswa, seperti atribut data (nama, nim, tugas, uts, uas) dan fungsi untuk menghitung nilai akhir.

### Konstruktor __init__

```python
def __init__(self, nama, nim, tugas, uts, uas):
    self.nama = nama
    self.nim = nim
    self.tugas = tugas
    self.uts = uts
    self.uas = uas
```
- Konstruktor __init__ adalah metode khusus yang dipanggil secara otomatis saat objek baru dari class ini dibuat.
- Parameter:
  - nama : Nama mahasiswa (tipe data string).
  - nim : Nomor Induk Mahasiswa (tipe data string/integer).
  - tugas : Nilai tugas mahasiswa (tipe data angka, seperti float atau int).
  - uts : Nilai Ujian Tengah Semester (tipe data angka).
  - uas : Nilai Ujian Akhir Semester (tipe data angka).
- self: Referensi ke instance objek yang sedang dibuat. Melalui self, atribut seperti self.nama dapat diakses dan dimodifikasi.
- Konstruktor ini menginisialisasi atribut berikut:
  - self.nama: Menyimpan nama mahasiswa.
  - self.nim: Menyimpan nomor induk mahasiswa.
  - self.tugas: Menyimpan nilai tugas mahasiswa.
  - self.uts: Menyimpan nilai UTS mahasiswa.
  - self.uas: Menyimpan nilai UAS mahasiswa.

### Fungsi input_data
Fungsi ini bertujuan untuk meminta data dari pengguna berupa nama, NIM, nilai tugas, nilai UTS, dan nilai UAS. Data tersebut kemudian dikembalikan dalam bentuk tuple. Fungsi ini juga menangani kesalahan jika input nilai tidak berupa angka.

```python
def input_data():
```
- def: Kata kunci untuk mendefinisikan sebuah fungsi.
- input_data: Nama fungsi yang mendeskripsikan tujuannya, yaitu untuk menerima input data.

```python
try:
        nama = input("Masukkan Nama: ")
        nim = input("Masukkan Nim: ")
        tugas = float(input("Masukkan Nilai Tugas: "))
        uts = float(input("Masukkan Nilai UTS: "))
        uas = float(input("Masukkan NIlai UAS: "))
        return nama, nim, tugas, uts, uas
    except ValueError:
        print("input nilai harus berupa angka")
        return None
```
- Tujuan: Untuk mencoba menjalankan kode yang mungkin menghasilkan kesalahan, yaitu konversi input nilai menjadi float.
- input() meminta pengguna memasukkan data berupa string.
- float() mengonversi input string menjadi tipe data angka pecahan (desimal).
- Jika pengguna memasukkan data yang tidak dapat dikonversi ke float (misalnya huruf atau simbol), maka akan terjadi exception ValueError.
- ```python
  return nama, nim, tugas, uts, uas
  ```
  - Fungsi ini mengembalikan tuple berisi semua data yang dimasukkan: (nama, nim, tugas, uts, uas).
- Fungsi None untuk menunjukkan bahwa data tidak valid dan input gagal diproses.

### 2. class ViewInputForm
- class: Kata kunci untuk mendeklarasikan sebuah class.
- ViewInputForm: Nama class yang mencerminkan bahwa fungsinya adalah menampilkan data dalam bentuk tabel.
```python
      def tampilkan_tabel(data):
            if data:
                print("\nDaftar Mahasiswa")
                print("=" * 65)
                print("| No |      Nama      |    NIM    | Tugas | UTS | UAS |  Akhir  |")
                print("=" * 65)
                for idx, mahasiswa in enumerate(data, start=1):
                    print(f"| {idx:<2} | {mahasiswa.nama:<14} | {mahasiswa.nim:<8} | {mahasiswa.tugas:<5.0f} | {mahasiswa.uts:<3.0f} | {mahasiswa.uas:<3.0f} | {mahasiswa.hitung_nilai_akhir():<7.2f} |")
                print("=" * 65)
            else:
                print("\nTidak ada data mahasiswa yang ditampilkan.")
```
- def tampilkan_tabel: Nama metode yang bertugas untuk menampilkan tabel data.
- data: Parameter yang berisi daftar objek mahasiswa (biasanya dikembalikan oleh semua_data dari class PengelolaData).
- if data: Mengecek apakah parameter data berisi daftar mahasiswa (tidak kosong).
- Jika tidak ada data (data kosong), pesan "Tidak ada data mahasiswa yang ditampilkan." akan dicetak.
- Daftar Mahasiswa: Judul tabel.
- Baris Pembatas (=): Panjangnya diatur agar sesuai dengan lebar tabel.
- Header Kolom:
  - Kolom mencakup No, Nama, NIM, Tugas, UTS, UAS, dan Akhir.
  - Akhir adalah nilai akhir yang dihitung menggunakan metode hitung_nilai_akhir pada class Mahasiswa.
- Looping dengan Enumerasi:
  - for idx, mahasiswa in enumerate(data, start=1):
- Format Tabel: Menggunakan f-string untuk mencetak data dengan format tertentu.
### 3. class PengelolaData:
```python
class PengelolaData:
    def __init__(self):
        self.data_mahasiswa = []

    def tambah_data(self, mahasiswa):
        self.data_mahasiswa.append(mahasiswa)

    def hapus_data(self, nama):
        for mahasiswa in self.data_mahasiswa:
            if mahasiswa.nama == nama:
                self.data_mahasiswa.remove(mahasiswa)
                return True
        return False

    def ubah_data(self, nama, mahasiswa_baru):
        for idx, mahasiswa in enumerate(self.data_mahasiswa):
            if mahasiswa.nama == nama:
                self.data_mahasiswa[idx] = mahasiswa_baru
                return True
        return False

    def semua_data(self):
        return self.data_mahasiswa
```
1. __init__:
  - Konstruktor yang membuat atribut data_mahasiswa, sebuah list kosong untuk menyimpan data mahasiswa.
2. tambah_data(mahasiswa):
  - Menambahkan objek mahasiswa ke dalam list data_mahasiswa.
3. hapus_data(nama):
  - Mencari mahasiswa berdasarkan nama dan menghapusnya dari list.
  - Mengembalikan True jika berhasil, False jika tidak ditemukan.
4. ubah_data(nama, mahasiswa_baru):
  - Mencari mahasiswa berdasarkan nama, lalu mengganti data mahasiswa lama dengan data baru (mahasiswa_baru).
  - Mengembalikan True jika berhasil, False jika tidak ditemukan.
5. semua_data():
  - Mengembalikan seluruh data mahasiswa dalam bentuk list.

### Main.py
```python
from data.mahasiswa import Mahasiswa
from view.form import input_data
from view.tabel_view import ViewInputForm
from process.pengelola_data import PengelolaData


def main():
    pengelola = PengelolaData()

    while True:
        print("\nMenu: [Lihat (L), Tambah (T), Ubah (U), Hapus (H), Keluar (K)]")
        pilihan = input("Pilih menu: ").lower()

        if pilihan == 'l':
            ViewInputForm.tampilkan_tabel(pengelola.semua_data())
        elif pilihan == 't':
            data = input_data()
            if data:
                nama, nim, tugas, uts, uas = data
                mahasiswa = Mahasiswa(nama, nim, tugas, uts, uas)
                pengelola.tambah_data(mahasiswa)
                print("Data berhasil ditambahkan!")
        elif pilihan == 'u':
            nama = input("Masukkan Nama yang ingin diubah: ")
            data = input_data()
            if data:
                nama_baru, nim, tugas, uts, uas = data
                mahasiswa_baru = Mahasiswa(nama_baru, nim, tugas, uts, uas)
                if pengelola.ubah_data(nama, mahasiswa_baru):
                    print("Data berhasil diubah!")
                else:
                    print("Data tidak ditemukan!")
        elif pilihan == 'h':
            nama = input("Masukkan Nama yang ingin dihapus: ")
            if pengelola.hapus_data(nama):
                print("Data berhasil dihapus!")
            else:
                print("Data tidak ditemukan!")
        elif pilihan == 'k':
            print("Keluar dari program...")
            break
        else:
            print("Pilihan tidak valid, silakan pilih menu yang tersedia.")

if __name__ == "__main__":
    main()
```
1. Import Modules:
   - Mengimpor class dan fungsi dari modul data, view, dan process untuk memisahkan logika program berdasarkan fungsionalitas.
2. main():
   - Fungsi utama untuk menjalankan program dengan antarmuka menu berbasis teks.
3. pengelola = PengelolaData():
   - Membuat instance dari class PengelolaData untuk mengelola data mahasiswa.
4. Menu Utama:
   - Lihat (L): Menampilkan data mahasiswa menggunakan ViewInputForm.tampilkan_tabel().
   - Tambah (T): Menambahkan data mahasiswa baru menggunakan fungsi input_data() dan menyimpannya ke PengelolaData.
   - Ubah (U): Mengubah data mahasiswa yang sudah ada berdasarkan nama.
   - Hapus (H): Menghapus data mahasiswa berdasarkan nama.
   - Keluar (K): Mengakhiri program.
5. Input Validasi:
   - Jika input tidak sesuai (menu tidak valid), program akan meminta input ulang.

### Hasil Kode Program
![foto](https://github.com/Manueljds2311105/foto/blob/f72f88bfde8a931077554041fd967b08669e241e/main.py%20-%20UAS%20Bahasa%20Pemograman%20-%20Visual%20Studio%20Code%20%5BAdministrator%5D%201_8_2025%208_43_38%20AM.png)
![foto](https://github.com/Manueljds2311105/foto/blob/f72f88bfde8a931077554041fd967b08669e241e/main.py%20-%20UAS%20Bahasa%20Pemograman%20-%20Visual%20Studio%20Code%20%5BAdministrator%5D%201_8_2025%208_44_38%20AM.png)
