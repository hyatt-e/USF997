import os, time, re, datetime
# import pandas as pd
from time import mktime
# from datetimerange import DateTimeRange


# GLOBAL #
doctype = None

invalidDate_msg1 = "Please enter a valid date."
invalidDate_msg2 = "Dates may use '.' '-' '\\' or '/' to separate month, day, and year.\nYou may choose to use no separators, and instead enter an 8 digit string (ie. March 9, 1994 as 03091994 "
invalidDate_msg3 = "The End Date must be later than the Start Date"
invalidDate_msg4 = "You cannot select a date that is in the future."
tooManyErrors_msg10 = "You're not worthy of this application. BYE."

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
startDate = ''
endDate = ''
singleDate = False
error = 0

dirs = []
paths = [
	# 'G:\\WPy-3661\\python\\USF-997\\IntIn-DEV\\#2018\\09\\03\\',
 # 'G:\\WPy-3661\\python\\USF-997\\IntIn-DEV\\#2018\\09\\04\\',
 # 'G:\\WPy-3661\\python\\USF-997\\IntIn-DEV\\#2018\\09\\05\\',
 'G:\\WPy-3661\\python\\USF-997\\IntIn-DEV\\#2018\\09\\06\\'
         ]
paths2 = []
outputA = {}
outputR = {}
unknown = {}
# file = open(r'G:/WPy-3661/python/USF-997/')
# #




def future_date_chk(inDate):
	if inDate > datetime.date.today().strftime('%m-%d-%Y'):
		error = 4
		set_time_rng(error)


def start_end_chk(start, end):
	if start[2] > end[2]:
		error = 3
		set_time_rng(error)
	elif start[1] > end[1]:
		error = 3
		set_time_rng(error)
	elif start[0] > end[0]:
		error = 3
		set_time_rng(error)
	elif start == end:
		singleDate = True


def dbl_digit(month, day):
	if len(month) == 1:
		month = '0' + month
	if len(day) == 1:
		day = '0' + day
	return month, day


def error_msg(error):
	if error == 1:
		print(invalidDate_msg1, invalidDate_msg2)
		os.system("pause")
	if error == 2:
		print(invalidDate_msg2)
		os.system("pause")
	if error == 10:
		print(tooManyErrors_msg10)
		os.system("pause")
		exit = True


def valiDate(date, separator, start):
	if start == None:
		stMonth, stDay, stYear = date.split(separator)
		stMonth, stDay = dbl_digit(stMonth, stDay)
		startDate = stMonth + '-' + stDay + '-' + stYear
		future_date_chk(startDate)
		startDate = [int(stMonth),int(stDay),int(stYear)]
		print(months[startDate[0]-1], stDay + ',', stYear)
		return startDate
	elif start != None:
		endMonth, endDay, endYear = date.split(separator)
		endMonth, endDay = dbl_digit(endMonth, endDay)
		endDate = endMonth + '-' + endDay + '-' + endYear
		future_date_chk(endDate)
		endDate = [int(endMonth), int(endDay), int(endYear)]
		start_end_chk(start, endDate)
		print(months[endDate[0] - 1], endDay + ',', endYear)
		os.system("pause")
		return endDate


def set_time_rng(error):
	exit = False
	errorCnt = 0

	os.system('cls')
	print("Please enter dates with the month, followed by day, followed by year.\n"
		  "'.' '-' '\\' or '/' are acceptable separators\n")

	error_msg(error)
	error = 0

	while exit == False:
		os.system('cls')

		# Take input for start date
		startDate = input("Start Date: ")
		mat = re.match("((\d{1,2})[\\\/\-.](\d{1,2})[\\\/\-.](\d{4}))|([\d{8}])", startDate)

		if startDate.lower() == "exit":
			exit = True
			break
		elif mat != None:
			# check for '\'
			mat = re.search('[\\\]', startDate)
			if mat != None:
				startDate = valiDate(startDate, '\\', None)
			else:
				# check for '/'
				mat = re.search('[/]', startDate)
				if mat != None:
					startDate = valiDate(startDate, '/', None)
				else:
					# check for '-'
					mat = re.search('[-]', startDate)
					if mat != None:
						startDate = valiDate(startDate, '-', None)
					else:
						# check for '.'
						mat = re.search('[.]', startDate)
						if mat != None:
							startDate = valiDate(startDate, '.', None)

						# no separators; check length
						elif len(startDate) == 8:
							stMonth = startDate[:2]
							stDay = startDate[2:4]
							stYear = startDate[4:]
							startDate = stMonth + '-' + stDay + '-' + stYear
							startDate = valiDate(startDate, '-', None)
						else:
							error = 1
							set_time_rng(error)

			# Take input for end date
			endDate = input("End Date: ")
			mat = re.match("((\d{1,2})[\\\/\-.](\d{1,2})[\\\/\-.](\d{4}))|([\d{8}])", endDate)

			if endDate.lower() == "exit":
				exit = True
				break
			elif mat != None:
				# check that end date >= start date

				# check for '\'
				mat = re.search('[\\\]', endDate)
				if mat != None:
					endDate = valiDate(endDate, '\\', startDate)
					exit = True
				else:
					# check for '/'
					mat = re.search('[/]', endDate)
					if mat != None:
						endDate = valiDate(endDate, '/', startDate)
						exit = True
					else:
						# check for '-'
						mat = re.search('[-]', endDate)
						if mat != None:
							endDate = valiDate(endDate, '-', startDate)
							exit = True
						else:
							# check for '.'
							mat = re.search('[.]', endDate)
							if mat != None:
								endDate = valiDate(endDate, '.', startDate)
								exit = True

							# no separators; check length
							elif len(endDate) == 8:
								endMonth = endDate[:2]
								endDay = endDate[2:4]
								endYear = endDate[4:]
								endDate = endMonth + '-' + endDay + '-' + endYear
								endDate = valiDate(endDate, '-', startDate)
								exit = True
							else:
								error = 12
								set_time_rng(error)

			elif errorCnt == 0:
				error = 1
				set_time_rng(error)
				errorCnt += 1
			elif errorCnt >= 5:
				error = 0
				set_time_rng(error)
				exit = True
				break
			else:
				error = 2
				errorCnt += 1
				set_time_rng(error)

		elif errorCnt == 0:
			error = 1
			errorCnt +=1
			set_time_rng(error)
		elif errorCnt >= 5:
			error = 10
			set_time_rng(error)
		else:
			error = 2
			errorCnt += 1
			set_time_rng(error)

	dateRange = pd.date_range(start=startDate, end=endDate)
	dateRange = pd.Series(dateRange.format())

	return dateRange


def create_paths(dates):
	for date in dates:
		year, month, day = date.split('-')
		paths.append('G:\\WPy-3661\\python\\USF-997\\IntIn-DEV\\#{}\\{}\\{}\\'.format(year, month, day))
	return paths


def find_dir(paths):
	for path in paths:
		try:
			os.chdir(path)
		except FileNotFoundError:
			paths.remove(path)

		dirs = os.listdir()
		for dirty in dirs:
			paths2.append(path + dirty + '\\')
			# loop through paths2 and check files

	check_file(paths2)


# quick check for doc type and partner num
def check_file(paths2):
	# 'IN0940230354092.int'

	numFiles = 0
	validDocList = []
	invalidDocs = 0
	segmentFiles = {}

	for path in paths2:
		numFiles = numFiles + len(os.listdir(path))

		for file in os.listdir(path):
			# Search all dirs within these paths
			docPath = path + file
			file = open(docPath)
			file = file.read()

			if '997' and '621418185' in file:
				validDoc = True
			else:
				validDoc = False

			if validDoc == True:
				segments = split_segs(file)
				#
				# lines = file.split("~")
				#
				# for strg in lines:
				# 	seg = strg.split('^')
				# 	segments[seg[0]] = strg
				#
				# for key in segments:
				# 	segNum = 0
				# 	fields = segments[key].split('^')
				#
				# 	for x in fields:
				# 		x = x.replace(' ', '')
				# 		fields[segNum] = x
				# 		segNum += 1
				# 	segments[key] = fields

				# find ISA segment by looking for ISA-key in segments
				# find ST segment, check doc type
				# for key in segments:
				# if key == "ISA":
				partner = (segments[1])[6]
				if partner == '621418185':
					partner = True
				else:
					partner = False
					break
				# if key == "ST":
				docType = (segments[3])[1]
				if docType == "997":
					docType = True
				else:
					docType = False

				if partner == True and docType == True:
					validDoc == True
					validDocList.append(docPath)
					segmentFiles[docPath] = segments

				else:
					validDoc == False
					invalidDocs += 1
			else:
				pass
				invalidDocs += 1

	errors = error_check(segmentFiles)

	print('Total:', numFiles)
	print('Valid:', len(validDocList))
	print('Invalid:', invalidDocs)


def error_check(segment_files):
	ak5 = []
	ak2 = []
	for fileKey in segment_files:
		file = segment_files[fileKey]
		for key in file:
			if (file[key])[0] == 'AK2':
				# Ak2/AK5 segments
				# Check for 'R'
				if (file[key])[4] == 'A':
					# Save document num, type and accept/reject symbol to list
					outputA[fileKey] = [(file[key])[1], (file[key])[2], (file[key])[4]]
				elif (file[key])[4] == 'R':
					# Save document num, type and accept/reject symbol to list
					outputR[fileKey] = [(file[key])[1], (file[key])[2], (file[key])[4]]
				else:
					unknown[fileKey] = [(file[key])[1], (file[key])[2], (file[key])[4]]

	# TODO: check accepted values against values in excel file
	# TODO: find the empty dict that printing

	print(outputA)
	print('\n')
	print(outputR)
	print('\n')
	print(unknown)


def split_segs(file):
	segments = {}
	line = {}

	lines = file.split("~")

	for strng in lines:
		seg = strng.split('^')
		if (seg[0] == 'AK2') or (seg[0] == 'AK5'):
			if seg[0] == 'AK2':
				ak2ak5Seg = strng
			elif seg[0] == 'AK5':
				strng = '^' + strng
				ak2ak5Seg += strng
				segments[len(segments)+1] = ak2ak5Seg
		else:
			segments[len(segments)+1] = strng

	for key in segments:
		segNum = 0
		fieldStrg = segments[key].split('^')
		fields = []

		for x in fieldStrg:
			x = x.replace(' ', '')
			# fields[segNum] = x
			# necessary to use a dict instead of list??
			fields.append(x)
			segNum += 1

		segments[key] = fields
	return segments


def check_cwd():
	print(os.getcwd())


# os.chdir(r'G:/WPy-3661/python/USF-997/IntIn-DEV/')
os.chdir('G:\\WPy-3661\\python\\USF-997\\IntIn-DEV\\')

# dateRange = set_time_rng(error)
# paths = create_paths(dateRange)


# file = open('G:\\WPy-3661\\python\\USF-997\\IntIn-DEV\\#2018\\09\\06\\09\\IN0940230354092.INT')
# file = file.read()
# split_segs(file)


paths2 = find_dir(paths)
# print(paths2)
# check_cwd()
