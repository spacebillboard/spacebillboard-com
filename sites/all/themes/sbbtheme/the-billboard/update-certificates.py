#!/usr/bin/env python

import os
import argparse
import subprocess
import shutil
from lib.data import data_manager

parser = argparse.ArgumentParser(description='Update the certificates for a certain id again by just creating them again and saving them over the previous ones.')

parser.add_argument('id', help="The id of the personal message")

args = parser.parse_args()

# first set up the variables
args.msgurl = "http://spacebillboard.com/messages/{}".format(args.id)
msg_in_data = data_manager.getPersonalMessage(args.id)
if msg_in_data is None:
  raise Exception("No personal message with id {} found".format(args.id))
args.name = msg_in_data['name']
args.message = msg_in_data['message']

folder = "../../../../../certificates"
tmpqr = "tmpqr.png"
tmpsvg = "tmp.svg"
tmpsvg_for_sharing = "tmp-for-sharing.svg"
tmppdf = "tmp.pdf"
tmppng = "tmp.png"
tmppng_for_sharing = "tmp-for-sharing.png"
tmpjpg = "tmp.jpg"
tmpjpg_for_sharing = "tmp-for-sharing.jpg"

#################################
# Generate the QR code
import qrcode
from qrcode.image.pure import PymagingImage
img = qrcode.make(args.msgurl, image_factory=PymagingImage)
with open(tmpqr, "w+") as out:
  img.save(out)

#################################
# Generate the PDF and PNG
def process_template(path):
  with open(path, 'r') as template_source:
    template = template_source.read()

  import textwrap
  wrapped_message = textwrap.wrap(args.message, 50)
  # HTML encode here (e.g., again errors with &)
  import cgi
  for i in range(len(wrapped_message)):
    wrapped_message[i] = cgi.escape(wrapped_message[i])
  # now put the message in the svg
  if len(wrapped_message) == 1:
    template = template.replace("%message1%", "")
    template = template.replace("%message2%", wrapped_message[0])
    template = template.replace("%message3%", "")
  elif len(wrapped_message) == 2:
    template = template.replace("%message1%", wrapped_message[0])
    template = template.replace("%message2%", wrapped_message[1])
    template = template.replace("%message3%", "")
  elif len(wrapped_message) == 3:
    template = template.replace("%message1%", wrapped_message[0])
    template = template.replace("%message2%", wrapped_message[1])
    template = template.replace("%message3%", wrapped_message[2])

  template = template.replace("%name%", cgi.escape(args.name))
  template = template.replace("%url%", cgi.escape(args.msgurl))
  return template

with open(tmpsvg, "w+") as sink:
  template = process_template("templates/certificate.svg")
  sink.write(template)

with open(tmpsvg_for_sharing, "w+") as sink:
  template = process_template("templates/certificate-for-sharing.svg")
  sink.write(template)

subprocess.call("inkscape -f {} --export-pdf {} --export-area-page --export-dpi 600".format(tmpsvg, tmppdf), shell=True)
subprocess.call("inkscape -f {} --export-png {} --export-area-page --export-dpi 150".format(tmpsvg, tmppng), shell=True)
subprocess.call("inkscape -f {} --export-png {} --export-area-page --export-width 500".format(tmpsvg_for_sharing, tmppng_for_sharing), shell=True)
subprocess.call("mogrify -format jpg -quality 95 {}".format(tmppng), shell=True)
subprocess.call("mogrify -format jpg -quality 95 {}".format(tmppng_for_sharing), shell=True)

#################################
# Move the pdf and pngs
shutil.move(tmppdf, "{}/{}.pdf".format(folder, args.id))
shutil.move(tmpjpg, "{}/{}.jpg".format(folder, args.id))
shutil.move(tmpjpg_for_sharing, "{}/{}-for-sharing.jpg".format(folder, args.id))

#################################
# Move the other temp files to trash
from send2trash import send2trash
defqr = "{}-qr.png".format(args.id)
defsvg = "{}.svg".format(args.id)
defsvg_for_sharing = "{}-for-sharing.svg".format(args.id)
defpng = "{}.png".format(args.id)
defpng_for_sharing = "{}-for-sharing.png".format(args.id)
shutil.move(tmpqr, defqr)
shutil.move(tmpsvg, defsvg)
shutil.move(tmpsvg_for_sharing, defsvg_for_sharing)
shutil.move(tmppng, defpng)
shutil.move(tmppng_for_sharing, defpng_for_sharing)
send2trash(defqr)
send2trash(defsvg)
send2trash(defsvg_for_sharing)
send2trash(defpng)
send2trash(defpng_for_sharing)
