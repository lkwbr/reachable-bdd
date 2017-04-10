#!/bin/bash
# main.py

"""
Luke Weber, S.I.D. 11398889
CptS 350, Course Project
Professor Zhe Dang, Ph.D
Washington State University
"""

# Standard/third-party libs
import sys
from pyeda.boolalg.bdd import (bddvar, expr2bdd, bdd2expr)
from pyeda.boolalg.expr import exprvar

# Custom libs
from parse import bdd_file_parse
from reach import five_step_reach

def main():
    """
    Driver function: must call with the following syntax:
    "./main.py [some_bdd_file_path]"
    """

    # Handle incoming BDD file, constructing if there
    if len(sys.argv) < 2: raise TypeError("No BDD graph file passed!")
    rr, k = bdd_file_parse(sys.argv[1])

    # See if given vertices are reachable in five steps
    target_vertices = (3, 1)
    reachable = five_step_reach(rr, *target_vertices, k)
    print(target_vertices, reachable)

# Let's go
main()
