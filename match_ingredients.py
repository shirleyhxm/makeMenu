#!/usr/bin/python

def matchRecipe( items , recipes ):
	"This gives you the minimal amount of ingredients"
	incompleteDishes = {}
	dishes = []
	sorted(items)
	for recipe in recipes:
		if set(recipes[recipe]) < set(items):
			dishes.append(recipe)
		else:
			if len(set(recipes[recipe]) - set(items)) <= 3:
				incompleteDishes[recipe] = set(recipes[recipe]) - set(items)
			if len(dishes) != 0:
				for dish in dishes:
					#print(dish)
					pass
	
			else:
				print('Lack ingredients:')
				for dish in incompleteDishes:
					print(dish + ': ' + ' '.join(list(incompleteDishes[dish])))
	return dishes


### Test cases ####

#items = ['onion', 'tofu', 'beef']
#recipes = {'Onion soup': ['onion'], 'Mapo': ['tofu', 'onion'], 'Hongshao': ['pork']}
#recipes = {'Onion soup': ['onion','potato'], 'Burger': ['lettuce','bread','patty'], 'Hongshao': ['pork']}

#items = ['a','b','c','d']
#recipes = {'A':['a','b'], 'B':['a','d'], 'C':['a','b','c','d','e'], 'D':['a','b','c','d','e','f','g','h'], 'E':['c','g','h'],'F':['c','g','h','u','i']}
#recipes = {'C':['a','b','c','d','e'], 'D':['a','b','c','d','e','f','g','h'], 'E':['c','g','h'],'F':['c','g','h','u','i']}

#matchRecipe(items,recipes)
