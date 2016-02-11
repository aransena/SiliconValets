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

    current_drone = drones[0]
    for order in orders:

        fulfilled = False
        product_id = 0

        # check if items are left in the order
        while order.products[product_id] > 0:

            drone_warehouse_dists = [(warehouse, get_distance(current_drone, warehouse)) for warehouse in warehouses]
            # sort warehouses in order of closeness
            for warehouse in [warehouse for warehouse, _ in sorted(drone_warehouse_dists, key=operator.itemgetter(1))]:

                # check if required number of products are in warehouse
                if warehouse.products[product_id] > 0:

                    # if so then, then check how many products we can load on this drone
                    for item in order.products:
                        payload += environment.product_weights[item.id]
                    #warehouse.products[]
                    environment.product_weights[product_id]


                    drone.load(warehouse, product_id, order.products[product_id], commands)



                    # the drone then brings the items to the order location
                    drone.deliver(order, product_id, order.products[product_id], commands)

                    delivered = True
                    break




        for drone in drones:

            delivered = False



            # go to next drone if current drone has delivered an order
            if delivered:
                break

            # get closest warehouses where all of the required products are inside
