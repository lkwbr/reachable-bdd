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
from parse import bdd_file_parse
from reach import five_step_reach

def main():
    """ Driver function: must call with "main.py [some_bdd_file]" """

    # Handle incoming BDD file, constructing if there
    if len(sys.argv) < 2: raise TypeError("No BDD file passed!")
    rr = bdd_file_parse(sys.argv[1])

    # See if given vertices are reachable in five steps
    reachable = five_step_reach(rr, 1, 0)
    assert reachable

# Let's go
main()