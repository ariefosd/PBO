class Mahasiswa:
    print ("-----------INPUT----------")
    print ("silahkan masukkan data anda")
    def __init__(self, nim, nama):
        self.nim = input ("NIM: ")
        self.nama = input ("Nama: ")
    def semester(self):
        tahun = input("Sekarang tahun berapa:")
        bulan = int(input("sekarang bulan berapa:"))
        
        xy = int(self.nim[:2])
        xz = int(tahun[-2:])
        if xz - xy >=0:
            if bulan > 6:
                print(self.nama, "kamu berada di semester", xz-xy+5)
            else:
                print(self.nama, "kamu berada di semester", xz-xy+4)
        else:
            print("Di tahun", tahun, self.nama, "kamu belum di perkuliahan")
        

Awaliza = Mahasiswa(" "," ")
Awaliza.semester()
print ("Mahasiswa lain :")
wiwit = Mahasiswa(" "," ")
wiwit.semester ()
