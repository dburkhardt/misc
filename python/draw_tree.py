#!/usr/bin/env python3
from ete3 import Tree, TreeStyle, NodeStyle, TextFace
import sys, argparse

parser = argparse.ArgumentParser(description='Draw newick trees')
parser.add_argument('tree', type=str, nargs=1,
                    help='newick tree string')
parser.add_argument('outfile', type=str, nargs=1,
                    help='path to store tree image')
parser.add_argument('-f', dest='format', type=int, nargs=1, default=0,
                    help='newick tree format')
parser.add_argument('-r', dest='rotated', type=int, nargs=1, default=0,
                    help='should the tree be rotated top to bottom? [0/no], 1/yes')

args = parser.parse_args()
ts = TreeStyle()
if args.rotated == 1:
    ts.show_leaf_name=True
    ts.rotation = 90

ns  = NodeStyle()
ns['size'] = 8

t = Tree(args.tree[0], format=args.format[0])
for n in t.traverse():
    n.set_style(ns)
    if not n.is_leaf():
        n.add_face(TextFace(text=n.name.rjust(2), ftype='Courier'), column=-1)

t.render(args.outfile[0], w=400, units='mm', tree_style=ts)
