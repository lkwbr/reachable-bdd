# reach.py

from pyeda.boolalg.bdd import (bddvar, expr2bdd, bdd2expr)
from pyeda.boolalg.expr import exprvar

def five_step_reach(rr, a, b):
    """
    Determine if two verticies a and b can reach eachother in five steps
    with the given BDD
    """

    # TODO: Generalize to 5-step

    xx1, xx2, yy1, yy2, zz1, zz2 = map(bddvar, 'abcdef')

    #two step reachability
    hh = rr.compose({yy1:zz1, yy2:zz2}) & rr.compose({xx1:zz1, xx2:zz2})
    hh = hh.smoothing({zz1,zz2})

    #test node 3 can reach node 0 in two steps, which must be false
    reachable = hh.restrict({xx1:1, xx2:1, yy1:0, yy2:0})

    return reachable
