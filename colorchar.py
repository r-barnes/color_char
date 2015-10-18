#!/usr/bin/env python3
#Author: Richard Barnes (rbarnes@umn.edu)

import argparse

char_color      = dict()
char_color['1'] = '\033[35m'
char_color['3'] = '\033[33m'


parser = argparse.ArgumentParser()
parser.add_argument('--input', '-i', type = argparse.FileType('r'), default = '-')
args = parser.parse_args()

for line in args.input:
  for k,v in char_color.items():
    line = line.replace(k,v+k)
  print(line, end="")


print("\033[39m")