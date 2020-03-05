#!/usr/bin/python
# -*- coding: iso-8859-2 -*-
import re

pattern = '^RUN [0-9][0-9][0-9][0-9][0-9][0-9] COMPLETED. OUTPUT IN FILE (.*).dat.$'

with open('atoms.txt') as atoms:
    for line in atoms:
        # print(line)
        if re.match(pattern, line):
            print(line)