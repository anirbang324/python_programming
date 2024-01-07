class Car:
    def init(self, car_type):

        self.type = car_type


class Service:
    def init(self, code, name, price_hatchback, price_sedan, price_suv):

        self.code = code


        self.name = name
        self.price_hatchback = price_hatchback
        self.price_sedan = price_sedan
        self.price_suv = price_suv


def get_price(self, car):
    if car.type == "Hatchback":
        return self.price_hatchback
    elif car.type == "Sedan":
        return self.price_sedan
    elif car.type == "SUV":
        return self.price_suv


class CarServiceStation:
    def init(self):

        self.services = []


def add_service(self, service):
    self.services.append(service)


def get_service(self, code):
    for service in self.services:
        if service.code == code:
            return service
    return None


def get_total_price(self, car, services):
    total_price = 0
    for code in services:
        service = self.get_service(code)
        if service:
            total_price += service.get_price(car)
    return total_price


stations = CarServiceStation()

stations.add_service(Service("BASIC", "Basic Service", 1000, 2000, 3000))
stations.add_service(Service("ENGINE", "Engine Fixing", 5000, 10000, 15000))
stations.add_service(Service("CLUTCH", "Clutch Fixing", 4000, 8000, 12000))
stations.add_service(Service("GEAR", "Gear Fixing", 3000, 6000, 9000))
stations.add_service(Service("BRAKE", "Brake Fixing", 2000, 4000, 6000))

car = Car("Hatchback")

services = ["BASIC", "ENGINE", "CLUTCH", "GEAR", "BRAKE"]
total_price = stations.get_total_price(car, services)
print(f"Total price for car of type {car.type}: {total_price}")


