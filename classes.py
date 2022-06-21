class Fahrzeug:
    __license_plate = ""
    __max_speed = 0.0
    __current_speed = 0.0
    __mileage = 0
    __color = ""
    __seat_heating = False
    __brand = ""
    __model = ""
    __power = 0
    __ccm = 0
    __fuel_type = ""
    __fuel_consumption = 0
    __fuel_tank_capacity = 0

    def __str__(x):
        return "Kennzeichen: " + x.__license_plate + ", Maximale Geschwindigkeit: " + str(
            x.__max_speed) + ", \nMomentane Geschwindigkeit: " + str(x.__current_speed) + ", Km Stand: " + str(
            x.__mileage) \
               + ", \nFarbe: " + x.__color + ", Sitzheizung: " + str(
            x.__seat_heating) + ", \nMarke: " + x.__brand + ", Modell: " + x.__model + ", \nKraft: " + str(
            x.__power) + ", Hubraum: " + str(x.__ccm) \
               + ", \nKraftstoff: " + x.__fuel_type + ", Verbrauch: " + str(
            x.__fuel_consumption) + ", \nTankkapazität: " + str(x.__fuel_tank_capacity);

    def __init__(self, license_plate, max_speed, mileage, color, seat_heating, brand, model, power, ccm, fuel_type,
                 fuel_consumption, fuel_tank_capacity):
        self.__license_plate = license_plate
        self.__max_speed = max_speed
        self.__mileage = mileage
        self.__color = color
        self.__seat_heating = seat_heating
        self.__brand = brand
        self.__model = model
        self.__power = power
        self.__ccm = ccm
        self.__fuel_type = fuel_type
        self.__fuel_consumption = fuel_consumption
        self.__fuel_tank_capacity = fuel_tank_capacity

    def accelerate(self, speed):
        self.__current_speed += speed

    def brake(self):
        self.__current_speed = 0

    def toString(self):
        print('Kennzeichen:' + self.__license_plate)

    def get_fuel_consumption(self):
        return self.__fuel_consumption * self.__current_speed / 100

    def get_fuel_tank_capacity(self):
        return self.__fuel_tank_capacity

    def get_fuel_level(self):
        return self.__fuel_tank_capacity - self.get_fuel_consumption()

    def get_mileage(self):
        return self.__mileage

    def get_max_speed(self):
        return self.__max_speed

    def get_current_speed(self):
        return self.__current_speed

    def get_color(self):
        return self.__color

    def get_seat_heating(self):
        return self.__seat_heating

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_power(self):
        return self.__power

    def get_ccm(self):
        return self.__ccm

    def get_fuel_type(self):
        return self.__fuel_type

    def get_license_plate(self):
        return self.__license_plate

    def set_license_plate(self, license_plate):
        self.__license_plate = license_plate

    def set_max_speed(self, max_speed):
        self.__max_speed = max_speed

    def set_current_speed(self, current_speed):
        self.__current_speed = current_speed

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def set_color(self, color):
        self.__color = color

    def set_seat_heating(self, seat_heating):
        self.__seat_heating = seat_heating

    def set_brand(self, brand):
        self.__brand = brand

    def set_model(self, model):
        self.__model = model

    def set_power(self, power):
        self.__power = power

    def set_ccm(self, ccm):
        self.__ccm = ccm

    def set_fuel_type(self, fuel_type):
        self.__fuel_type = fuel_type

    def set_fuel_consumption(self, fuel_consumption):
        self.__fuel_consumption = fuel_consumption

    def set_fuel_tank_capacity(self, fuel_tank_capacity):
        self.__fuel_tank_capacity = fuel_tank_capacity


class PKW(Fahrzeug):
    __seats = 0

    def __init__(self, license_plate, max_speed, mileage, color, seat_heating, brand, model, power, ccm, fuel_type,
                 fuel_consumption, fuel_tank_capacity, seats):
        super().__init__(license_plate, max_speed, mileage, color, seat_heating,
                         brand, model, power, ccm, fuel_type, fuel_consumption, fuel_tank_capacity)
        self.__seats = seats

    def __str__(x):
        return super().__str__() + ", Sitze: " + str(x.__seats)

    def get_seats(self):
        return self.__seats

    def set_seats(self, seats):
        self.__seats = seats


class Cabrio(PKW):
    __top_type = ""
    __top_status = False

    def __init__(self, license_plate, max_speed, mileage, color, seat_heating, brand, model, power, ccm, fuel_type,
                 fuel_consumption, fuel_tank_capacity, seats, top_type, top_status):
        super().__init__(license_plate, max_speed, mileage, color, seat_heating,
                         brand, model, power, ccm, fuel_type, fuel_consumption, fuel_tank_capacity, seats)
        self.__top_type = top_type
        self.__top_status = top_status

    def __str__(x):
        return super().__str__() + ", \nTop-Typ: " + x.__top_type + ", Top-Status: " + str(x.__top_status)

    def get_top_type(self):
        return self.__top_type

    def get_top_status(self):
        return self.__top_status

    def set_top_type(self, top_type):
        self.__top_type = top_type

    def set_top_status(self, top_status):
        self.__top_status = top_status

    def toogleTop(self):
        self.__top_status = not self.__top_status


class Pickup(PKW):
    __max_load = 0.0
    __four_wheel = False

    def __init__(self, license_plate, max_speed, mileage, color, seat_heating, brand, model, power, ccm, fuel_type,
                 fuel_consumption, fuel_tank_capacity, seats, max_load, four_wheel):
        super().__init__(license_plate, max_speed, mileage, color, seat_heating,
                         brand, model, power, ccm, fuel_type, fuel_consumption, fuel_tank_capacity, seats)
        self.__max_load = max_load
        self.__four_wheel = four_wheel

    def __str__(x):
        return super().__str__() + ", \nMaximales Ladegewicht: " + x.__max_load + ", Vier Räder: " + str(x.__four_wheel)

    def get_max_load(self):
        return self.__max_load

    def get_four_wheel(self):
        return self.__four_wheel

    def set_max_load(self, max_load):
        self.__max_load = max_load

    def toogleFourWheel(self):
        self.__four_wheel = not self.__four_wheel


class FamilyCar(PKW):
    __roofBox_Volume = 0.0
    __child_seat = False

    def __init__(self, license_plate, max_speed, mileage, color, seat_heating, brand, model, power, ccm, fuel_type,
                 fuel_consumption, fuel_tank_capacity, seats, roofBox_Volume, child_seat):
        super().__init__(license_plate, max_speed, mileage, color, seat_heating,
                         brand, model, power, ccm, fuel_type, fuel_consumption, fuel_tank_capacity, seats)
        self.__roofBox_Volume = roofBox_Volume
        self.__child_seat = child_seat

    def __str__(x):
        return super().__str__() + ", \nDachboxvolumen: " + str(x.__roofBox_Volume) + ", Kindersitz: " + str(
            x.__child_seat)

    def get_roofBox_Volume(self):
        return self.__roofBox_Volume

    def get_child_seat(self):
        return self.__child_seat

    def set_roofBox_Volume(self, roofBox_Volume):
        self.__roofBox_Volume = roofBox_Volume

    def set_child_seat(self, child_seat):
        self.__child_seat = child_seat


class LKW(Fahrzeug):
    __achses = 0
    __maximum_load = 0.0
    __sleeper_cab = False
    __current_load = 0.0
    __trailer_volume = 0.0

    def __init__(self, license_plate, max_speed, mileage, color, seat_heating, brand, model, power, ccm, fuel_type,
                 fuel_consumption, fuel_tank_capacity, achses, maximum_load, sleeper_cab, current_load, trailer_volume):
        super().__init__(license_plate, max_speed, mileage, color, seat_heating,
                         brand, model, power, ccm, fuel_type, fuel_consumption, fuel_tank_capacity)
        self.__achses = achses
        self.__maximum_load = maximum_load
        self.__sleeper_cab = sleeper_cab
        self.__current_load = current_load
        self.__trailer_volume = trailer_volume

    def __str__(x):
        return super().__str__() + ", Achsen: " + str(
            x.__achses) + ", \nMaximale Ladung: " + x.__maximum_load + ", Schlafkabine: " + str(x.__sleeper_cab) \
               + ", \nMomentane Ladung: " + x.__current_load + ", Anhängervolumen: " + x.__trailer_volume

    def load(self, load):
        if load > self.__maximum_load:
            print("Load is too large")
        else:
            self.__current_load = load

    def unload(self):
        self.__current_load = 0.0

    def get_achses(self):
        return self.__achses

    def get_maximum_load(self):
        return self.__maximum_load

    def get_sleeper_cab(self):
        return self.__sleeper_cab

    def get_current_load(self):
        return self.__current_load

    def get_trailer_volume(self):
        return self.__trailer_volume

    def set_achses(self, achses):
        self.__achses = achses

    def set_maximum_load(self, maximum_load):
        self.__maximum_load = maximum_load

    def set_sleeper_cab(self, sleeper_cab):
        self.__sleeper_cab = sleeper_cab

    def set_current_load(self, current_load):
        self.__current_load = current_load

    def set_trailer_volume(self, trailer_volume):
        self.__trailer_volume = trailer_volume


class Fahrzeug:
    __license_plate = ""
    __max_speed = 0.0
    __current_speed = 0.0
    __mileage = 0
    __color = ""
    __seat_heating = False
    __brand = ""
    __model = ""
    __power = 0
    __ccm = 0
    __fuel_type = ""
    __fuel_consumption = 0
    __fuel_tank_capacity = 0

    def __str__(x):
        return "Kennzeichen: " + x.__license_plate + ", Maximale Geschwindigkeit: " + str(
            x.__max_speed) + ", \nMomentane Geschwindigkeit: " + str(x.__current_speed) + ", Km Stand: " + str(
            x.__mileage) \
               + ", \nFarbe: " + x.__color + ", Sitzheizung: " + str(
            x.__seat_heating) + ", \nMarke: " + x.__brand + ", Modell: " + x.__model + ", \nKraft: " + str(
            x.__power) + ", Hubraum: " + str(x.__ccm) \
               + ", \nKraftstoff: " + x.__fuel_type + ", Verbrauch: " + str(
            x.__fuel_consumption) + ", \nTankkapazität: " + str(x.__fuel_tank_capacity);

    def __init__(self, license_plate, max_speed, mileage, color, seat_heating, brand, model, power, ccm, fuel_type,
                 fuel_consumption, fuel_tank_capacity):
        self.__license_plate = license_plate
        self.__max_speed = max_speed
        self.__mileage = mileage
        self.__color = color
        self.__seat_heating = seat_heating
        self.__brand = brand
        self.__model = model
        self.__power = power
        self.__ccm = ccm
        self.__fuel_type = fuel_type
        self.__fuel_consumption = fuel_consumption
        self.__fuel_tank_capacity = fuel_tank_capacity

    def accelerate(self, speed):
        self.__current_speed += speed

    def brake(self):
        self.__current_speed = 0

    def toString(self):
        print('Kennzeichen:' + self.__license_plate)

    def get_fuel_consumption(self):
        return self.__fuel_consumption * self.__current_speed / 100

    def get_fuel_tank_capacity(self):
        return self.__fuel_tank_capacity

    def get_fuel_level(self):
        return self.__fuel_tank_capacity - self.get_fuel_consumption()

    def get_mileage(self):
        return self.__mileage

    def get_max_speed(self):
        return self.__max_speed

    def get_current_speed(self):
        return self.__current_speed

    def get_color(self):
        return self.__color

    def get_seat_heating(self):
        return self.__seat_heating

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_power(self):
        return self.__power

    def get_ccm(self):
        return self.__ccm

    def get_fuel_type(self):
        return self.__fuel_type

    def get_license_plate(self):
        return self.__license_plate

    def set_license_plate(self, license_plate):
        self.__license_plate = license_plate

    def set_max_speed(self, max_speed):
        self.__max_speed = max_speed

    def set_current_speed(self, current_speed):
        self.__current_speed = current_speed

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def set_color(self, color):
        self.__color = color

    def set_seat_heating(self, seat_heating):
        self.__seat_heating = seat_heating

    def set_brand(self, brand):
        self.__brand = brand

    def set_model(self, model):
        self.__model = model

    def set_power(self, power):
        self.__power = power

    def set_ccm(self, ccm):
        self.__ccm = ccm

    def set_fuel_type(self, fuel_type):
        self.__fuel_type = fuel_type

    def set_fuel_consumption(self, fuel_consumption):
        self.__fuel_consumption = fuel_consumption

    def set_fuel_tank_capacity(self, fuel_tank_capacity):
        self.__fuel_tank_capacity = fuel_tank_capacity


class PKW(Fahrzeug):
    __seats = 0

    def __init__(self, license_plate, max_speed, mileage, color, seat_heating, brand, model, power, ccm, fuel_type,
                 fuel_consumption, fuel_tank_capacity, seats):
        super().__init__(license_plate, max_speed, mileage, color, seat_heating,
                         brand, model, power, ccm, fuel_type, fuel_consumption, fuel_tank_capacity)
        self.__seats = seats

    def __str__(x):
        return super().__str__() + ", Sitze: " + str(x.__seats)

    def get_seats(self):
        return self.__seats

    def set_seats(self, seats):
        self.__seats = seats


class Cabrio(PKW):
    __top_type = ""
    __top_status = False

    def __init__(self, license_plate, max_speed, mileage, color, seat_heating, brand, model, power, ccm, fuel_type,
                 fuel_consumption, fuel_tank_capacity, seats, top_type, top_status):
        super().__init__(license_plate, max_speed, mileage, color, seat_heating,
                         brand, model, power, ccm, fuel_type, fuel_consumption, fuel_tank_capacity, seats)
        self.__top_type = top_type
        self.__top_status = top_status

    def __str__(x):
        return super().__str__() + ", \nTop-Typ: " + x.__top_type + ", Top-Status: " + str(x.__top_status)

    def get_top_type(self):
        return self.__top_type

    def get_top_status(self):
        return self.__top_status

    def set_top_type(self, top_type):
        self.__top_type = top_type

    def set_top_status(self, top_status):
        self.__top_status = top_status

    def toogleTop(self):
        self.__top_status = not self.__top_status


class Pickup(PKW):
    __max_load = 0.0
    __four_wheel = False

    def __init__(self, license_plate, max_speed, mileage, color, seat_heating, brand, model, power, ccm, fuel_type,
                 fuel_consumption, fuel_tank_capacity, seats, max_load, four_wheel):
        super().__init__(license_plate, max_speed, mileage, color, seat_heating,
                         brand, model, power, ccm, fuel_type, fuel_consumption, fuel_tank_capacity, seats)
        self.__max_load = max_load
        self.__four_wheel = four_wheel

    def __str__(x):
        return super().__str__() + ", \nMaximales Ladegewicht: " + x.__max_load + ", Vier Räder: " + str(x.__four_wheel)

    def get_max_load(self):
        return self.__max_load

    def get_four_wheel(self):
        return self.__four_wheel

    def set_max_load(self, max_load):
        self.__max_load = max_load

    def toogleFourWheel(self):
        self.__four_wheel = not self.__four_wheel


class FamilyCar(PKW):
    __roofBox_Volume = 0.0
    __child_seat = False

    def __init__(self, license_plate, max_speed, mileage, color, seat_heating, brand, model, power, ccm, fuel_type,
                 fuel_consumption, fuel_tank_capacity, seats, roofBox_Volume, child_seat):
        super().__init__(license_plate, max_speed, mileage, color, seat_heating,
                         brand, model, power, ccm, fuel_type, fuel_consumption, fuel_tank_capacity, seats)
        self.__roofBox_Volume = roofBox_Volume
        self.__child_seat = child_seat

    def __str__(x):
        return super().__str__() + ", \nDachboxvolumen: " + str(x.__roofBox_Volume) + ", Kindersitz: " + str(
            x.__child_seat)

    def get_roofBox_Volume(self):
        return self.__roofBox_Volume

    def get_child_seat(self):
        return self.__child_seat

    def set_roofBox_Volume(self, roofBox_Volume):
        self.__roofBox_Volume = roofBox_Volume

    def set_child_seat(self, child_seat):
        self.__child_seat = child_seat


class LKW(Fahrzeug):
    __achses = 0
    __maximum_load = 0.0
    __sleeper_cab = False
    __current_load = 0.0
    __trailer_volume = 0.0

    def __init__(self, license_plate, max_speed, mileage, color, seat_heating, brand, model, power, ccm, fuel_type,
                 fuel_consumption, fuel_tank_capacity, achses, maximum_load, sleeper_cab, current_load, trailer_volume):
        super().__init__(license_plate, max_speed, mileage, color, seat_heating,
                         brand, model, power, ccm, fuel_type, fuel_consumption, fuel_tank_capacity)
        self.__achses = achses
        self.__maximum_load = maximum_load
        self.__sleeper_cab = sleeper_cab
        self.__current_load = current_load
        self.__trailer_volume = trailer_volume

    def __str__(x):
        return super().__str__() + ", Achsen: " + str(
            x.__achses) + ", \nMaximale Ladung: " + x.__maximum_load + ", Schlafkabine: " + str(x.__sleeper_cab) \
               + ", \nMomentane Ladung: " + x.__current_load + ", Anhängervolumen: " + x.__trailer_volume

    def load(self, load):
        if load > self.__maximum_load:
            print("Load is too large")
        else:
            self.__current_load = load

    def unload(self):
        self.__current_load = 0.0

    def get_achses(self):
        return self.__achses

    def get_maximum_load(self):
        return self.__maximum_load

    def get_sleeper_cab(self):
        return self.__sleeper_cab

    def get_current_load(self):
        return self.__current_load

    def get_trailer_volume(self):
        return self.__trailer_volume

    def set_achses(self, achses):
        self.__achses = achses

    def set_maximum_load(self, maximum_load):
        self.__maximum_load = maximum_load

    def set_sleeper_cab(self, sleeper_cab):
        self.__sleeper_cab = sleeper_cab

    def set_current_load(self, current_load):
        self.__current_load = current_load

    def set_trailer_volume(self, trailer_volume):
        self.__trailer_volume = trailer_volume


x = Cabrio("lala", 200, 2000, "green", True, "Porsche", "Caymon", 500, 500, "Diesel", 10, 200, 4, "NOrmal", True);
print(x)