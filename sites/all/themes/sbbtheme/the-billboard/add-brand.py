#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description='Adds a brand to the billboard')

parser.add_argument('--label', required=True, help="The label of the brand")
parser.add_argument('--name', required=True, help="The name of the brand")
parser.add_argument('--url', required=True, help="The url of the brand")
parser.add_argument('--row', required=True, type=int, help="The row of the logo of the brand on the billboard")
parser.add_argument('--column', required=True, type=int, help="The column of the logo of the brand on the billboard")
parser.add_argument('--width', required=True, type=int, help="The width of the logo of the brand on the billboard")
parser.add_argument('--height', required=True, type=int, help="The height of the logo of the brand on the billboard")

args = parser.parse_args()

# first test whether the required squares are not already occupied
from lib.generator import artifact_generator
from lib.billboard import Img, PImg, OverlapError
from lib.data import data_manager
billboard = artifact_generator.buildBillboard(data_manager.load())
pimg = PImg(args.row, args.column, Img(args.width, args.height, args.label, ""))
overlapping = billboard.overlaps(pimg)
if overlapping is not None:
  raise OverlapError(pimg, overlapping)
# we are good to go
data_manager.addBrand(args.label, args.name, args.url, (args.width, args.height), (args.row, args.column))
