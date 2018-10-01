N = int(input("Enter number (N): "))
K = int(input("Enter number (K): "))
k = int(input("Enter number (k): "))
p = int(input("Enter number (p): "))
WW = int(input("Enter number (WW): "))
HH = int(input("Enter number (HH): "))
MM = int(input("Enter number (MM): "))
GG = int(input("Enter number (GG): "))
omega = int(input("Enter spread number (⍬): "))
sigma = float(input("Enter decay rate number (⍵): "))

if WW > N:
    print("Nonono")
    quit()
if HH > N:
    print("Nonono")
    quit()
if MM > N:
    print("Nonono")
    quit()
if GG > N:
    print("Nonono")
    quit()


def recursion_wind(node_num, omega, sigma, val):
    if omega == -1:
        return
    pool[node_num].wind_val = val
    for x in pool[node_num].get_con():
        if pool[x].wind_val >= val * sigma:
            continue
        recursion_wind(x, omega - 1, sigma, val * sigma)

def recursion_smell(node_num, omega, sigma, val):
    if omega == -1:
        return
    pool[node_num].smell_val = val
    for x in pool[node_num].get_con():
        if pool[x].smell_val >= val * sigma:
            continue
        recursion_smell(x, omega - 1, sigma, val * sigma)

#Random begin
def randint(a, b):
    "Return random integer in range [a, b], including both end points."
    return a + randbelow(b - a + 1)

def randbelow(n):
    "Return a random int in the range [0,n).  Raises ValueError if n<=0."
    if n <= 0:
       raise ValueError
    k = n.bit_length()
    numbytes = (k + 7) // 8
    while True:
        r = int.from_bytes(random_bytes(numbytes), 'big')
        r >>= numbytes * 8 - k
        if r < n:
            return r

def random_bytes(n):
    "Return n random bytes"
    with open('/dev/urandom', 'rb') as file:
        return file.read(n)
#Random end
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


def level_one(pool, p):
    for x in pool:
        if x.get_len() > p:
            return True
    return False


def output(K_pool, N_pool):
    outwriter = []
    nodes = []
    for x in K_pool:
        outwriter.append(x.get_con())
        nodes.append(x)
    for x in N_pool:
        outwriter.append(x.get_con())
        nodes.append(x)
    file = open("out.txt", "w")
    for x in range(len(outwriter)):
        line = str(x) + ":" + str(nodes[x].wall) + "," + str(nodes[x].hole) + "," + str(nodes[x].monster) + "," + str(nodes[x].gold) + "," + str(float(nodes[x].wind_val)) + "," + str(float(nodes[x].smell_val))
        for y in outwriter[x]:
            line += " " + str(y)
        print(line)
        line += "\n"
        file.write(line)
    file.close()


K_pool = [node(x) for x in range(K)]
N_pool = [node(x) for x in range(K, N)]
pool = []
for x in K_pool:
    pool.append(x)
for x in N_pool:
    pool.append(x)

tracker = 0
try:
    for K_element in K_pool:
        for i in range(k):
            K_element.add_edge(N_pool[tracker].get_id())
            N_pool[tracker].add_edge(K_element.get_id())
            tracker += 1
            if tracker == len(N_pool):
                tracker = 0
except:
    print("Sorry terrible damage cannot do that")
    quit()
              
if level_one(N_pool, p):
    print("Sorry i cannot do that")
    quit()
try:
    for node in N_pool:
        if node.get_len() == p:
            continue
        for x in range(len(N_pool)):
            if node.get_len() == p:
                break
            if node.get_id() == N_pool[tracker].get_id():
                tracker += 1
                continue
            if N_pool[tracker].get_len() == p:
                tracker += 1
                continue
            node.add_edge(N_pool[tracker].get_id())
            N_pool[tracker].add_edge(node.get_id())
            tracker += 1
            if tracker == len(N_pool):
                tracker = 0
except:
    print("Sorry terrible damage cannot do that")
    quit()

#Paste walls
check = 0
while True:  
    random_number = randint(0, N - 1)
    if random_number >= len(K_pool):
        if N_pool[random_number - len(K_pool)].wall == 0:
            N_pool[random_number - len(K_pool)].wall = 1
            check += 1
    else:
        if K_pool[random_number].wall == 0:
            K_pool[random_number].wall = 1
            check += 1
    if check == WW:
        break
#Paste holes
check = 0
while True:  
    random_number = randint(0, N - 1)
    if pool[random_number].hole == 0:
        pool[random_number].hole = 1
        check +=1
        if omega == 0:
            pool[random_number].wind_val = 1
        else:
            recursion_wind(random_number, omega, sigma, 1)
    if check == HH:
        break
#Paste monster
check = 0
while True:  
    random_number = randint(0, N - 1)
    if pool[random_number].monster == 0:
        pool[random_number].monster = 1
        check+=1
        if omega == 0:
            pool[random_number].smell_val = 1
        else:
            recursion_smell(random_number, omega, sigma, 1)
    if check == MM:
        break
#Paste gold
check = 0
while True:  
    random_number = randint(0, N - 1)
    if random_number >= len(K_pool):
        if N_pool[random_number - len(K_pool)].gold == 0:
            N_pool[random_number - len(K_pool)].gold = 1
            check += 1
    else:
        if K_pool[random_number].gold == 0:
            K_pool[random_number].gold = 1
            check += 1
    if check == GG:
        break



output(K_pool, N_pool)