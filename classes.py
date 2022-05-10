from numpy import power


class Fahrzeug:
    license_plate = ""
    max_speed = 0.0
    current_speed = 0.0
    mileage = 0
    color = ""
    seat_heating = False
    brand = ""
    model = ""
    power = 0
    ccm = 0
    fuel_type = ""
    fuel_consumption = 0
    fuel_tank_capacity = 0

    def __init__(self, license_plate, max_speed, current_speed, mileage, color, seat_heating, brand, model, power, ccm, fuel_type, fuel_consumption, fuel_tank_capacity):
        self.license_plate = license_plate
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.mileage = mileage
        self.color = color
        self.seat_heating = seat_heating
        self.brand = brand
        self.model = model
        self.power = power
        self.ccm = ccm
        self.fuel_type = fuel_type
        self.fuel_consumption = fuel_consumption
        self.fuel_tank_capacity = fuel_tank_capacity

    def accelerate(self, speed):
        self.current_speed += speed

    def brake(self):
        self.current_speed = 0

    def get_fuel_consumption(self):
        return self.fuel_consumption * self.current_speed / 100

    def get_fuel_tank_capacity(self):
        return self.fuel_tank_capacity

    def get_fuel_level(self):
        return self.fuel_tank_capacity - self.get_fuel_consumption()

    def get_mileage(self):
        return self.mileage

    def get_max_speed(self):
        return self.max_speed

    def get_current_speed(self):
        return self.current_speed

    def get_color(self):
        return self.color

    def get_seat_heating(self):
        return self.seat_heating

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_power(self):
        return self.power

    def get_ccm(self):
        return self.ccm

    def get_fuel_type(self):
        return self.fuel_type

    def get_license_plate(self):
        return self.license_plate

    def set_license_plate(self, license_plate):
        self.license_plate = license_plate

    def set_max_speed(self, max_speed):
        self.max_speed = max_speed

    def set_current_speed(self, current_speed):
        self.current_speed = current_speed

    def set_mileage(self, mileage):
        self.mileage = mileage

    def set_color(self, color):
        self.color = color

    def set_seat_heating(self, seat_heating):
        self.seat_heating = seat_heating

    def set_brand(self, brand):
        self.brand = brand

    def set_model(self, model):
        self.model = model

    def set_power(self, power):
        self.power = power

    def set_ccm(self, ccm):
        self.ccm = ccm

    def set_fuel_type(self, fuel_type):
        self.fuel_type = fuel_type

    def set_fuel_consumption(self, fuel_consumption):
        self.fuel_consumption = fuel_consumption

    def set_fuel_tank_capacity(self, fuel_tank_capacity):
        self.fuel_tank_capacity = fuel_tank_capacity


class PKW(Fahrzeug):
    seats = 0

    def __init__(self, license_plate, max_speed, current_speed, mileage, color, seat_heating, brand, model, power, ccm, fuel_type, fuel_consumption, fuel_tank_capacity, seats):
        super().__init__(license_plate, max_speed, current_speed, mileage, color, seat_heating,
                         brand, model, power, ccm, fuel_type, fuel_consumption, fuel_tank_capacity)
        self.seats = seats

    def get_seats(self):
        return self.seats

    def set_seats(self, seats):
        self.seats = seats


class Cabrio(PKW):
    top_type = ""
    top_status = False

    def __init__(self, license_plate, max_speed, current_speed, mileage, color, seat_heating, brand, model, power, ccm, fuel_type, fuel_consumption, fuel_tank_capacity, seats, top_type, top_status):
        super().__init__(license_plate, max_speed, current_speed, mileage, color, seat_heating,
                         brand, model, power, ccm, fuel_type, fuel_consumption, fuel_tank_capacity, seats)
        self.top_type = top_type
        self.top_status = top_status

    def get_top_type(self):
        return self.top_type

    def get_top_status(self):
        return self.top_status

    def set_top_type(self, top_type):
        self.top_type = top_type

    def set_top_status(self, top_status):
        self.top_status = top_status

    def toogleTop(self):
        self.top_status = not self.top_status


class Pickup(PKW):
    max_load = 0.0
    four_wheel = False

    def __init__(self, license_plate, max_speed, current_speed, mileage, color, seat_heating, brand, model, power, ccm, fuel_type, fuel_consumption, fuel_tank_capacity, seats, max_load, four_wheel):
        super().__init__(license_plate, max_speed, current_speed, mileage, color, seat_heating,
                         brand, model, power, ccm, fuel_type, fuel_consumption, fuel_tank_capacity, seats)
        self.max_load = max_load
        self.four_wheel = four_wheel

    def get_max_load(self):
        return self.max_load

    def get_four_wheel(self):
        return self.four_wheel

    def set_max_load(self, max_load):
        self.max_load = max_load

    def toogleFourWheel(self):
        self.four_wheel = not self.four_wheel


class FamilyCar(PKW):
    roofBox_Volume = 0.0
    child_seat = False

    def __init__(self, license_plate, max_speed, current_speed, mileage, color, seat_heating, brand, model, power, ccm, fuel_type, fuel_consumption, fuel_tank_capacity, seats, roofBox_Volume, child_seat):
        super().__init__(license_plate, max_speed, current_speed, mileage, color, seat_heating,
                         brand, model, power, ccm, fuel_type, fuel_consumption, fuel_tank_capacity, seats)
        self.roofBox_Volume = roofBox_Volume
        self.child_seat = child_seat

    def get_roofBox_Volume(self):
        return self.roofBox_Volume

    def get_child_seat(self):
        return self.child_seat

    def set_roofBox_Volume(self, roofBox_Volume):
        self.roofBox_Volume = roofBox_Volume

    def set_child_seat(self, child_seat):
        self.child_seat = child_seat


class LKW(Fahrzeug):
    achses = 0
    maximum_load = 0.0
    sleeper_cab = False
    current_load = 0.0
    trailer_volume = 0.0

    def __init__(self, license_plate, max_speed, current_speed, mileage, color, seat_heating, brand, model, power, ccm, fuel_type, fuel_consumption, fuel_tank_capacity, achses, maximum_load, sleeper_cab, current_load, trailer_volume):
        super().__init__(license_plate, max_speed, current_speed, mileage, color, seat_heating,
                         brand, model, power, ccm, fuel_type, fuel_consumption, fuel_tank_capacity)
        self.achses = achses
        self.maximum_load = maximum_load
        self.sleeper_cab = sleeper_cab
        self.current_load = current_load
        self.trailer_volume = trailer_volume

    def load(self, load):
        if load > self.maximum_load:
            print("Load is too large")
        else:
            self.current_load = load

    def unload(self):
        self.current_load = 0.0

    def get_achses(self):
        return self.achses

    def get_maximum_load(self):
        return self.maximum_load

    def get_sleeper_cab(self):
        return self.sleeper_cab

    def get_current_load(self):
        return self.current_load

    def get_trailer_volume(self):
        return self.trailer_volume

    def set_achses(self, achses):
        self.achses = achses

    def set_maximum_load(self, maximum_load):
        self.maximum_load = maximum_load

    def set_sleeper_cab(self, sleeper_cab):
        self.sleeper_cab = sleeper_cab

    def set_current_load(self, current_load):
        self.current_load = current_load

    def set_trailer_volume(self, trailer_volume):
        self.trailer_volume = trailer_volume
