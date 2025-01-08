class ViewInputForm:
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