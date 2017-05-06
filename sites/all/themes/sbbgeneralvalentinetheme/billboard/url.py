#!/usr/bin/env python

import argparse
from pprint import pprint
import os
import re
import sys

parser = argparse.ArgumentParser(description='Print out the company URL for a given URL label.')

parser.add_argument('label', nargs='+', help="The label of the company (used in billboards.py, the name of the billboard file etc.")
parser.add_argument('-b', '--beta', action='store_true', help="Print beta URLs.")

args = parser.parse_args()

if args.beta:
  base = "http://beta.spacebillboard.com/companies/"
else:
  base = "http://spacebillboard.com/companies/"

for l in args.label:
  print "{0}{1}".format(base, l)
