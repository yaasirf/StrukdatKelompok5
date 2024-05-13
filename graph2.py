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
