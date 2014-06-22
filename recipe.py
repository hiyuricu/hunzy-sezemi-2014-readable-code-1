# coding: utf-8
import sys

file_name      = sys.argv[1]
recipe_records = open(file_name, "r").readlines();

for recipe in recipe_records:
	print recipe.rstrip()
