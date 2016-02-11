from classes import Environment, Drone, Warehouse, Order
import math
import operator
from read_data import getData


def get_distance(object1, object2):
    return math.sqrt(abs(object1.position[0] - object2.position[0]) + abs(object1.position[1] + object2.position[1]))


def calculate_total_weight(order, product_weights):
    """
    Calculates the total weight of an order.
    :param order:
    :return:
    """
    total_weight = 0
    for product_id, num_items in enumerate(order.products):
        total_weight += num_items * product_weights[product_id]
    return total_weight


if __name__ == '__main__':

    environment, warehouses, orders, drones = getData('busy_day.in')
    commands = []

    # sort order by total weight of items in order
    order_total_weights = [(order, calculate_total_weight(order, environment.product_weights)) for order in orders]

    orders = [order for order in sorted(order_total_weights, key=operator.itemgetter(1))]

    for order in orders:
        for drone in drones:

            drone_warehouse_dists = [(warehouse, get_distance(drone, warehouse)) for warehouse in warehouses]
            # sort warehouses in order of closeness
            for warehouse in [warehouse for warehouse, _ in sorted(drone_warehouse_dists, key=operator.itemgetter(1))]:

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
