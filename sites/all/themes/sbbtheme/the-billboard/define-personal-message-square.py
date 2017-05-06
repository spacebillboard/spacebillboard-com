#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description='Defines a square as personal message square')

parser.add_argument('--row', required=True, type=int, help="The row of the square")
parser.add_argument('--column', required=True, type=int, help="The column of the square")

args = parser.parse_args()

# first test whether this square is not already occupied
from lib.generator import artifact_generator
from lib.billboard import Img, PImg
from lib.data import data_manager
billboard = artifact_generator.buildBillboard(data_manager.load())
if billboard.overlaps(PImg(args.row, args.column, Img(1, 1, "", ""))):
  raise Exception("this square is already taken")
# we are good to go
data_manager.addPersonalMessageSquare(args.row, args.column)
