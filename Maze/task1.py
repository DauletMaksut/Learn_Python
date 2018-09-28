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
p = int(input("Enter number (p): "))
K = int(input("Enter number (K): "))
k = int(input("Enter number (k): "))

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
if level_one(N_pool, p):
    print("Sorry i cannot do that")
    quit()
end = tracker
for node in N_pool:
    for x in N_pool:
        if len(N_pool) == end:
            end = tracker
            break
        if node.get_len() == p:
            print('exit,',node.get_id(),node.get_con())
            break
        if node.get_id() == N_pool[end].get_id():
            continue
        if N_pool[end].get_len() == p:
            continue
        node.add_edge(N_pool[end].get_id())
        N_pool[end].add_edge(node.get_id())
        end += 1
    print("mnb")
    # for r_node in N_pool:
    #     if node.get_len() == p:
    #         break
    #     if r_node.get_len() == p:
    #         continue
    #     if r_node.get_id() == node.get_id():
    #         continue 
    #     if node.get_id() in r_node.get_con():
    #         continue
    #     node.add_edge(r_node.get_id())
    #     r_node.add_edge(node.get_id())

        
if not we_are_cool:
    print("It is sad to say but sry")
    quit()

    # for i in range(len(N_pool)):
    #     for y in range(len(N_pool)):
    #         max_node -= 1
    #         if max_node == -1:
    #             max_node = len(N_pool) - 1
    #         if N_pool[max_node].get_len() != p
    #             break
    #     for z in range(len(N_pool) - 1):
    #         if N_pool[min_node]
            

        
    #     if N_pool[min_node].get_id() not in N_pool[max_node].get_con():
    #         N_pool[min_node].add_edge(N_pool[max_node].get_id())
    #         N_pool[max_node].add_edge(N_pool[min_node].get_id())

# while not we_are_cool(N_pool, p):
#     print("Suka")
#     current_node = N_pool[take_node]
#     tmp = take_node
#     for i in range(len(N_pool) - 1):
#         tmp+=1
#         change_len = current_node.get_len()
#         if tmp == len(N_pool):
#             tmp = 0
#         if N_pool[tmp].get_len != p:
#             current_node.add_edge(N_pool[tmp].get_id())
#             N_pool[tmp].add_edge(current_node.get_id())
#             if current_node.get_len != change_len:
#                 break
#     take_node += 1
#     if take_node == len(N_pool):
#         take_node = 0
    # if take_node == tracker:
    #     print("Emm, but nio nio nio i won't do that")
    #     quit()
output(K_pool, N_pool)