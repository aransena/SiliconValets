from classes import Environment, Drone, Warehouse, Product, Order
import math
import operator


def fake_load():
    return Environment(), Drone(), Warehouse()

def get_distance(object1, object2):
    return math.sqrt(abs(object1.position[0] - object2.position[0]) + abs(object1.position[1] + object2.position[1]))


if __name__ == '__main__':

    environment, drones, warehouses = fake_load()
    commands = []

    # do something with orders first

    for order in environment.orders:

        for drone in drones:

            warehouse_warehouse_dists = [(warehouse, get_distance(drone, warehouse)) for warehouse in warehouses]
            # sort warehouses in order of closeness
            for warehouse in [warehouse for warehouse, _ in sorted(warehouse_warehouse_dists, key=operator.itemgetter(1))]:

                # check if products are in warehouse
                # products is an array indexed by product ids, with numbers indicating the number of items
                for product_id, num_products in order.products:

                    # check if required number of products are in warehouse
                    if warehouse.products[product_id] <= num_products:

                        # if so then, drone should go to warehouse
                        commands.append(drone.load())
                        break


            # get closest warehouses where all of the required products are inside
