def angry(func):
	def wrapper():
		func()
		print('he is angry')
	return wrapper

@angry
def human():
	print('this is human')

human()
# Добавить 10 декораторов, которые будут дополнять эту функцию. Например, декораторы с чертами характера

# def timer(func):
# 	import time
# 	def wrapper():
# 		start = time.time()
# 		func()
# 		end = time.time()
# 		print('time: ', end-start)
# 	return wrapper

# count = 0
# def counter(func):
# 	def wrapper():
# 		global count
# 		count+=1
# 		func()
# 		print(func.__name__, 'is called', count)
# 	return wrapper

# def logging(func):
# 	def wrapper():
# 		func()
# 		print('Function is',func.__name__)
# 	return wrapper

# @logging
# @counter
# @timer
# def webpage():
# 	import requests
# 	page = requests.get('https://www.random.org/')
# 	print(page.text)

# @counter
# @timer
# def ask():
# 	a = input('Text: ')
# 	# print(a)

# # webpage()
# ask()
# webpage()
# webpage()
# def salat(func):
# 	def wrapper():
# 		func()
# 		print('salat')
# 	return wrapper

# def tomato(func):
# 	def wrapper():
# 		func()
# 		print('tomato')
# 	return wrapper

# @tomato
# @salat
# def burger():
# 	print('This is burger')

# @salat
# def sandwich():
# 	print('this is sandwich')

# # burger()
# sandwich()
# num1 = num2 = sign = ''
# while num1 == '' or num2 == '' or sign == '':
# 	try:
# 		num1 = int(input('Number1: '))
# 		sign = input('Sign: ')
# 		num2 = int(input('Number2: '))
# 		if sign == '/' and num2 == 0:
# 			raise ZeroDivisionError
# 	except ValueError:
# 		print('Wrong value')
# 	except ZeroDivisionError:
# 		sign = ''
# 		print('Go to school')
# 	except:
# 		print('Something go wrong')
# 	try:
# 		if sign == '+':
# 			print(f"{num1} + {num2} = {num1+num2}")
# 		elif sign == '':
# 			print()
# 	except TypeError:
# 		print('Wrong types')

# Задание 1: Добавить остальные операции в калькулятор (-, *, /)
# Задание 2: Сделать проверку на правильность знака. Например, вместо +,-,*,/ пользователь ввел !. Обработать ошибку
# Задание 3: Перед использованием калькулятора, попросить пользователя представиться. Если он вводит числа в своем имени, то обработать исключительную ситуацию.
# try:
# 	a = 5
# 	print(a/0)
# except:
# 	print('You stupid!')

# print('Hello world!')

# class Human:
# 	def __init__(self, name):
# 		self.name = name
# 		self.age = 0
# 		self.clever = 5
# 	def live(self):
# 		print(self.name, 'is alive')

# class Woman(Human):
# 	def __init__(self,name):
# 		super().__init__(name)
# 		self.character = True
# 	def live(self):
# 		# super().live()
# 		print('What a wonderful day of', self.name)
# 	def nails(self):
# 		print(self.name, 'is on manicure')
# class Man(Human):
# 	def __init__(self, name):
# 		super().__init__(name)
# 		self.money = 100
# 	def job(self):
# 		self.money += 50
# 	def balance(self):
# 		print('Balance: ', self.money)

# obj = Human('Bob')
# obj.live()
# obj2 = Woman('Clara')
# obj2.live()
# obj2.nails()
# print(obj2.name, obj2.character, obj2.age)




# Создать класс Животное. От него наследуются классы Котик, Собачка и Хомячок. В классе есть 3 поля (характеристики) и 2 поведения (методы). В классах конкретных животных добавить по 1 дополнительному поведения

# # print('Hello world')
# from random import *

# class University:
# 	def __init__(self, title, faculty):
# 		self.title = title
# 		self.faculty = faculty
# 		self.budget = False
# 	def studying(self, name):
# 		print(name + ' is studying')
# 	def isbudget(self):
# 		if self.budget == True:
# 			print('Congratulations! You are on budget!')
# 		else:
# 			print('Pay money and study')

# class Student:
# 	def __init__(self, name):
# 		self.name = name
# 		self.gladness = 50
# 		self.progress = 0
# 		self.alive = True
		

# 	def ask_budget(self):
# 		if self.progress > 30:
# 			self.gladness += 10
# 			univer.budget = True
# 	def say_hello(self):
# 		print('Hello!')
# 	def to_study(self):
# 		if univer.budget == True:
# 			self.gladness -= 1
# 			print('Too much responsibility')
# 		print('Time to study')
# 		if self.progress < 5:
# 			self.gladness -= 4
# 		self.progress += 5
# 		self.gladness -= 1
# 	def to_sleep(self):
# 		print('Time to sleep')
# 		self.gladness += 2
# 	def to_chill(self):
# 		print('Rest time')
# 		self.gladness += 5
# 		self.progress -= 2
# 	def is_alive(self):
# 		if self.progress < -10:
# 			print('You are bad')
# 			self.alive = False
# 		elif self.gladness <= 0:
# 			print('Dead inside')
# 			self.alive = False
# 		elif self.progress > 50:
# 			print('Amazing! You are so smart')
# 			self.alive = False
# 	def statics(self, univer):
# 		print('Gladness: ', self.gladness, 'Progress: ',self.progress)
# 		print('Budget: ', univer.budget)
# 	def live(self, day):
# 		day = "Day " + str(day) + " of " + self.name + " life"
# 		print(day)
# 		live_cube = randint(1,4)
# 		if live_cube == 1:
# 			self.to_study()
# 			self.ask_budget()
# 			univer.studying(self.name)
# 		elif live_cube == 2:
# 			self.to_sleep()
# 		elif live_cube == 3:
# 			self.to_chill()
# 		elif live_cube == 4:
# 			self.say_hello()
# 		self.statics(univer)
# 		self.is_alive()
		
# univer = University('Step', 'Computer Science')
# sanya = Student('Sanya')
# for day in range(365):
# 	if sanya.alive == False:
# 		break
# 	sanya.live(day)

# # human = Student('Zolo')
# # for day in range(365):
# # 	if human.alive == False:
# # 		break
# # 	human.live(day)