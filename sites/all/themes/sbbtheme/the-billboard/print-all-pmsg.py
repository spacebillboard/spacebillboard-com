#!/usr/bin/env python

import argparse
import sys
import textwrap

parser = argparse.ArgumentParser(description='Prints characteristics about personal messages')
#parser.add_argument('--width', type=int, default=sys.maxint, help='The width of the text block to output. Leave out for inifinite.')
args = parser.parse_args()

from lib.data import data_manager, personal_message_squares, brands, personal_messages
data = data_manager.load()

messages = map(lambda x: x['message'], data[personal_messages])
total = ''.join(messages).replace('\n','')
print total
#print '\n'.join(textwrap.wrap(total, args.width))
