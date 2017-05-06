#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description='Prints characteristics about personal messages')
args = parser.parse_args()

from lib.data import data_manager, personal_message_squares, brands, personal_messages
data = data_manager.load()
from pprint import pprint

# Helper class
class Stats:
  
  def __init__(self, label):
    self.label = label
    self.counters = {}

  def count(self, key):
    if key in self.counters:
      self.counters[key] = self.counters[key] + 1
    else:
      self.counters[key] = 1

  def pprint(self):
    print("{}:".format(self.label))
    for key, value in self.counters.iteritems():
      print("- {}: {}".format(key, value))

# Built the stats
number = len(data[personal_messages])
total_length = 0
types = Stats("Types")
valentine_designs = Stats("Valentine designs")
for msg in data[personal_messages]:
  total_length = total_length + len(msg['message'])
  if 'type' not in msg or msg['type'] is None:
    types.count("normal")
  else:
    types.count(msg['type'])
    if msg['type'] == 'valentine':
      valentine_designs.count(msg['design'])

# Print
print("Total number of personal messages: {}".format(number))
print("Mean length: {} characters".format(total_length / number))
print("")
types.pprint()
print("")
valentine_designs.pprint()
