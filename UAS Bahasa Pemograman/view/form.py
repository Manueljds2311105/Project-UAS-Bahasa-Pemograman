def input_data():
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
    