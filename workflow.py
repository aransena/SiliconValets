from classes import Environment, Drone, Warehouse, Order
import math
import operator
from read_data import getData


def get_distance(object1, object2):
    return math.sqrt(abs(object1.position[0] - object2.position[0]) + abs(object1.position[1] + object2.position[1]))


if __name__ == '__main__':

    environment, drones, warehouses = getData('busy_day.in')
    commands = []

    # do something with orders first

    for order in environment.orders:

        for drone in drones:

            warehouse_warehouse_dists = [(warehouse, get_distance(drone, warehouse)) for warehouse in warehouses]
            # sort warehouses in order of closeness
            for warehouse in [warehouse for warehouse, _ in sorted(warehouse_warehouse_dists, key=operator.itemgetter(1))]:

                # check if products are in warehouse
                # products is an array indexed by product ids, with numbers indicating the number of items
                for product_id, num_items in order.products:

                    # check if required number of products are in warehouse
                    if warehouse.products[product_id] <= num_items:

                        # if so then, drone should go to warehouse
                        drone.load(warehouse, product_id, num_items, commands)

                        # the drone then brings the items to the order location
                        drone.deliver(order, product_id, num_items, commands)

                        break


            # get closest warehouses where all of the required products are inside
