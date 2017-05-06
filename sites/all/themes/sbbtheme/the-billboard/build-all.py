#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description='Generate all SpaceBillbaord artifacts based on the current data.yaml.')
args = parser.parse_args()

from lib.generator import ArtifactGenerator
generator = ArtifactGenerator()
generator.generateAll()

# generate the billboard images
import subprocess
subprocess.call("/opt/phantomjs/phantomjs render-billboard-img.js", shell=True)
