
class Truck:
    def __init(self, capacity, speed, load, packages, miles, address, departure_time):
        self.capacity = capacity
        self.speed = speed
        self.load = load
        self.packages = packages
        self.miles = miles
        self.address = address
        self.depature_time = departure_time
        self.time = departure_time

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (self.capacity, self.speed, self.load, self.packages, self.miles,
                                               self.address, self.departure_time)