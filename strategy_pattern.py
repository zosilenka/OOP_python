# python3

from abc import ABC, abstractmethod


class Kos:
    def __init__(self, metlot):
        self.metlot = metlot

    def lec(self):
        self.metlot.lataj()

    def zmienlot(self, metlot):
        self.metlot = metlot


class Lot(ABC):
    @abstractmethod
    def lataj(self):
        pass


class KosLot(Lot):
    def lataj(self):
        print("fruuu")


class SupKosLot(Lot):
    def lataj(self):
        print("supfru")


# run

kos = Kos(SupKosLot())
kos.lec()
kos.zmienlot(KosLot())
kos.lec()