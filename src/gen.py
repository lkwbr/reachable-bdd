# gen.py

import random

def generate_graph(n, fn):
    """
    Generate random graph with the given number of nodes n, writing to the
    given filename fn within the graphs/ folder
    """

    # NOTE: Fraction must be greater than or equal to 1
    edge_to_node_fract = 2 / 1
    m = int(edge_to_node_fract * n)

    with open(fn, "w+") as f:

        # (1) Connect every node to an edge
        node_list = list(range(n))
        random.shuffle(node_list)
        for i in range(0, n, 2):
            u, v = (node_list[i], node_list[i + 1])
            edge = "{} {}".format(v, u)
            print(edge, file = f)

        # (2) With the leftover allotted edges, randomly connect nodes
        remaining_nodes = m - n
        for i in range(0, remaining_nodes):
            u, v = (random.randint(0, n), random.randint(0, n))
            edge = "{} {}".format(v, u)
            print(edge, file = f)
