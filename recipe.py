# coding: utf-8

recipe_records = open("recipe-records.txt", "r").readlines();

for recipe in recipe_records:
	print recipe.rstrip()
