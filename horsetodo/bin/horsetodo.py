#!/usr/bin/env python

import horsetodo
import argparse

parser = argparse.ArgumentParser(description="A simple TODO script", add_help=True)

parser.add_argument('--add', '-a', type=str)
parser.add_argument('--remove', '-r', type=int)

args = parser.parse_args()

print(f"{args.add}\n{args.remove}")