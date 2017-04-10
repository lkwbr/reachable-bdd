# reach.py

from pyeda.boolalg.bdd import (bddvar, expr2bdd, bdd2expr)
from pyeda.boolalg.expr import exprvar

def five_step_reach(rr, a, b, k):
    """
    Determine if two verticies a and b can reach eachother in five steps
    with the given BDD
    """

    # TODO: Generalize to 5-step
    # TODO: Auto-generate 1024 node BDD

    # TODO: Have more xx1, xx2, ... for length of k

    var_base = 0
    var_coll = []
    num_steps = 2

    # Get start and end expressions covered
    var_set_start = [bddvar("b{}".format(i + var_base)) for i in range(k)]
    var_base += k
    var_set_end = [bddvar("b{}".format(i + var_base)) for i in range(k)]
    var_base += k
    var_coll.append(var_set_start)
    var_coll.append(var_set_end)

    # Now cover all intermediate
    for s in range(num_steps - 1):

        var_set = [bddvar("b{}".format(i + var_base)) for i in range(k)]
        var_base += k

        var_coll.append(var_set)

    # Two step reachability
    for
    hh = rr.compose({yy1:zz1, yy2:zz2}) & rr.compose({xx1:zz1, xx2:zz2})
    hh = hh.smoothing({zz1, zz2})

    a_bin = to_bin(a, k)
    b_bin = to_bin(b, k)

    restrict_dict = {c:d for c, d in zip(var_set_start, a_bin)}
    restrict_dict.update({c:d for c, d in zip(var_set_end, b_bin)})
    print(restrict_dict)

    # See if node a can reach node b in 5 steps
    reachable = hh.restrict(restrict_dict)
    return reachable


    # TODO: Remove lower stuff

    xx1, xx2, yy1, yy2, zz1, zz2 = map(bddvar, ["v0", "v1", "v2", "v3", "v4", "v5"])

    # Two step reachability
    hh = rr.compose({yy1:zz1, yy2:zz2}) & rr.compose({xx1:zz1, xx2:zz2})
    hh = hh.smoothing({zz1, zz2})

    a_bin = to_bin(a, k)
    b_bin = to_bin(b, k)

    restrict_dict_a = {c:d for c, d in zip(var_set_start, a_bin)}
    restrict_dict_b = {c:d for c, d in zip(var_set_end, b_bin)}

    # See if node a can reach node b in 5 steps
    reachable = hh.restrict({xx1:1, xx2:1, yy1:0, yy2:0})

    return reachable

def to_bin(num, k):
    node_bin = "{0:0b}".format(n)
    node_bin = "0" * (k - len(node_bin)) + node_bin
    return [int(x) for x in node_bin]
