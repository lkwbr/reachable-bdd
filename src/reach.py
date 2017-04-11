# reach.py

from pyeda.boolalg.bdd import (bddvar, expr2bdd, bdd2expr)
from pyeda.boolalg.expr import exprvar
from multiprocessing.pool import ThreadPool

def num_step_reach(rr, a, b, k, num_steps = 5):
    """
    Determine if two verticies a and b can reach eachother in variable number
    of steps with the given BDD (default number of steps is 5)
    NOTE: Generalized because I wanted to
    """

    # Help us divide and conquer with multiple threads
    pool = ThreadPool(processes = 1)

    # Create our BDD variables, matching those exactly in rr (except zz's)
    xx_list = [bddvar("xx{}".format(i)) for i in range(k)]
    yy_list = [bddvar("yy{}".format(i)) for i in range(k)]
    zz_list = [bddvar("zz{}".format(i)) for i in range(k)]

    # Compose for each step
    # NOTE: Very slow for many nodes and edges; may want divide and conquer here
    hh = rr
    yyzz_compose_dict = {a:b for a, b in zip(yy_list, zz_list)}
    xxzz_compose_dict = {a:b for a, b in zip(xx_list, zz_list)}
    for i in range(0, num_steps - 1):

        # Kickoff threads on async composition
        yyzz_async_result = pool.apply_async(hh.compose, [yyzz_compose_dict])
        xxzz_async_result = pool.apply_async(rr.compose, [xxzz_compose_dict])

        # Block: get results from threads
        yyzz_compose = yyzz_async_result.get()
        xxzz_compose = xxzz_async_result.get()

        # Conjunct them and do smoothing
        hh = (yyzz_compose & xxzz_compose).smoothing(set(zz_list))
        
        print("\tComposed for step", i)

    print("Number of satisfiable variables", len(list(hh.satisfy_all())))

    # See if a and b can reach eachother in the given number of steps
    restrict_dict = {c:d for c, d in zip(set(xx_list), to_bin(a, k))}
    restrict_dict.update({c:d for c, d in zip(set(yy_list), to_bin(b, k))})
    return hh.restrict(restrict_dict)

def to_bin(num, k):
    node_bin = "{0:0b}".format(num)
    node_bin = "0" * (k - len(node_bin)) + node_bin
    return [int(x) for x in node_bin]
