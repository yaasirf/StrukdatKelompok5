class Peta:
    def __init__(self):
        self.listKota = {}

    def printPeta(self):
        for kota in self.listKota:
            print(kota, ":", self.listKota[kota])

    def tambahkanKota(self, kota):
        if kota not in self.listKota:
            self.listKota[kota] = {}
            return True
        return False

    def hapusKota(self, hapusKota):
        if hapusKota in self.listKota:
            for kotaLain in self.listKota:
                if hapusKota in self.listKota[kotaLain]:
                    del self.listKota[kotaLain][hapusKota]
            del self.listKota[hapusKota]
            return True
        return False

    def tambahkanJalan(self, kota1, kota2, jarak):
        if kota1 in self.listKota and kota2 in self.listKota:
            self.listKota[kota2][kota1] = jarak, 'KM'
            self.listKota[kota1][kota2] = jarak, 'KM'
            return True
        return False

def hapusJalan(self, kota1, kota2):
        if kota1 in self.listKota and kota2 in self.listKota:
            if kota1 in self.listKota[kota2]:
                del self.listKota[kota2][kota1]
            if kota2 in self.listKota[kota1]:
                del self.listKota[kota1][kota2]
            return True
        return False

    def dijkstra(self, source):
        jarak = {kota: float('inf') for kota in self.listKota}
        jarak[source] = 0

        unvisitedCities = list(self.listKota.keys())
        while unvisitedCities:
            minJarak = float('inf')
            dekatKota = None
  for kota in unvisitedCities:
                if jarak[kota] < minJarak:
                    minJarak = jarak[kota]
                    dekatKota = kota
            unvisitedCities.remove(dekatKota)

            for neighbor, weight in self.listKota[dekatKota].items():
                jarakNeighbor = jarak[dekatKota] + weight[0]
                if jarakNeighbor < jarak[neighbor]:
                    jarak[neighbor] = jarakNeighbor

        return jarak

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
print("Jalan yang terhubung")
petaJawaTimur = Peta()
petaJawaTimur.tambahkanKota("Surabaya")
petaJawaTimur.tambahkanKota("Malang")
petaJawaTimur.tambahkanKota("Sidoarjo")
petaJawaTimur.tambahkanKota("Kediri")
petaJawaTimur.tambahkanKota("Mojokerto")
petaJawaTimur.tambahkanKota("Jember")
petaJawaTimur.tambahkanKota("Bangkalan")
petaJawaTimur.tambahkanKota("Blitar")
petaJawaTimur.tambahkanKota("Probolinggo")
petaJawaTimur.tambahkanKota("Pasuruan")
petaJawaTimur.tambahkanKota("Lamongan")
petaJawaTimur.tambahkanKota("Gresik")
petaJawaTimur.tambahkanKota("Tuban")
petaJawaTimur.tambahkanKota("Bojonegoro")
petaJawaTimur.tambahkanKota("Sampang")

edges = [
    ("Surabaya", "Sidoarjo", 20),
    ("Surabaya", "Mojokerto", 40),
    ("Surabaya", "Malang", 80),
    ("Malang", "Blitar", 30),
    ("Malang", "Pasuruan", 50),
    ("Sidoarjo", "Gresik", 15),
    ("Sidoarjo", "Bangkalan", 10),
    ("Kediri", "Blitar", 35),
    ("Kediri", "Jember", 90),
    ("Kediri", "Gresik", 60),
    ("Mojokerto", "Lamongan", 45),
    ("Mojokerto", "Jember", 85),
    ("Jember", "Pasuruan", 70),
    ("Bangkalan", "Gresik", 25),
    ("Bangkalan", "Blitar", 55),
    ("Surabaya", "Lamongan", 55),
    ("Probolinggo", "Jember", 75),
    ("Kediri", "Malang", 45),
    ("Probolinggo", "Pasuruan", 60),
    ("Lamongan", "Gresik", 20),
    ("Probolinggo", "Bangkalan", 35),
    ("Surabaya", "Bangkalan", 25),
    ("Surabaya", "Sampang", 40),
    ("Bojonegoro", "Tuban", 50),
    ("Lamongan", "Bojonegoro", 55),
    ("Tuban", "Lamongan", 30),
    ("Gresik", "Tuban", 40),
    ("Sampang", "Bangkalan", 45),
    ("Bojonegoro", "Mojokerto", 65),
    ("Bojonegoro", "Kediri", 60)
]

for edge in edges:
    petaJawaTimur.tambahkanJalan(edge[0], edge[1], edge[2])

petaJawaTimur.printPeta()
print('-----------------')

jarakSemuaKota = petaJawaTimur.dijkstra("Surabaya")
print("Jarak Kota Berikut Nya dari Surabaya")
for kota, jarak in jarakSemuaKota.items():
    print(kota, "adalah", jarak, "KM")
