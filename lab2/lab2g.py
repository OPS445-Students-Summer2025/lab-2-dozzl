#!/usr/bin/env python3
#Author: Fahad Rajper
#AuthorID:115398174
#date created: 2025/28/5
import sys

if len(sys.argv) > 1:
    timer = int(sys.argv[1])
else:
    timer = 3

while timer != 0:
    print(timer)
    timer = timer - 1

print('blast off!')
