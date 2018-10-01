file_name = input("Enter the read file name: ")
sigma = int(input("Enter spread number don't find sigma ⍬: "))
omega = float(input("Enter decay rate number (omega ⍵): "))



class node:
    def __init__(self, id):
        self.id = id
        self.connection = []
        self.monster = 0
        self.hole = 0
        self.wall = 0
        self.gold = 0
        self.wind_val = 0
        self.smell_val = 0

    def add_edge(self, edge):
        if edge not in self.connection:
            self.connection.append(edge)
            return True
        else:
            return False

    def remove_edge(self, edge):
        self.connection.remove(edge)

    def get_con(self):
        return self.connection.copy()

    def get_id(self):
        return self.id

    def get_len(self):
        return len(self.connection)


def recursion_wind(node_num, sigma, omega, val):
    if sigma == -1:
        return
    position = 0
    for x in range(len(pool)):
        if pool[x].get_id() == node_num:
            pool[x].wind_val = val
            position = x
    for element in pool:
        if element.get_id() in pool[position].get_con():
            if element.wind_val < val * omega:
                recursion_wind(element.get_id(), sigma - 1, omega, val * omega)

def recursion_smell(node_num, sigma, omega, val):
    if sigma == -1:
        return
    position = 0
    for x in range(len(pool)):
        if pool[x].get_id() == node_num:
            pool[x].smell_val = val
            position = x
    for element in pool:
        if element.get_id() in pool[position].get_con():
            if element.smell_val < val * omega:
                recursion_smell(element.get_id(), sigma - 1, omega, val * omega)

def output(pool):
    for element in pool:
        line = str(element.id) + ":" + str(element.wall) + "," + str(element.hole) + "," + str(element.monster) + "," + str(element.gold) + "," + str(float(element.wind_val)) + "," + str(float(element.smell_val))
        for x in element.get_con():
            line += " " + str(x)
        print(line)




file = open("out.txt", "r")
pool = []
for line in file:
    semicolon = line.strip().split(":")
    new_node = node(int(semicolon[0]))
    parts = semicolon[1].split(",")
    new_node.wall = int(parts[0])
    new_node.hole = int(parts[1])
    new_node.monster = int(parts[2])
    new_node.gold = int(parts[3])
    new_node.wind_val = float(parts[4])
    parts = parts[5].split(" ")
    new_node.smell_val = float(parts[0])
    for x in range(1, len(parts)):
        new_node.add_edge(int(parts[x]))
    pool.append(new_node)

for element in pool:
    if element.hole == 1:
        recursion_wind(element.get_id(), sigma, omega, 1)
for element in pool:
    if element.monster == 1:
        recursion_smell(element.get_id(), sigma, omega, 1)
output(pool)