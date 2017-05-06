#!/usr/bin/env python

import os
import argparse
import subprocess
import shutil

parser = argparse.ArgumentParser(description='Adds a Valentine message to the billboard (which is also a personal message)')

parser.add_argument('--id', required=True, help="The id of the personal message")
parser.add_argument('--message', required=True, help="The message")
parser.add_argument('--from', required=True, dest="from_", help="The name of the poster of the personal message")
parser.add_argument('--to', required=True, help="The name of the poster of the personal message")
parser.add_argument('--source', required=True, help="The type of the Valentine Message", choices=['com', 'be', 'nl'])
parser.add_argument('--design', required=True, help="The design of the Valentine card to use", choices=['cedric','pell','darkyr','lejla','tjorven'])
parser.add_argument('--show-name', action='store_true', help="Show the name of the poster on the Thank You page or not")

args = parser.parse_args()

# generate the files
from lib.valentine_card_generator import valentine_card_generator
valentine_card_generator.generateAll(args.id, args.message, args.to, args.from_, args.source, args.design)
from lib.personal_message_generator import personal_message_generator
# note: do not generate a folding model for Valentine Cards
# note: do not generate a certificate for Valentine Cards
#personal_message_generator.generateCertificate(args.id, args.message, args.from_, None, None, args.show_name, False, False)

# then add the personal message to the database
#from lib.data import data_manager
#data_manager.addValentineMessage(args.id, args.message, args.to, args.from_, args.source, args.design, args.show_name)
