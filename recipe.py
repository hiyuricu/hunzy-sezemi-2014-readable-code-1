# coding: utf-8
import sys

file_name      = sys.argv[1]
assigned_ID    = int(sys.argv[2])
recipe_records = open(file_name, "r").readlines();

for ID, recipe in enumerate(recipe_records):
	if ID == assigned_ID:
		print ID, ":", recipe.rstrip()
