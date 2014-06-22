# coding: utf-8
import sys

file_name      = sys.argv[1]
recipe_records = open(file_name, "r").readlines();

for ID, recipe in enumerate(recipe_records):
	print ID, ":", recipe.rstrip()
