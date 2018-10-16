import random
import copy

N = int(input("Enter number (N): "))
K = int(input("Enter number (K): "))
k = int(input("Enter number (k): "))
p = int(input("Enter number (p): "))
WW = int(input("Enter number (WW): "))
HH = int(input("Enter number (HH): "))
MM = int(input("Enter number (MM): "))
GG = int(input("Enter number (GG): "))
T_num = int(input("Enter number of teleports: "))
omega = int(input("Enter spread number don't find sigma ⍬: "))
sigma = float(input("Enter decay rate number (omega ⍵): "))
sim_steps = int(input("Enter simulation steps: "))
class node:
    def __init__(self, id, edges):
        self.id = id
        self.connection = []
        self.edges = edges
        self.monster = 0
        self.hole = 0
        self.wall = 0
        self.gold = 0
        self.wind_val = 0
        self.smell_val = 0
        self.free = True
        self.port = 0
        self.visited = 0 

class Monster:
    def __init__(self, currentplace):
        self.current_state = currentplace
        self.next_state = 0
        self.moved = 0

def recursion_wind(node_num, omega, sigma, val):
    if omega == -1:
        return
    pool[node_num].wind_val = val
    for x in pool[node_num].connection:
        if pool[x].wind_val >= val * sigma:
            continue
        recursion_wind(x, omega - 1, sigma, val * sigma)

def recursion_smell(node_num, omega, sigma, val):
    if omega == -1:
        return
    pool[node_num].smell_val = val
    for x in pool[node_num].connection:
        if pool[x].smell_val >= val * sigma:
            continue
        recursion_smell(x, omega - 1, sigma, val * sigma)

def checkGraph(node_num):
    if pool[node_num].visited == 1:
        return False
    pool[node_num].visited = 1
    check.add(node_num)
    if len(check) == N:
        return True
    for x in pool[node_num].connection:
        checkGraph(x)
    if len(check) == N:
        return True
    return False

# Init maze
K_pool = [node(x, k) for x in range(K)]
N_pool = [node(x, p) for x in range(K, N)]
pool = []
for x in K_pool:
    pool.append(x)
for x in N_pool:
    pool.append(x)

node_num = len(pool) - 1
min = pool[0]
max = pool[len(pool) - 1]
while True:
    for x in pool:
        if x.edges == 0:
            continue
        if x.edges <= min.edges and x.edges != 0 and min != x:
            min = x
        
    for x in range(len(pool)):
        if pool[node_num - x].edges == 0:
            continue
        if pool[node_num - x].edges >= max.edges and pool[node_num - x].edges != max.edges:
            max = pool[node_num - x]
    if (not (min.id in max.connection)) and min != max:
        min.connection.append(max.id)
        min.edges -= 1
        max.connection.append(min.id)
        max.edges -= 1

    if min.edges == 0:
        for x in pool:
            if x.edges > 0:
                min = x
    if max.edges == 0:
        for x in pool:
            if x.edges > 0:
                max = x
    
    num = 0
    for x in pool:
        if x.edges == 0:
            num += 1
    if num == len(pool):
        break
#End creation of maze

check = set()
if not checkGraph(0):
    print("Cannot create such maze")
    quit()

# #Testtest
# for x in pool:
#     print(x.connection)


# Init monster
monster = set()
res_room = set()
while len(monster) < MM:
    num = random.randint(0, N - 1)
    if not ( num in res_room):
        res_room.add(num)
        pool[num].free = False
        pool[num].monster = 1
        move_to = random.randint(0, len(pool[num].connection) - 1 )
        tmp = Monster(num)
        tmp.next_state = pool[num].connection[move_to]
        recursion_smell(num, omega, sigma, 1)
        monster.add(tmp)

# Init hole
hole = set()
while len(hole) < HH:
    num = random.randint(0, N - 1)
    if pool[num].free:
        pool[num].free = False
        hole.add(num)
        pool[num].hole = 1
        recursion_wind(num, omega, sigma, 1)

# Init wall
wall = set()
while len(wall) < WW:
    num = random.randint(0, N - 1)
    if pool[num].free:
        pool[num].free = False
        wall.add(num)
        pool[num].wall = 1
   
# Init gold
gold = set()
while len(gold) < GG:
    num = random.randint(0, N - 1)
    if pool[num].free:
        pool[num].free = False
        gold.add(num)
        pool[num].gold = 1
  
# Enter the number of overall nodes
teleport = set()
while len(teleport) < T_num:
    num = random.randint(0, N - 1)
    if pool[num].free:
        pool[num].free = False
        teleport.add(num)
        pool[num].port = 1


# file = open("text.txt", "r")

print()
print()
print("Mosnter is moving")
global_clock = 0

while True:
    for x in pool:
        if x.smell_val > 0: 
            x.smell_val = 1
        if x.wind_val > 0: 
            x.wind_val = 1
    print()
    print()
    print("Round", global_clock + 1)
    if global_clock != 0:
        for iter in range(len(pool)):
            if clone_pool[iter].smell_val != pool[iter].smell_val or clone_pool[iter].monster != pool[iter].monster:
                line = str(pool[iter].id) +":" + str(pool[iter].wall) +","+ str(pool[iter].hole) +","+  str(pool[iter].monster) +","+  str(pool[iter].gold) +","+ str(pool[iter].wind_val) +","+ str(pool[iter].smell_val)
                for elem in pool[iter].connection:
                    line +=  " " + str(elem) 
                print(line)
        last_res.close()

    if global_clock != 0:
        last_res = open("out.txt", "w")
        for iter in range(len(pool)):
            line = str(pool[iter].id) +":" + str(pool[iter].wall) +","+ str(pool[iter].hole) +","+  str(pool[iter].monster) +","+  str(pool[iter].gold) +","+ str(pool[iter].wind_val) +","+ str(pool[iter].smell_val)
            for elem in pool[iter].connection:
                line +=  " " + str(elem) 
            line += "\n"
            last_res.write(line)
        last_res.close()


    if global_clock == 0:
        last_res = open("out.txt", "w")
        for x in pool:
            line = str(x.id) +":" + str(x.wall) +","+ str(x.hole) +","+  str(x.monster) +","+  str(x.gold) +","+ str(x.wind_val) +","+ str(x.smell_val)
            for elem in x.connection:
                line +=  " " + str(elem) 
            print(line)
            last_res.write(line) 
        line += "\n"
        last_res.close()
    clone_pool = copy.deepcopy(pool)

    for i in pool:
        i.smell_val = 0
    for x in monster:
        tmp = pool[x.current_state]
        if pool[x.next_state].wall == 1:
            x.current_state = x.next_state
            recursion_smell(x.current_state, omega, sigma , 1)
            x.next_state = tmp.id
            continue
        if pool[x.next_state].hole == 1:
            x.current_state = x.next_state
            recursion_smell(x.current_state, omega, sigma , 1)
            x.next_state = tmp.id
            continue
        
        if pool[x.current_state].port == 1 and x.moved != 1:
            x.next_state = list(teleport)[ random.randint(0, len(teleport) - 1)]
            x.moved = 1
            for x in teleport:
                pool[x].smell_val = 1
            continue
        x.moved = 0
        x.current_state = x.next_state
        x.next_state = pool[x.current_state].connection[ random.randint(0, len(pool[x.next_state].connection) - 1) ]


    global_clock += 1
    if global_clock == sim_steps:
        break
