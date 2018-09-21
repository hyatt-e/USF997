import os, time
from datetimerange import DateTimeRange


os.chdir(r'G:/WPy-3661/python/USF-997/IntIn-DEV/')
# file = open(r'G:/WPy-3661/python/USF-997/')


def find_dir():
	dir_count = 0

	# drill into directories
	# first dir has #<year> and needs to be check separately
	if dir_count <= 0:
		for fldr in os.listdir():
			if fldr == "#{}".format(tm[dir_count]):
				print(fldr)
				dir_count += 1

				os.chdir("{}\\{}".format(os.getcwd(), fldr))
				print(os.getcwd())
			else:
				print('nope')

	if 0 < dir_count:
		# TODO: how many does to go back? Does it matter? Probs best to input how many; Date picker?

		# use fldr to check whether the for loop has already ran on this directory
		# set fldr to 0 to enter while loop
		dir_len = len(os.listdir())

		# while loop for today

		fldr = 0
		while int(fldr) < dir_len:
			for fldr in os.listdir():
				if fldr == str(tm[dir_count]).zfill(2):
					print(fldr)
					dir_count += 1

					os.chdir("{}\\{}".format(os.getcwd(), fldr))
					# os.chdir("G:\\IntIn-DEV\\{}\\{}".format(fldr, str(tm_g[dir_count]).zfill(2)))
					print(os.getcwd())
				else:
					print('nope')


		# while loop for yesterday

		fldr = 0
		while int(fldr) < dir_len:
			for fldr in os.listdir():
				if fldr == str((tm[dir_count]) - 1).zfill(2):
					print(fldr)
					dir_count += 1

					os.chdir("{}\\{}".format(os.getcwd(), fldr))
					# os.chdir("G:\\IntIn-DEV\\{}\\{}".format(fldr, str(tm_g[dir_count]).zfill(2)))
					print(os.getcwd())
				else:
					print('nope')


# quick check for doc type and partner num
def check_file():
	# 'IN0940230354092.int'
	file = open('.\\IntIn-DEV\\')
	file = file.read()
	segments = {}
	line = {}

	if '997' and '621418185' in file:
		validDoc = True
	else:
		validDoc = False

	if validDoc == True:
		lines = file.split("~")

		for strg in lines:
			seg = strg.split('^')
			segments[seg[0]] = strg

		for key in segments:
			segNum = 0
			fields = segments[key].split('^')

			for x in fields:
				x = x.replace(' ', '')
				fields[segNum] = x
				segNum += 1
			segments[key] = fields

		print(segments)
		# find ISA segment by looking for ISA-key in segments
		# find ST segment, check doc type
		for key in segments:
			if key == "ISA":
				partner = (segments[key])[6]
				if partner == '621418185':
					partner = True
				else:
					partner = False
					break
			elif key == "ST":
				docType = (segments[key])[1]
				if docType == "997":
					docType = True
				else:
					docType = False
					break
			else:
				pass

			if partner == True and docType == True:
				validDoc == True
			else:
				validDoc == False
				break

	else:
		pass


def check_cwd():
	print(os.getcwd())

check_cwd()
