import networkx as nx
import matplotlib.pyplot as plt
import copy

node_num = int(input("Enter number of nodes(N): "))
connectivity_num = int(input("Enter number of edges(k): "))
leaf_num = int(input("Enter number of borders(K): "))


def output(outwriter):
    file = open("out.txt", "w")
    for x in range(len(outwriter)):
        line = str(x) + ":"
        for y in outwriter[x]:
            line += " " + str(y)
        line += "\n"
        print(line)
        file.write(line)
    file.close()


# Build regular graph
def regular_graph(connectivity_num, node_num):
    try:
        G = nx.random_regular_graph(connectivity_num, node_num)
    except:
        print("Such graph impossible")
        quit()
    output_writer = [[] for i in range(G.number_of_nodes()) ]
    for v1, v2 in G.edges():
        output_writer[v1].append(v2)
        output_writer[v2].append(v1)
    output(output_writer)
    nx.draw(G)
    plt.show()

def break_brain(connectivity_num, node_num, leaf_num):
    add_to_node = []
    try:
        G = nx.random_regular_graph(connectivity_num, node_num - leaf_num)
    except:
        print("Such graph impossible")
        quit()
    edges = copy.deepcopy(G.edges())
    empty = 0
    for v1, v2 in edges:
        if empty == leaf_num:
            break
        G.remove_edge(v1, v2)
        if nx.is_connected(G):
            add_to_node.append(v1)
            add_to_node.append(v2)
            empty += 2
        else:
            G.add_edge(v1, v2)
    if empty != leaf_num:
        print("Such graph impossible")
        quit()
    add_leaf = G.number_of_nodes()
    for x in add_to_node:
        G.add_edge(x, add_leaf)
        add_leaf += 1
    output_writer = [[] for i in range(G.number_of_nodes()) ]
    for v1, v2 in G.edges():
        output_writer[v1].append(v2)
        output_writer[v2].append(v1)   
    output(output_writer)
    nx.draw(G)
    plt.show()

if leaf_num == 0:
    regular_graph(connectivity_num, node_num)
elif leaf_num % 2 == 0:
    break_brain(connectivity_num, node_num, leaf_num)
else:
    print("Such graph is impossible")