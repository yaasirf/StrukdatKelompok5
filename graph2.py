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
