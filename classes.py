class Environment():
    def __init__(self, dimensions, num_drones,turn, orders, max_payload):
        self.dimensions = dimensions
        self.num_drones = num_drones
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
    def __init__(self, location, num_products, products):
        self.location = location
        self.num_products = num_products
        self.products = products


class Command():
    def __init__(self, drone_id, command_type, warehouse_or_customer_id, product_id, num_products):
        self.drone_id = drone_id
        command_type = command_type.upper()
        if command_type not in ['LOAD', 'UNLOAD', 'DELIVER', 'L', 'U', 'D']:
            raise ValueError('Command type has to be one of load, unload, deliver, or L, U, D.')
        if command_type == 'LOAD':
            command_type = 'L'
        elif command_type == 'UNLOAD':
            command_type = 'U'
        elif command_type == 'DELIVER':
            command_type = 'D'
        self.command_type = command_type
        self.warehouse_or_customer_id = warehouse_or_customer_id
        self.product_id = product_id
        self.num_products = num_products
