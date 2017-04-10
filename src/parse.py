# parse.py

from pyeda.boolalg.bdd import (bddvar, expr2bdd, bdd2expr)
from pyeda.boolalg.expr import exprvar
from functools import reduce
import math

def bdd_file_parse(f):
    """
    Parse given file f, assuming it is in the correct BDD format;
    Translating graph edges to Boolean formulas and BDDs
    """

    with open(f) as bdd_file:

        # Parse all edge node numbers
        edge_nodes = list(map(lambda x: list(map(int, x.split())), \
            bdd_file.readlines()))

    # Get number of unique nodes
    nodes = set()
    for en in edge_nodes:
        nodes.add(en[0])
        nodes.add(en[1])
    n = len(nodes)
    k = math.ceil(math.log(n, 2))
    print(n, k)

    # Convert each number to binary
    binary_nodes = list(map(lambda x: binary_vector(x, k), edge_nodes))
    print(binary_nodes)

    # TODO: here

    x1, x2, y1, y2, z1, z2 = map(exprvar, 'abcdef')

    #first edge 0-->1, i.e., 00 --> 01
    r = ~x1 & ~x2 & ~y1 & y2
    rr = expr2bdd(r)

    #second edge 1-->2; i.e., 01-->10
    r = r | ( ~x1 & x2 & y1 & ~y2  )
    rr = expr2bdd(r)

    #third edge  2-->3; i.e., 10-->11
    r = r | ( x1 & ~x2 & y1 & y2  )
    rr = expr2bdd(r)

    #fourth edge  3-->0; i.e., 11-->00
    r = r | ( x1 & x2 & ~y1 & ~y2  )
    rr = expr2bdd(r)

    return rr

def binary_vector(x, k):
    """
    Convert decimal number 10 into binary vector, e.g., 3 to [0, 0, 1, 1] for
    x = 3, k = 4
    """

    # Two nodes connected by edge
    node_list = [n for n in x]

    # Get binary of number for each node
    node_binary_list = []
    r = None
    for n in node_list:
        node_bin = "{0:0b}".format(n)
        node_bin = "b" + "0" * (k - len(node_bin)) + node_bin
        print(node_bin)

        node_expr_var = exprvar(node_bin)

        if r is None: r = node_expr_var
        else: r &= node_expr_var

        #bin_vect = [int(v) for v in list("{0:0b}".format(n))]
        #bin_vect = [0] * (k - len(bin_vect)) + bin_vect
        #node_binary_list.append(bin_vect)

    a = exprvar("".join(bin_node))
    expr_vect = []

    return bin_vect
