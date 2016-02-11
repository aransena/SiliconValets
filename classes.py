class Environment():
    def __init__(self, dimensions, num_drones,turn, orders, max_payload):
        self.dimensions = dimensions
        self.num_drones = num_drones
        self.turn = turn
        self.orders = orders
        self.max_payload = max_payload


class Drone():

    def __init__(self, id, position, weight, products):
        self.id = id
        self.position = position
        self.weight = weight
        self.products = []

    def load(self, warehouse, product_id, num_items, commands):

        # fly drone to warehouse location
        self.move(warehouse.location)

        # remove items from warehouse
        warehouse.products[product_id] = warehouse.products[product_id] - num_items

        # add items to drone
        self.products[product_id] = self.products[product_id] + num_items
        commands.append(Command(self.id, 'load', warehouse.id, product_id, num_items))

    def unload(self, warehouse, product_id, num_items, commands):

        # fly drone to warehouse location
        self.move(warehouse.location)

        # remove items from drone
        self.products[product_id] = self.products[product_id] + num_items

        # add items to warehouse
        warehouse.products[product_id] = warehouse.products[product_id] - num_items
        commands.append(Command(self.id, 'unload', warehouse.id, product_id, num_items))

    def deliver(self, order, product_id, num_items, commands):

        # fly drone to order location
        self.move(order.location)

        # remove items from drone
        self.products[product_id] = self.products[product_id] + num_items

        # add items to order
        order.products[product_id] = order.products[product_id] + num_items
        commands.append(Command(self.id, 'deliver', order.id, product_id, num_items))

    def move(self, destination):
        self.position = destination


class Warehouse():
    def __init__(self, id, position, products):
        self.id = id
        self.position = position
        self.products = products


class Order():
    def __init__(self, id, location, num_products, products):
        self.id = id
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
