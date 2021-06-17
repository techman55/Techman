class quicksetup:
	
	def is_first_open(name, message=None):
		try:
			check = open(".{}.cashe".format(name), "r+")
			return False
		except FileNotFoundError:
			if message != None:
				print(message)
			check = open(".{}.cashe".format(name), "w")
			check.write("first_open was completed")
			return True
	
	def reset_first_open(name):
		import os
		try:
			os.remove(".{}.cashe".format(name))
			return True
		except FileNotFoundError:
			return False

#quicksetup.is_first_open('test', 'Hello')
#quicksetup.reset_first_open('test')
