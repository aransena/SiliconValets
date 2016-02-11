import read_data as rd
import matplotlib.pyplot as plt

data = rd.getData("example.in")
#data = rd.getData("mother_of_all_warehouses.in")
#data = rd.getData("redundancy.in")
drones = data[3]
print drones[0].position

environment = data[0]
warehouses = data[1]
orders = data[2]

plt.figure(1)
plt.margins(0.1,0.1)
j=0
for w in warehouses:
    if j == 0:
        plt.plot(w.position[0], w.position[1],'bo',markersize=20)
        j=1
    else:
        plt.plot(w.position[0], w.position[1],'go')

for o in orders:
    plt.plot(o.location[0], o.location[1],'ro',alpha=0.3)

plt.show()
