#!/usr/bin/env python

import argparse
from pprint import pprint
import os
import re
import sys

BASE = "/home/sbb/webapps/beta/sites/all/"
BILLBOARD_DIR = BASE + "themes/sbbtheme/billboard/"
CHF_DIR = BASE + "modules/sbbcompanies/classes/"
CHF = CHF_DIR + "CompanyHelperFunctions.inc.php"
CHF_NEW = CHF_DIR + "CompanyHelperFunctions-new.inc.php"
BB = BILLBOARD_DIR + "billboards.py"
BB_NEW = BILLBOARD_DIR + "billboards-new.py"

parser = argparse.ArgumentParser(description='Add a new company to billboards.py and CompanyHelperFunctions.inc.php.')

parser.add_argument('label', help="The label of the company (used in billboards.py, the name of the billboard file etc.")
parser.add_argument('name', help="The real name of the company. Case-sensitive.")
parser.add_argument('url', help="The URL of the company.")
parser.add_argument('dimensions', help="The dimensions of the image in the billboard of this company in number of squares. Format: [int]x[int]")
parser.add_argument('-t', '--tagline', default="Your tagline", help="The URL of the company.")
parser.add_argument('-b', '--billboard-img', help="The name of the image to be used in the billboard. Default: LABEL-widthxheight.jpg")
parser.add_argument('-f', '--featured-img', help="The name of the image to be used as featured sponsor. Default: LABEL.jpg")
parser.add_argument('-ul', '--url-label', help="The label in the URL (/companies/x).")

args = parser.parse_args()

# parse the dimensions
p = re.compile('([0-9]+)x([0-9]+)')
m = p.match(args.dimensions)
if m is None:
  print "The dimensions should be of format [int]x[int] (both larger than zero). Given: " + args.dimensions + " (label: " + args.label + ")"
  sys.exit()
args.width = int(m.group(1))
args.height = int(m.group(2))
if args.width == 0 or args.height == 0:
  print "The dimensions should be of format [int]x[int] (both larger than zero). Given: " + args.dimensions + " (label: " + args.label + ")"
  sys.exit()

# calculate the images if not given
if args.billboard_img is None:
  args.billboard_img = "{0}-{1}x{2}.png".format(args.label, args.width * 30 + (args.width - 1) * 4,  args.height * 30 + (args.height - 1) * 4)
if args.featured_img is None:
  args.featured_img = "{0}.png".format(args.label)

# set the url label if not given
if args.url_label is None:
  args.url_label = args.label

# check whether the label already exists
bb = open(BB, "r")
for line in bb:
  if line.startswith(args.label):
    print("Label \"{0}\" found in line \"{1}\". Continue?".format(args.label, line))
    if raw_input() != "y":
      sys.exit()
bb.close()

# update CompanyHelperFunctions.inc.php
chf = open(CHF, "r")
chf_new = open(CHF_NEW, "w")
for line in chf:
  chf_new.write(line)
  if "%ANCBTL%" in line:
    chf_new.write("""   '{0}' => array(
      'name' => '{1}',
      'img'=> '{2}',
      'tagline' => '{3}',
      'url' => '{4}',
      'billboard' => 'billboard-{5}.inc.php',
      'percentageSold' => 22
    ),\n""".format(args.url_label, args.name, args.featured_img, args.tagline, args.url, args.label))
os.remove(CHF)
os.rename(CHF_NEW, CHF)
chf.close()
chf_new.close()

# update billboards.py
bb = open(BB, "r")
bb_new = open(BB_NEW, "w")
for line in bb:
  bb_new.write(line)
  if "%ANCBTL%" in line:
    bb_new.write("""
{0} = ShowroomBillboard(Img({1}, {2}, "{3}", "{4}"))
{0}.generate_html_to("billboard-{0}.inc.php")\n""".format(args.label, args.width, args.height, args.billboard_img, args.url))
os.remove(BB)
os.rename(BB_NEW, BB)
bb.close()
bb_new.close()

print "done"
