#Techman's python3 function library
class techman:

	def version():
		return 1.0
		
	def is_compatible(required_version):
		if techman.version() >= required_version:
			return True
		else:
			return False
			
	def check_for_update():
		print('Todo: Check for update')
		pass

class yn:

	#yn.ask => Takes in a prompt, asks for input, and returns True for "yes" and False for "no" based on response (Syntax: yn.ask('Yes or no? '))
	def ask(prompt, yes_list = ["yes","y"], no_list = ['no', 'y']):
		response = input(prompt).lower()
		if response in yes_list:
			return True
		elif response in no_list:
			return False
		else:
			print('Invaild Option, use {yes} or {no}\n'.format(yes=yes_list[0], no=no_list[0]))
			return yn.ask(prompt, yes_list, no_list)

	#yn.check => Takes in a string and returns True for "yes" and False for "no" based on string, also returns None for invaild option (Syntax: yn.ask('yes'))
	def check(string, yes_list = ["yes","y"], no_list = ['no', 'y']):
		string = string.lower()
		if string in yes_list:
			return True
		elif string in no_list:
			return False
		else:
			return None

class quicksetup:

	def is_first_open(name, message=None):
		try:
			open(".{}.cashe".format(name), "r").close()
			return False
		except FileNotFoundError:
			if message != None:
				print(message)
			with open(".{}.cashe".format(name), "w") as cashe:
				cashe.write("first_open was completed")
			return True
		
	def reset_first_open(name):
		import os
		try:
			os.remove(".{}.cashe".format(name))
			return True
		except FileNotFoundError:
			return False

	def does_config_exist(name):
		import json
		try:
			with open('.{}.config'.format(name), 'r') as file:
				json.loads(file.read().replace('\'', '\"'))
				return True
		except FileNotFoundError:
			return False
		except json.decoder.JSONDecodeError:
			print('[ERROR]: JSON Decode Error')
			return False

	def write_config(name, config):
		import json
		try:
			with open('.{}.config'.format(name), 'w') as file:
				file.write(str(config).replace('\'', '\"').replace('True', 'true').replace('False', 'false'))
				return config
		except:
			return None

	def read_config(name):
		import json
		if quicksetup.does_config_exist(name):
			with open('.{}.config'.format(name), 'r') as file:
				return json.loads(file.read().replace('\'', '\"'))
		else:
			return None

	def reset_config(name):
		import os
		try:
			os.remove(".{}.config".format(name))
			return True
		except FileNotFoundError:
			return False
