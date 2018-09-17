import os, time
# 'IN0940230354092.int'
# file = open()
# file = file.read()
tm_g = time.localtime()
segments = {}
line = {}


# quick check for doc type and partner num
def check_file():
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

	dir_count = 0
	while dir_count < 4:
		for fldr in os.listdir():
			if fldr == "#{}".format(tm_g[dir_count]):
				dir_count += 1
				print(fldr)

				os.chdir("G:\\IntIn-DEV\\{}\\{}".format(fldr, str(tm_g[dir_count]).zfill(2)))
				print(os.getcwd())
			else:
				print('nope')


def check_cwd():
	print(os.getcwd())

check_cwd()
