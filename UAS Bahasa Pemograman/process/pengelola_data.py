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