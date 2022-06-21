class Pkw:
    def __init__(self, max_reifen):
        self.__motor = None
        self.__fahrgestell = None
        self.__reifen = []
        self.__max_reifen = max_reifen

    def set_motor(self, motor):
        self.__motor = motor

    def set_fahrgestell(self, fahrgestell):
        self.__fahrgestell = fahrgestell

    def add_reifen(self, reifen, reifen_position=-1):
        if reifen_position == -1:
            if len(self.__reifen) < self.__max_reifen and self.__max_reifen > 0:
                self.__reifen.append(reifen)
        else:
            if reifen_position <= self.__max_reifen:
                self.__reifen.insert(reifen_position, reifen)

    def reset_reifen(self):
        self.__reifen = []

    def drop_reifen(self, reifen_position):
        if reifen_position <= self.__max_reifen:
            self.__reifen.pop(reifen_position)

    def get_motor(self):
        return self.__motor

    def get_fahrgestell(self):
        return self.__fahrgestell

    def get_reifen(self):
        return self.__reifen

    def get_max_reifen(self):
        return self.__max_reifen

    def get_reifen_anzahl(self):
        return len(self.__reifen)

    def set_max_reifen(self, max_reifen):
        self.__max_reifen = max_reifen


class Reifen:
    def __init__(self, zoll, profiltiefe):
        self.__zoll = zoll
        self.__profiltiefe = profiltiefe

    def get_zoll(self):
        return self.__zoll

    def get_profiltiefe(self):
        return self.__profiltiefe

    def set_profiltiefe(self, profiltiefe):
        self.__profiltiefe = profiltiefe


class Fahrgestell:
    def __init__(self):
        self.__doors = 0

    def get_doors(self):
        return self.__doors


class Motor:
    def __init__(self, power, ccm):
        self.__power = power
        self.__ccm = ccm
        self.__gelaufene_kilometer = 0

    def get_power(self):
        return self.__power

    def get_ccm(self):
        return self.__ccm

    def get_gelaufene_kilometer(self):
        return self.__gelaufene_kilometer

    def set_gelaufene_kilometer(self, gelaufene_kilometer):
        if gelaufene_kilometer > self.__gelaufene_kilometer:
            self.__gelaufene_kilometer = gelaufene_kilometer
        else:
            print(f"Gelaufene Kilometer dürfen nicht unter {self.__gelaufene_kilometer} sein!")


class Fahrzeughalter:
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__pkws = []

    def add_pkw(self, pkw):
        self.__pkws.append(pkw)

    def get_pkws(self):
        return self.__pkws

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_pkw_anzahl(self):
        return len(self.__pkws)

    def get_pkw_by_index(self, index):
        return self.__pkws[index]

    def add_pkw_by_index(self, pkw, index):
        self.__pkws.insert(index, pkw)


if __name__ == "__main__":
    pkw = Pkw(4)
    pkw.set_motor(Motor(300, "1.6"))
    pkw.set_fahrgestell(Fahrgestell())
    for i in range(4):
        pkw.add_reifen(Reifen(185, 200))
    fahrzeughalter = Fahrzeughalter("Max", "Mustermann")
    fahrzeughalter.add_pkw(pkw)
    print(fahrzeughalter.get_pkw_anzahl())
    print(fahrzeughalter.get_pkw_by_index(0).get_motor().get_power())
    print(fahrzeughalter.get_pkw_by_index(0).get_reifen())
    print(fahrzeughalter.get_pkw_by_index(0).get_reifen()[0].get_zoll())
    print(fahrzeughalter.get_pkw_by_index(0).get_reifen()[0].get_profiltiefe())
    print(fahrzeughalter.get_pkw_by_index(0).get_fahrgestell().get_doors())
    fahrzeughalter.get_pkw_by_index(0).set_max_reifen(3)
    print(fahrzeughalter.get_pkw_by_index(0).get_max_reifen())
