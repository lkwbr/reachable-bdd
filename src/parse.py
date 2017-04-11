# parse.py

from pyeda.boolalg.bdd import (bddvar, expr2bdd, bdd2expr)
from pyeda.boolalg.expr import exprvar
from functools import reduce
import math

__edge_expressions = []

def bdd_file_parse(f):
    """
    Parse given file f, assuming it is in the correct BDD format;
    translating graph edges to Boolean formulas and BDDs
    """

    global __edge_expressions

    # TODO: Do divide and conquer

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

    # Convert each number to binary
    expr_var_names_xx = ["xx{}".format(i) for i in range(k)]
    expr_var_names_yy = ["yy{}".format(i) for i in range(k)]
    expr_var_names = expr_var_names_xx + expr_var_names_yy
    __edge_expressions = list(map(lambda x: edge_expr(x, k, expr_var_names), \
        edge_nodes))

    # Divide and conquer
    rr = recursive_build(0, len(__edge_expressions) - 1)
    return rr

    # Connect all the expressions and create a bdd
    rr = None
    i = 0
    for r in edge_expressions:
        if rr is None: rr = expr2bdd(r)
        else: rr = rr | expr2bdd(r)

        print("{}/{}".format(i, len(edge_expressions)))
        i += 1

    return rr, k

def recursive_build(a, b):

    if a == b:
        r = __edge_expressions[a]
        return expr2bdd(r)

    split_index = math.floor((b + a) / 2)
    return recursive_build(a, split_index) | recursive_build(split_index + 1, b)

def edge_expr(edge_nodes, k, expr_var_names):
    """
    Get BDD expression from each set of nodes for any given edge; e.g.,
    first edge 0-->1, i.e., 00 --> 01
    r = ~x1 & ~x2 & ~y1 & y2
    """

    # Each BDD variable gets a unique id (w/in the pairs of nodes for the edge)
    var_id = 0

    # For each node of edge, convert each bit to a BDD variable in an expression
    r = None
    for n in edge_nodes:

        node_bin = "{0:0b}".format(n)
        node_bin = "0" * (k - len(node_bin)) + node_bin
        node_bin_list = list(node_bin)

        for node_var_str in node_bin_list:

            # Give each variable a unique name, "v[unique num]"
            uniq_var_id = expr_var_names[var_id]
            var_id += 1

            # Create variable from bit
            node_var = exprvar(uniq_var_id)
            if node_var_str == "0": node_var = ~node_var

            # Update the edge relation
            if r is None: r = node_var
            else: r &= node_var

    return r
