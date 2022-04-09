"""
Written by WENG XINN CHOW @ 04.04.2020
Python script for Blank Page CTF Challenge
"""

file = open("blank page - task.txt", "r").read()
output = ""
for c in file:
	# Space
	if ord(c) == 32:
		output += "0"
	# Dots
	else:
		output += "1"
print(output)