class Environment():
    def __init__(self, dimensions, turn, orders, max_payload):
        self.dimensions = dimensions
        self.turn = turn
        self.orders = orders
        self.max_payload = max_payload


class Drone():
    def __init__(self, position, max_payload, weight):
        self.position = position
        self.weight = weight
        self.products = []

    def load(self):
        pass

    def unload(self):
        pass

    def deliver(self):
        pass


class Warehouse():
    def __init__(self, position, products):
        self.position = position
        self.products = products


class Product():
    def __init__(self, id, weight):
        self.id = id
        self.weight = weight


class Order():
    def __init__(self, location, products):
        self.location = location
        self.products = products
