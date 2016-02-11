import classes as cl

def nextLine(f):
    line = f.readline()
    line = line.split()
    line = map(int,line)
    return line

    

def getData(dataset):
    #dataset = "busy_day.in"

    f = open(dataset, 'r')

    line = nextLine(f)
    
    environment = cl.Environment(dimensions = [line[0],line[1]], num_drones = line[2], turn = line[3], orders = 0, max_payload = line[4])


    line = nextLine(f)
    num_products=line[0]
    line = nextLine(f)
    product_weights=line
    products=[]
    #for i in range(0,num_products):
        #products.append(cl.Product(i,product_weights[i]))

    line = nextLine(f)
    num_warehouses=line[0]
    warehouses=[]
    for i in range(0,num_warehouses):
        line=nextLine(f)
        pos = [line[0],line[1]]
        line=nextLine(f)
        products = line
        warehouse = cl.Warehouse(i,pos,products)
        warehouses.append(warehouse)

    drones=[]
    
    for i in range(0,environment.num_drones):
        drone = cl.Drone(i,warehouses[0].position,0,[])
        drones.append(drone)

    line = nextLine(f)
    num_orders=line[0]
    orders=[]

    for i in range(0,num_orders):
        line=nextLine(f)
        pos = [line[0],line[1]]
        line=nextLine(f)
        num_products = line[0]
        line=nextLine(f)
        products = line
        order = cl.Order(i,pos,num_products, products)
        orders.append(order)

    data=[environment,warehouses,orders,drones]

    return data
