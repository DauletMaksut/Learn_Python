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
K_pool = [node(x) for x in range(4)]
N_pool = [node(x) for x in range(4, 8)]
pool = []
for x in K_pool:
    pool.append(x)
for x in N_pool:
    pool.append(x)
def work():
    pool[2].smell_val = 20

work()
print(type(pool[2]))