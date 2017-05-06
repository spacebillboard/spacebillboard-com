#!/usr/bin/env python

import os
import argparse
import subprocess
import shutil

parser = argparse.ArgumentParser(description='Adds a personal message to the billboard')

parser.add_argument('--id', required=True, help="The id of the personal message")
parser.add_argument('--message', required=True, help="The message")
parser.add_argument('--name', required=True, help="The name of the poster of the personal message")
parser.add_argument('--url', required=False, help="The URL of the homepage of the poster of the personal message")
parser.add_argument('--twitter', required=False, help="The Twitter username of the poster of the personal message")
parser.add_argument('--show-name', action='store_true', help="Show the name of the poster on the Thank You page or not")
parser.add_argument('--show-url', action='store_true', help="Show the URL of the poster on the Thank You page or not")
parser.add_argument('--show-twitter', action='store_true', help="The id of the personal message")

args = parser.parse_args()

# generate the files
from lib.personal_message_generator import personal_message_generator
personal_message_generator.generateAll(args.id, args.message, args.name, args.url, args.twitter, args.show_name, args.show_url, args.show_twitter)

# then add the personal message to the database
from lib.data import data_manager
data_manager.addPersonalMessage(args.id, args.name, args.message, args.url, args.twitter, args.show_name, args.show_url, args.show_twitter)
