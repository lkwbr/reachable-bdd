# reach.py

from pyeda.boolalg.bdd import (bddvar, expr2bdd, bdd2expr)
from pyeda.boolalg.expr import exprvar

def five_step_reach(rr, a, b, k):
    """
    Determine if two verticies a and b can reach eachother in five steps
    with the given BDD
    """

    # NOTE: Created this so you can vary the number of steps dynamically
    num_steps = 5

    # Create our BDD variables, matching those exactly in rr (except zz's)
    xx_list = [bddvar("xx{}".format(i)) for i in range(k)]
    yy_list = [bddvar("yy{}".format(i)) for i in range(k)]
    zz_list = [bddvar("zz{}".format(i)) for i in range(k)]

    # Compose for each step
    hh = rr
    for i in range(0, num_steps - 1):
        yyzz_compose_dict = {a:b for a, b in zip(yy_list, zz_list)}
        xxzz_compose_dict = {a:b for a, b in zip(xx_list, zz_list)}
        hh = (hh.compose(yyzz_compose_dict) & rr.compose(xxzz_compose_dict))\
            .smoothing(set(zz_list))

    print("all satisfied", list(hh.satisfy_all()))

    # See if a and b can reach eachother in the given number of steps
    restrict_dict = {c:d for c, d in zip(set(xx_list), to_bin(a, k))}
    restrict_dict.update({c:d for c, d in zip(set(yy_list), to_bin(b, k))})
    return hh.restrict(restrict_dict)

def to_bin(num, k):
    node_bin = "{0:0b}".format(num)
    node_bin = "0" * (k - len(node_bin)) + node_bin
    return [int(x) for x in node_bin]
