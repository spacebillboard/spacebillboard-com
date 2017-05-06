#!/usr/bin/env python

import os
import argparse
import subprocess
import shutil
from lib.data import data_manager

parser = argparse.ArgumentParser(description='Adds a Valentine message to the billboard (which is also a personal message)')

parser.add_argument('--id', required=True, help="The id of the personal message")

args = parser.parse_args()

msg_in_data = data_manager.getPersonalMessage(args.id)
if msg_in_data is None:
  raise Exception("No personal message with id {} found".format(args.id))
args.from_ = msg_in_data['name']
args.message = msg_in_data['message']
args.source = 'be' if msg_in_data['language'] == 'nl' else 'com' 
args.design = msg_in_data['design']
args.to = msg_in_data['to']

# delete the old file
from send2trash import send2trash
send2trash("../../../../../static/valentine/valentine-{}.pdf".format(args.id))

# regenerate the files
from lib.valentine_card_generator import valentine_card_generator
valentine_card_generator.generateAll(args.id, args.message, args.to, args.from_, args.source, args.design)
#from lib.personal_message_generator import personal_message_generator
# note: do not generate a folding model for Valentine Cards
# note: do not generate a certificate for Valentine Cards
#personal_message_generator.generateCertificate(args.id, args.message, args.from_, None, None, args.show_name, False, False)
