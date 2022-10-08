#!/bin/python3

#Print string
print("Hello, world!") #double quotes
print('Hello, world!') #single quotes

print("""This string runs
multiple lines!""") #triple quote for multi-line

print("This string is "+"awesome!") #we can also concatenate

print('\n') #new line

#MATH

print(50 + 50) #add
print(50 - 50) #subtract
print(50 * 50) #multiply
print(50 / 50) #divide
print(50 + 50 - 50 * 50 / 50) #PEMDAS
print(50 ** 2) #exponents
print(50 % 6) #modulo - takes what is left over
print(50 / 6) #division with decimals
print(50 // 6) #no leftovers / remainder

#VARIABLES AND METHODS
quote = "All is fair in love and war"
print(quote)

print(quote.upper()) #uppercase
print(quote.lower()) #lower
print(quote.title()) #title case
print(len(quote)) #counts characters

name = "Heath" #string
age = 33 #int
gpa = 3.7 #float - has a decimal

print(int(age))
print(int(30.1))
print(int(30.9))

print("My name is " + name + " and I am " + str(age) + " years old.")

age +=1
print(age)

birthday = 1
age += birthday
print(age)


#FUNCTIONS

print('\n')

print("Here is an example function:")

def who_am_i(): #this is a function
	name = "Heath"
	age = 33
	print("My name is " + name + " and I am " + str(age) + " years old.")
	
who_am_i()


#adding parameters
def add_one_hundred(num):
	print(num + 100)
	
add_one_hundred(100)

#multiple parameters
def add(x,y):
	print(x + y)
	
add(7,7)

def multiply(x,y):
	return x * y

multiply(7,7)
print(multiply(7,7))

def square_root(x):
	print(x ** .5)
	
square_root(64)

def nl():
	print('\n')
	
nl()

#BOOLEAN EXPRESSIONS (True or False)
print("Boolean expressions:")

bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1, bool2, bool3, bool4)
print(type(bool1))

bool5 = "True"
print(type(bool5))

nl()

#Relational and Boolean Operators
greater_than = 7 > 5

less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7

test_not = not True #False

nl()
#CONDITIONAL STATEMENTS

def drink(money):
	if money >= 2:
		return "You've got yourself a drink!"
	else:
		return "No drink for you!"

print(drink(3))
print(drink(1))

def alcohol(age,money):
	if (age >= 21) and (money >= 5):
		return "We're getting a drink!"
	elif (age >= 21) and (money < 5):
		return "Come back with more money."
	elif (age < 21) and (money >= 5):
		return "Nice try, kid!"
	else:
		return "You're too poor and too young!"

print(alcohol(21,5))
print(alcohol(21,4))
print(alcohol(20,5))
print(alcohol(20,4))