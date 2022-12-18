class Animal:
	def __init__(self, species):
		self.species = species
		self.nutrition = 'None'
		self.age = 0
	def sleep(self):
		print(f'{self.species} is sleeping')
	def move(self):
		print(f'{self.species} is moving')
	def eat(self):
		print(f'{self.species} is eating')

class Cat(Animal):
	def play(self):
		print('It is playing')

class Dog(Animal):
	def __init__(self, species):
		super().__init__(species)
		self.owner = 'None'
	def move(self):
		# super().move()
		print('Dog is running')

hamster = Animal('Hamster')
hamster.sleep()
hamster.move()
hamster.eat()

# cat1 = Cat('Siamez')
# cat1.sleep()
# cat1.eat()
# cat1.move()
# cat1.play()

dog1 = Dog('Chihuahua')
dog1.sleep()
dog1.eat()
dog1.move()


# class Book:
# 	def __init__(self):
# 		self.author = 'None'
# 		self.title = 'None'
# 		self.pages = 0
# 	def read(self):
# 		print(f'Book {self.title} is being read')
# 	def add_info(self):
# 		try:
# 			self.author = input('Input the name of author:')
# 			self.title = input('Input title of the book:')
# 			self.pages = int(input('Input the amount of pages: '))
# 			if self.author.isalpha() == False:
# 				raise NameError
# 			if self.pages < 0:
# 				raise ValueError
# 		except NameError:
# 			print('Bad names')
# 		except ValueError:
# 			print('Not correct pages')
# 		except:
# 			print('Error')

# obj1 = Book()
# obj1.read()
# obj1.add_info()
# obj1.read()