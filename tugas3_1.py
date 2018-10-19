class Orang:
    nama = None
    
    def __init__(self, nama):
        self.nama = nama
    
    def info(self):
        print("Orang")
        print("-------------")
        print("Nama      : ", self.nama)
        print("")

class Mahasiswa(Orang):
    npm = None
    
    def __init__(self, nama, npm, semester):
        Orang.__init__(self, nama)
        self.npm = npm
        self.semester = semester
    
    def info(self):
        print("Mahasiswa")
        print("-------------")
        print("Nama      : ", self.nama)
        print("NPM       : ", self.npm)
        print("Semester  : ", self.semester)
        print("")

class Pegawai(Orang):
    nip = None
    
    def __init__(self, nama, nip):
        Orang.__init__(self, nama)
        self.nip = nip
    
    def info(self):
        print("Pegawai")
        print("-------------")
        print("Nama      : ", self.nama)
        print("NIP       : ", self.nip)
        print("")

class Dosen(Pegawai):
    nidn = None
    
    def __init__(self, nama, nip, nidn):
        Pegawai.__init__(self, nama, nip)
        self.nidn = nidn
    
    def info(self):
        print("Dosen")
        print("-------------")
        print("Nama      : ", self.nama)
        print("NIP       : ", self.nip)
        print("NIDN      : ", self.nidn)
        print("")

class Karyawan(Pegawai):
    def __init__(self, nama, nip):
        Pegawai.__init__(self, nama, nip)
    
    def info(self):
        print("Karyawan")
        print("-------------")
        print("Nama      : ", self.nama)
        print("NIP       : ", self.nip)
        print("")

mahasiswa1 = Mahasiswa("Arief Wicaksono", "140411100008", "8")
mahasiswa1.info()

mahasiswa2 = Mahasiswa("Mohammad Awaliza", "140411100004", "7")
mahasiswa2.info()

karyawan1 = Karyawan("Hendro", "7830492827")
karyawan1.info()
