import read_data as rd

data = rd.getData("example.in")
drones = data[4]
print drones[0].position
