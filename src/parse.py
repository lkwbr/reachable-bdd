# parse.py

from pyeda.boolalg.bdd import (bddvar, expr2bdd, bdd2expr)
from pyeda.boolalg.expr import exprvar
from functools import reduce
import math

var_id = 0

def bdd_file_parse(f):
    """
    Parse given file f, assuming it is in the correct BDD format;
    Translating graph edges to Boolean formulas and BDDs
    """

    # Parse all edge node numbers
    with open(f) as bdd_file:
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
    edge_expressions = list(map(lambda x: binary_vector(x, k), edge_nodes))
    print(binary_nodes)

    # Connect all the expressions and create a bdd
    rr = None
    r = None
    for re in edge_expressions:

        # Update relation
        if r is None: r = re
        else: r |= re

        # Update BDD
        rr = expr2bdd(r)

    return rr

    # TODO: Remove below, as this is outdated

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

def binary_vector(edge_nodes, k):
    """
    Convert decimal number 10 into binary vector, e.g., 3 to [0, 0, 1, 1] for
    x = 3, k = 4, where x is in edge_nodes
    """

    global var_id

    # For each node of edge, convert each bit to a BDD variable in an expression
    r = None
    for n in edge_nodes:

        node_bin = "{0:0b}".format(n)
        node_bin = "b" + "0" * (k - len(node_bin)) + node_bin
        node_bin_list = list(node_bin)

        for node_var_str in node_bin_list

            print(node_var_str)

            # Give each variable a unique name, "#[unique num]"
            uniq_var_id = "#" + str(var_id)
            var_id += 1

            # Create variable from bit
            node_var = exprvar(uniq_var_id)
            if node_var_str == "0": node_var = ~node_var

            # Update the edge relation
            if r is None: r = node_expr_var
            else: r &= node_expr_var

    return r
