class Peta:
  def __init__(self):
    self.cityList = {}

  def printPeta(self):
    for kota in self.cityList:
      print(kota + ":", self.cityList[kota])

  def tambahkanKota(self, kota):
    if kota not in self.cityList:
      self.cityList[kota] = []
      return True
    return False

  def hapusKota(self, kotaDihapus):
    #cek apakah kota yang ingin dihapus ada di list
    if kotaDihapus in self.cityList:
      for kotalain in self.cityList:
    #cek apakah kota yang ingin dihapus ada jalannya ke kotalain
        if kotaDihapus in self.cityList[kotalain]:
          self.cityList[kotalain].remove(kotaDihapus)
      del self.cityList[kotaDihapus]
      return True
    return False

  def tambahkanJalan(self, kota1, kota2):
    if kota1 in self.cityList and kota2 in self.cityList:
    #masukkan kota 1 di list kota2
      self.cityList[kota2].append(kota1)
    #masukkan kota 2 di list kota1
      self.cityList[kota1].append(kota2)
      return True
    return False

def hapusJalan(self, kota1, kota2):
    if kota1 in self.cityList and kota2 in self.cityList:
      self.cityList[kota2].remove(kota1)
    #hapus kota 1 di list kota2
      self.cityList[kota1].remove(kota2)
    #hapus kota 2 di list kota1
      return True
    return False

# Inisiasi objek peta Jawa Timur
petaJawaTimur = Peta()

# Tambahkan kota-kota di Jawa Timur
kotaJawaTimur = [
  "Surabaya",
  "Malang",
  "Sidoarjo",
  "Kediri",
  "Mojokerto",
  "Jember",
  "Bangkalan",
  "Blitar",
  "Probolinggo",
  "Pasuruan",
  "Lamongan",
  "Gresik",
  "Tuban",
  "Bojonegoro",
  "Sampang"
]

for kota in kotaJawaTimur:
  petaJawaTimur.tambahkanKota(kota)

# Tambahkan jalan-jalan di Jawa Timur
petaJawaTimur.tambahkanJalan("Surabaya", "Sidoarjo")
petaJawaTimur.tambahkanJalan("Surabaya", "Mojokerto")
petaJawaTimur.tambahkanJalan("Surabaya", "Malang")
petaJawaTimur.tambahkanJalan("Malang", "Blitar")
petaJawaTimur.tambahkanJalan("Malang", "Pasuruan")
petaJawaTimur.tambahkanJalan("Sidoarjo", "Gresik")
petaJawaTimur.tambahkanJalan("Sidoarjo", "Bangkalan")
petaJawaTimur.tambahkanJalan("Kediri", "Blitar")
petaJawaTimur.tambahkanJalan("Kediri", "Jember")
petaJawaTimur.tambahkanJalan("Kediri", "Gresik")
petaJawaTimur.tambahkanJalan("Mojokerto", "Lamongan")
petaJawaTimur.tambahkanJalan("Mojokerto", "Jember")
petaJawaTimur.tambahkanJalan("Jember", "Pasuruan")
petaJawaTimur.tambahkanJalan("Bangkalan", "Gresik")
petaJawaTimur.tambahkanJalan("Bangkalan", "Blitar")
petaJawaTimur.tambahkanJalan("Surabaya", "Lamongan")
petaJawaTimur.tambahkanJalan("Probolinggo", "Jember")
petaJawaTimur.tambahkanJalan("Kediri", "Malang")
petaJawaTimur.tambahkanJalan("Probolinggo", "Pasuruan")
petaJawaTimur.tambahkanJalan("Lamongan", "Gresik")
petaJawaTimur.tambahkanJalan("Probolinggo", "Bangkalan")
petaJawaTimur.tambahkanJalan("Surabaya", "Bangkalan")
petaJawaTimur.tambahkanJalan("Surabaya", "Sampang")
petaJawaTimur.tambahkanJalan("Bojonegoro", "Tuban")
petaJawaTimur.tambahkanJalan("Lamongan", "Bojonegoro")
petaJawaTimur.tambahkanJalan("Tuban", "Lamongan")
petaJawaTimur.tambahkanJalan("Gresik", "Tuban")
petaJawaTimur.tambahkanJalan("Sampang", "Bangkalan")
petaJawaTimur.tambahkanJalan("Bojonegoro", "Mojokerto")
petaJawaTimur.tambahkanJalan("Bojonegoro", "Kediri")


# Tampilkan peta awal
petaJawaTimur.printPeta()
print('------------------------------')

# Hapus kota Bangkalan
petaJawaTimur.hapusKota("Bangkalan")

# Tampilkan peta setelah Bangkalan dihapus
petaJawaTimur.printPeta()



