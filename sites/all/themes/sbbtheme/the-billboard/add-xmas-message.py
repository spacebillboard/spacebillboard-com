#!/usr/bin/env python

import os
import argparse
import subprocess
import shutil

parser = argparse.ArgumentParser(description='Adds a Christmas message to the billboard (which is also a personal message)')

parser.add_argument('--id', required=True, help="The id of the personal message")
parser.add_argument('--message', required=True, help="The message")
parser.add_argument('--from', required=True, dest="from_", help="The name of the poster of the personal message")
parser.add_argument('--from-is-plural', action='store_true', help="The from field is plural")
parser.add_argument('--to', required=True, help="The name of the poster of the personal message")
parser.add_argument('--to-is-plural', action='store_true', help="The to field is plural")
parser.add_argument('--language', required=True, help="The language of the Christmas Message (supported: \"nl\" | \"en\"")
parser.add_argument('--url', required=False, default="", help="The URL of the homepage of the poster of the personal message")
parser.add_argument('--twitter', required=False, default="", help="The Twitter username of the poster of the personal message")
parser.add_argument('--show-name', action='store_true', help="Show the name of the poster on the Thank You page or not")
parser.add_argument('--show-url', action='store_true', help="Show the URL of the poster on the Thank You page or not")
parser.add_argument('--show-twitter', action='store_true', help="The id of the personal message")

args = parser.parse_args()

# generate the files
from lib.christmas_card_generator import christmas_card_generator
christmas_card_generator.generateAll(args.id, args.message, args.to, args.to_is_plural, args.from_, args.from_is_plural, args.language)
from lib.personal_message_generator import personal_message_generator
# note: do not generate a folding model for Christmas Cards
personal_message_generator.generateCertificate(args.id, args.message, args.from_, args.url, args.twitter, args.show_name, args.show_url, args.show_twitter)

# then add the personal message to the database
from lib.data import data_manager
data_manager.addChristmasMessage(args.id, args.message, args.to, args.to_is_plural, args.from_, args.from_is_plural, args.language, args.url, args.twitter, args.show_name, args.show_url, args.show_twitter)
