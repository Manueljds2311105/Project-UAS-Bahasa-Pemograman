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