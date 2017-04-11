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
from reach import num_step_reach
from gen import generate_graph

# Custom graph params
__custom_graph_len = 1024
__graph_folder = "graphs"
__custom_graph_file_loc = "{}/{}_custom.graph".format(__graph_folder, __custom_graph_len)

def main():
    """
    Driver function: must call with the following syntax:
    "./main.py [some_bdd_file_path]"
    """

    # Handle incoming BDD file, constructing if there; otherwise,
    # randomly generate graph of predefined size
    if len(sys.argv) < 2:
        graph_file = __custom_graph_file_loc
        generate_graph(__custom_graph_len, graph_file)
        print("Generated random BDD with {} nodes".format(__custom_graph_len))
    else: graph_file = sys.argv[1]
    rr, k = bdd_file_parse(graph_file)
    print("Done parsing BDD file ")

    # See if given vertices are reachable in five steps
    target_vertices = (3, 0)
    num_steps = 5
    print("Determine reachability of {} in {} steps".format(target_vertices, \
        num_steps))
    reachable = num_step_reach(rr, *target_vertices, k, num_steps)
    if bool(reachable): print("Reachable!")
    else: print("Unreachable!")

# Let's go
main()
