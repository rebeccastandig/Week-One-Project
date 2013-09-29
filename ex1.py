import os
import string
import shutil

def main():
	source_dir = './original_files'
	destination_dir = './'

	def make_dir(folder_name):
		for num in range(97, 123):
			if not os.path.exists(chr(num) + "/"):
				os.mkdir(chr(num) + "/")
			if not os.path.exists("leftovers"):
				os.mkdir("leftovers")
	
	make_dir(destination_dir)

	source_files = os.listdir(source_dir)

	for f in source_files:
		source_path = os.path.join(source_dir, f)

		if f[0] in string.letters:
			destination_path = os.path.join(destination_dir + f[0]+ "/", f)

			clearshutil.copyfile(source_path, destination_path)


main()