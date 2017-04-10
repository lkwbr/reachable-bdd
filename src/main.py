#!/bin/bash
# main.py

"""
Luke Weber, S.I.D. 11398889
CptS 350, Professor Zhe Dang, Ph.D
Washington State University
"""

import sys
from pyeda.boolalg.bdd import (bddvar, expr2bdd, bdd2expr)
from pyeda.boolalg.expr import exprvar

# Custom libs
from parse import *
from reach import five_step_reach

def main():
    """ Driver function: must call with "main.py [some_bdd_file]" """

    # Handle
    if sys.argc < 2: raise TypeError("No BDD file passed!")
    bdd_file = sys.argv[1]

    x1, x2, y1, y2, z1, z2 = map(exprvar, 'abcdef')
    xx1, xx2, yy1, yy2, zz1, zz2 = map(bddvar, 'abcdef')

    # Translating graph edges to bool formulas and BDDs

    #first edge 0-->1, i.e., 00 --> 01
    r = ~x1 & ~x2 & ~y1 & y2
    rr = expr2bdd(r)

    #second edge 1-->2; i.e., 01-->10
    r = r | ( ~x1 & x2 & y1 & ~y2  )
    rr= expr2bdd(r)

    #third edge  2-->3; i.e., 10-->11
    r=r | ( x1 & ~x2 & y1 & y2  )
    rr= expr2bdd(r)

    #fourth edge  3-->0; i.e., 11-->00
    r=r | ( x1 & x2 & ~y1 & ~y2  )
    rr= expr2bdd(r)


    #two step reachability
    hh = rr.compose({yy1:zz1, yy2:zz2}) & rr.compose({xx1:zz1, xx2:zz2})
    hh = hh.smoothing({zz1,zz2})

    #test node 3 can reach node 0 in two steps, which must be false
    assert hh.restrict({xx1:1, xx2:1, yy1:0, yy2:0})

# Let's go
main()
