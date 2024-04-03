class Package:
    def __init__(self, id, address, city, state, zipcode, delivery_deadline, weight, status):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.delivery_deadline = delivery_deadline
        self.weight = weight
        self.status = status
        self.departed_at = None
        self.delivered_at = None

    def __str__(self):
        return "Package ID: %s, Address: %s, City: %s, State: %s, Zipcode: %s, Delivery Deadline: %s, Weight: %s, Delivery Time: %s, Status: %s" % (self.id, self.address, self.city, self.state, self.zipcode,
                                                       self.delivery_deadline, self.weight, self.delivered_at, 
                                                       self.status)
    
    # Method to update status of package
    def status_update(self, convert_timedelta):
        if self.delivered_at < convert_timedelta:
            self.status = "Delivered"
        elif self.departed_at > convert_timedelta:
            self.status = "En route"
        else:
            self.status = "At hub"