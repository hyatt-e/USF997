import os, time, re, datetime
from time import mktime
# from datetimerange import DateTimeRange


# GLOBAL #
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

os.chdir(r'G:/WPy-3661/python/USF-997/IntIn-DEV/')
# file = open(r'G:/WPy-3661/python/USF-997/')
# #


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
				# stMonth, stDay, stYear = startDate.split("\\")
				# startDate = stMonth+stDay+stYear
				# future_date(startDate)
				# startDate = [int(stMonth),int(stDay),int(stYear)]
				# print(months[startDate[0]-1], stDay + ',', stYear)
			else:
				# check for '/'
				mat = re.search('[/]', startDate)
				if mat != None:
					startDate = valiDate(startDate, '/', None)
					# stMonth, stDay, stYear = startDate.split("/")
					# startDate = [int(stMonth),int(stDay),int(stYear)]
					# future_date_chk(startDate)
					# print(months[startDate[0]-1], stDay + ',', stYear)
				else:
					# check for '-'
					mat = re.search('[-]', startDate)
					if mat != None:
						startDate = valiDate(startDate, '-', None)
						# stMonth, stDay, stYear = startDate.split("-")
						# startDate = [int(stMonth), int(stDay), int(stYear)]
						# future_date_chk(startDate)
						# print(months[startDate[0] - 1], stDay + ',', stYear)
					else:
						# check for '.'
						mat = re.search('[.]', startDate)
						if mat != None:
							startDate = valiDate(startDate, '.', None)
							# stMonth, stDay, stYear = startDate.split(".")
							# startDate = [stMonth,stDay,stYear]
							# future_date_chk(startDate)
							# print(months[startDate[0] - 1], stDay + ',', stYear)

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
				# TODO: check that end date >= start date

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

	return startDate, endDate


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


def find_dir(startDate, endDate):
	dir_count = 0

	# drill into directories
	# first dir has #<year> and needs to be check separately
	if dir_count <= 0:
		for fldr in os.listdir():
			fldr = fldr.replace('#', '')
			if startDate[2] <= int(fldr) <= endDate[2]:
				dir_count += 1

				os.chdir("{}\\{}".format(os.getcwd(), '#' + fldr))
				print(os.getcwd())
			else:
				yrFlag = True
				# print('nope')

	if 0 < dir_count:
		# TODO: how many does to go back? Does it matter? Probs best to input how many; Date picker?

		# use fldr to check whether the for loop has already ran on this directory
		# set fldr to 0 to enter while loop
		dir_len = len(os.listdir())

		# while loop for today

		for fldr in os.listdir():
			if startDate[0] <= int(fldr) <= endDate[0]:
				dir_count += 1

				os.chdir("{}\\{}".format(os.getcwd(), fldr))
				# os.chdir("G:\\IntIn-DEV\\{}\\{}".format(fldr, str(tm_g[dir_count]).zfill(2)))
				print(os.getcwd())
			# else:
				# print('nope')


		# while loop for yesterday

		for fldr in os.listdir():
			if startDate[1] <= int(fldr) <= endDate[1]:
				dir_count += 1

				try:
					os.chdir("{}\\{}".format(os.getcwd(), fldr))
				# os.chdir("G:\\IntIn-DEV\\{}\\{}".format(fldr, str(tm_g[dir_count]).zfill(2)))
				except FileNotFoundError:
					continue
				print(os.getcwd())
			# else:
				# print('nope')

			# check_file()


# quick check for doc type and partner num
def check_file():
	# 'IN0940230354092.int'
	for file in os.listdir():
		path = os.getcwd() + file
		print(path)
		file = open(os.getcwd())
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

os.chdir('G:\\WPy-3661\\python\\USF-997\\IntIn-DEV\\')

startDate, endDate = set_time_rng(error)
find_dir(startDate, endDate)
# check_cwd()

