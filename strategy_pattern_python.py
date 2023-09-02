# python3

def latajKos(name):
    print(f"{name} fru")


def latajSupKos(name):
    print(f"{name} supfru")


class Kos:
    def __init__(self, lot):
        self.lot = lot

    def lec(self):
        self.lot

    def zmienLot(self, lot):
        self.lot = lot


# run

kos = Kos(latajKos("Kos"))
kos.lec()
kos.zmienLot(latajSupKos("Sup Kos"))
kos.lec()
