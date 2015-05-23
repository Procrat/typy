#!/bin/python3

import csv
import sys
import time

with open(sys.argv[1]) as log:
	for line in log:
		print(line.trim())
		time.sleep(1)