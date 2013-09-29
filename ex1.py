import os
import string
import shutil

def main():
	source_dir = './original_files'
	destination_dir = './'

	def make_dir(folder_name):
		for num in range(97, 123):
			#uncertain if this will work, will it start
			# with "./"?
			if not os.path.exists(chr(num) + "/"):
				os.mkdir(chr(num) + "/")
			#I made this so my else below works,
			#but do I really need it? Unclear?
			if not os.path.exists("leftovers"):
				os.mkdir("leftovers")
	
	make_dir(destination_dir)

	source_files = os.listdir(source_dir)

	# def looping_through_text():

	for f in source_files:
		source_path = os.path.join(source_dir, f)

		#I think string.letters is all I need here...
		if f[0] in string.letters:
			destination_path = os.path.join(destination_dir + f[0]+ "/", f)
		# else:
		# 	destination_path = os.path.join(destination_dir + "leftovers", + f)

	# looping_through_text()

	# print source_path
	# print destination_path

			shutil.copyfile(source_path, destination_path)


main()