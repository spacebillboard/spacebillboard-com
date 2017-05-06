#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description='Generates an SVG, PDF and PNG of the current state of the billboard based on the current data.yaml.')
args = parser.parse_args()

from lib.generator import ArtifactGenerator
generator = ArtifactGenerator()
generator.generateFinal()
