class node:
    def __init__(self, id):
        self.id = id
        self.connection = []

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
    for x in K_pool:
        outwriter.append(x.get_con())
    for x in N_pool:
        outwriter.append(x.get_con())
    file = open("out.txt", "w")
    for x in range(len(outwriter)):
        line = str(x) + ":"
        for y in outwriter[x]:
            line += " " + str(y)
        line += "\n"
        file.write(line)
    file.close()


def we_are_cool(N_pool, p):
    for node in N_pool:
        if node.get_len != p:
            return False
    return True


N = int(input("Enter number (N): "))
K = int(input("Enter number (K): "))
k = int(input("Enter number (k): "))
p = int(input("Enter number (p): "))

K_pool = [node(x) for x in range(K)]
N_pool = [node(x) for x in range(K, N)]

tracker = 0
for K_element in K_pool:
    for i in range(k):
        K_element.add_edge(N_pool[tracker].get_id())
        N_pool[tracker].add_edge(K_element.get_id())
        tracker += 1
        if tracker == len(N_pool):
            tracker = 0
if we_are_cool(K_pool, k):
    print("Hard to do")
    quit()         
if level_one(N_pool, p):
    print("Sorry i cannot do that")
    quit()

for node in N_pool:
    if node.get_len() == p:
        continue
    for x in range(len(N_pool)):
        print("node", node.get_id())
        if node.get_len() == p:
            print("Made node", node.get_id())
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
        print("tracker", tracker, node.get_id())
        if tracker == len(N_pool):
            tracker = 0
    print("Made node in for", node.get_id(), node.get_con())

  
if not we_are_cool:
    print("It is sad to say but sry")
    quit()
output(K_pool, N_pool)