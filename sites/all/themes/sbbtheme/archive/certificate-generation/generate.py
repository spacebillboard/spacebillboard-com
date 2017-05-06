#!/usr/bin/env python

import argparse
import os
import qrcode
import subprocess
import shutil

parser = argparse.ArgumentParser(description='Generate the certificate for a certain person')

parser.add_argument('name', help="The name of the person to which the certificate is directed") # sequence argument
parser.add_argument('message', help="The message to be put on the certificate") # sequence argument
parser.add_argument('id', help="The id of the message") # sequence argument

args = parser.parse_args()
args.url = "http://spacebillboard.com/messages/{}".format(args.id)

folder = "../../../../../certificates"
tmpqr = "tmpqr.png"
tmpsvg = "tmp.svg"
tmppdf = "tmp.pdf"
tmppng = "tmp.png"

#################################
# Generate the QR code
from qrcode.image.pure import PymagingImage
img = qrcode.make(args.url, image_factory=PymagingImage)
with open(tmpqr, "w+") as out:
  img.save(out)

#################################
# Generate the PDF and PNG
with open("certificate-template.svg", 'r') as template_source:
  template = template_source.read()

template = template.replace("%name%", args.name)
template = template.replace("%message%", args.message)
template = template.replace("%url%", args.url)

with open(tmpsvg, "w+") as sink:
  sink.write(template)

subprocess.call("inkscape -f {} --export-pdf {} --export-dpi 600".format(tmpsvg, tmppdf), shell=True)
subprocess.call("inkscape -f {} --export-png {} --export-dpi 100".format(tmpsvg, tmppng), shell=True)

#################################
# Move the temp files
# TODO test wether the file exists yet first and throw an error
shutil.move(tmppdf, "{}/{}.pdf".format(folder, args.id))
shutil.move(tmppng, "{}/{}.png".format(folder, args.id))

#################################
# Remove the leftovers
os.remove(tmpqr)
os.remove(tmpsvg)
