import os, time

file = open('IN0940230354092.int')
file = file.read()

tm = time.localtime()

if '997' and '621418185' in file:
	validDoc = True
else:
	validDoc = False
	break

if validDoc == True:
	lines = file.split("~")

	segments = {}

	for strg in lines:
		seg = strg.split('^')
		segments[seg[0]] = strg

	for key in segments:
		segNum = 0
		line = {}
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
while dir_count < 4
    for fldr in os.listdir():
        if fldr == "#{}".format(tm[dir_count]):
            dir_count += 1
            print(fldr)

            os.chdir("G:\\IntIn-DEV\\{}\\{}".format(fldr, str(tm[dir_count]).zfill(2)))
            print(os.getcwd())
        else:
            print('nope')
