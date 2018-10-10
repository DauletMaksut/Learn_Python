N = int(input("Value of (N): "))
K = int(input("Value of (K): "))
k = int(input("Value of (k): "))
p = int(input("Value of (p): "))

WW = int(input("Value of (WW): "))
HH = int(input("Value of (HH): "))
MM = int(input("Value of (MM): "))
GG = int(input("Value of (GG): "))

spread = int(input("Value of spread: "))
decay_rate = float(input("Value of decay rate: "))

class node:
    def __init__(self, mid, need_edges):
        self.mid = mid
        self.paths = []
        self.conn = need_edges
        self.hole = 0
        self.monster = 0
        self.wall = 0
        self.gold = 0
        self.wind = 0.0
        self.smell = 0.0

    def get_length(self):
        return len(self.paths)

    def add_edge(self, edge):
        if edge in self.paths:
            return False
        else:
            self.paths.append(edge)
            self.conn -= 1
            return True

def check_graph():
    for node in nodes:
        if node.conn != 0:
            return False
    return True

def add_smell(index_of_node ,spread_level, decay_rate, value_of_smell):
    if spread_level == -1:
        return
    nodes[index_of_node].smell = value_of_smell
    for i in nodes[index_of_node].paths:
        if nodes[i].smell < (value_of_smell * decay_rate):
            add_smell(i, spread_level - 1, decay_rate, value_of_smell * decay_rate)

def add_wind(index_of_node ,spread_level, decay_rate, value_of_wind):
    if spread_level == -1:
        return
    nodes[index_of_node].wind = value_of_wind
    for i in nodes[index_of_node].paths:
        if nodes[i].wind < (value_of_wind * decay_rate):
            add_wind(i, spread_level - 1, decay_rate, value_of_wind * decay_rate)

    

nodes = []
for i in range(K):
    nodes.append(node(i, k))
for i in range(K, N):
    nodes.append(node(i, p))

MIN = nodes[0]
MAX = nodes[0]
while True:
    for node in nodes:
        if MIN.conn == 0:
            for tmp in nodes:
                if tmp.conn != 0:
                    MIN = tmp
        if node.conn == 0:
            continue
        if MIN.conn > node.conn and node.conn != 0:
            MIN = node
    for node in nodes:
        if MAX.conn <= node.conn and node.conn != 0 and node != MIN:
            if node.mid in MIN.paths:
                continue
            MAX = node
    if MAX.mid != MIN.mid:
        MAX.add_edge(MIN.mid)
        MIN.add_edge(MAX.mid)
    if check_graph():
        break
for i in range(WW):
    nodes[i].wall = 1
for i in range(HH):
    add_wind(i ,spread, decay_rate, 1.0)
    nodes[i].hole = 1
for i in range(MM):
    add_smell(i ,spread, decay_rate, 1.0)
    nodes[i].monster = 1
for i in range(GG):
    nodes[i].gold = 1

file = open("result.txt", "w")
for node in nodes:
    line = str(node.mid) + ":" + str(node.wall) + "," +str(node.hole) + "," +str(node.monster) + "," + str(node.gold) + "," +str(node.wind) +"," +str(node.smell)
    for i in node.paths:
        line += " " + str(i)
    print(line)
    line += "\n"
    file.write(line)
file.close() 


