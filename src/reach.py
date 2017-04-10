# reach.py

from pyeda.boolalg.bdd import (bddvar, expr2bdd, bdd2expr)
from pyeda.boolalg.expr import exprvar

def five_step_reach(rr, a, b, expr_var_names):
    """
    Determine if two verticies a and b can reach eachother in five steps
    with the given BDD
    """

    # TODO: Generalize to 5-step
    # TODO: Adapt for input a, b
    # TODO: Auto-generate 1024 node BDD

    xx1, xx2, yy1, yy2, zz1, zz2 = map(bddvar, ["v0", "v1", "v2", "v3", "v4", "v5"])

    #two step reachability
    hh = rr.compose({yy1:zz1, yy2:zz2}) & rr.compose({xx1:zz1, xx2:zz2})
    hh = hh.smoothing({zz1, zz2})

    #test node 3 can reach node 0 in two steps, which must be false
    reachable = hh.restrict({xx1:1, xx2:1, yy1:0, yy2:0})

    return reachable
