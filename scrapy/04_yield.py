def fruits():
	return ['banana', 'apple', 'grapes']


for fruit in fruits():
	print(fruit)


def fruits_yield():
	yield 'banana'
	yield 'apple'
	yield 'grapes'


print(fruits_yield())

for fruit in fruits_yield():
	print(fruit)


def fruits_yield2():
	yield 'banana'
	print('some code for banana')
	yield 'apple'
	print('come code for apple')
	yield 'yield 3'
	print('come code for grapes')

for fruit in fruits_yield2():
	print(fruit)