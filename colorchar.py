#!/usr/bin/env python3
#Author: Richard Barnes (rbarnes@umn.edu)

import argparse
import re

reset_color     = "\033[39m"
char_color      = dict()
char_color['1'] = '\033[35m'
char_color['2'] = '\033[34m'
char_color['3'] = '\033[33m'


parser = argparse.ArgumentParser()
parser.add_argument('--input',    '-i', type = argparse.FileType('r'), default = '-')
parser.add_argument('--boundary', '-b', action="store_const", const=True, default=False)
args = parser.parse_args()

for line in args.input:
  if args.boundary:
    for k,v in char_color.items():
      line = re.sub(r'(?<=\b)'+k+r'(?=\b)',v+k+reset_color,line)
  else: #TODO: Find a faster way of doing the following
    line_rep = ""
    for i in range(len(line)):
      if line[i] in char_color:
        line_rep += char_color[line[i]]+line[i]+reset_color
      else:
        line_rep += line[i]
    line = line_rep
  print(line, end="")

print(reset_color)