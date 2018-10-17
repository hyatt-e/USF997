import os, re, datetime, pandas
from datetime import date, timedelta


# TODO: change paths for files
# GLOBAL VARIABLES #

doctype = None
error = 0

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
startDate = ''
endDate = ''
singleDate = False
dateRange = None

last810 = None
last855 = None
usf_ctrl_nums = None
status = None

dirs = []
paths = [
	# 'G:\\WPy-3661\\python\\USF-997\\IntIn-DEV\\#2018\\09\\03\\',
 # 'G:\\WPy-3661\\python\\USF-997\\IntIn-DEV\\#2018\\09\\04\\',
 # 'G:\\WPy-3661\\python\\USF-997\\IntIn-DEV\\#2018\\09\\05\\',
 # 'G:\\WPy-3661\\python\\USF-997\\IntIn-DEV\\#2018\\09\\06\\'
         ]
paths2 = []
outputA = {}
outputR = {}
unknown = {}

numFiles = 0
validDocList = []
invalidDocs = 0

segmentFiles = {}
# print(usf_ctrl_nums)
# usf_ctrl_nums.columns = ['DocType', 'LastDoc#']
# file = open(r'G:/WPy-3661/python/USF-997/')
# #


def last_accepted(usf_ctrl_nums):
	global last810
	global last855

	docType = usf_ctrl_nums.iloc[0,0]
	if docType == "810's":
		last810 = int(usf_ctrl_nums.iloc[0, 1])

	docType = usf_ctrl_nums.iloc[2,0]
	if docType == "855's":
		last855 = int(usf_ctrl_nums.iloc[2, 1])

	# print('Last document numbers:')
	# print("810: {}".format(last810))
	# print("855: {}".format(last855))
	# return last810, last855
	return last810, last855


def future_date_chk(inDate):
	if inDate > datetime.date.today().strftime('%m-%d-%Y'):
		error = 4
		# set_time_rng(error)
		main_loop(error)


def start_end_chk(start, end):
	d1 = datetime.datetime.strptime(start, "%m-%d-%Y").date()
	d2 = datetime.datetime.strptime(end, "%m-%d-%Y").date()
	if d2 < d1:
		error = 3
		# set_time_rng(error)
		main_loop(error)
	# if start[3:5] > end[3:5]:
	# 	error = 3
	# 	set_time_rng(error)
	# elif start[1] > end[1]:
	# 	error = 3
	# 	set_time_rng(error)
	# elif start[0] > end[0]:
	# 	error = 3
	# 	set_time_rng(error)
	# elif start == end:
	# 	singleDate = True


def dbl_digit(month, day, year):
	if len(month) == 1:
		month = '0' + month
	if len(day) == 1:
		day = '0' + day
	if len(year) == 2:
		year = '20' + year
	return month, day, year


def valiDate(start, separator, end):
	if end == None:
		stMonth, stDay, stYear = start.split(separator)
		stMonth, stDay, stYear = dbl_digit(stMonth, stDay, stYear)
		startDate = stMonth + '-' + stDay + '-' + stYear
		future_date_chk(startDate)
		startDateList = [int(stMonth),int(stDay),int(stYear)]
		# print(months[startDate[0]-1], stDay + ',', stYear)
		print(months[int(stMonth)-1], stDay + ',', stYear+'\n')
		return startDate
	elif end != None:
		endMonth, endDay, endYear = end.split(separator)
		endMonth, endDay, endYear = dbl_digit(endMonth, endDay, endYear)
		endDate = endMonth + '-' + endDay + '-' + endYear
		future_date_chk(endDate)
		endDateList = [int(endMonth), int(endDay), int(endYear)]
		start_end_chk(start, endDate)
		# print(months[endDate[0] - 1], endDay + ',', endYear)
		print(months[int(endMonth)-1], endDay + ',', endYear+'\n')
		os.system("pause")
		return endDate


def set_time_rng(error):
	exit = False
	errorCnt = 0
	global status

	status = "SELECT DATE RANGE . . ."
	statusOutput(status)

	error_msg(error)

	while exit == False:
		# Take input for start date
		# TODO: skip start input if error was on end date
		# TODO: add default value

		print(instruction_msg2)
		# startDate = input("Start Date: ")

		defaultStart = date.today() - timedelta(1)
		defaultStart = defaultStart.strftime('%m-%d-%Y')
		print('[{}]'.format(defaultStart))
		startDate = input("Start Date: ") or defaultStart

		if startDate.lower() == "exit":
			exit = True
			error = 11
			break
		elif startDate == '':
			error = 4
			error_msg(error)
		else:
			# ([\d{8}])
			# match = re.match("((\d{1,2})[\\\](\d{1,2})[\\\](\d{4}))", startDate)
			# match = re.findall("((\d{1,2})[\\\](\d{1,2})[\\\](\d{4}))", startDate)
			if (re.findall("((\d{1,2})[\\\](\d{1,2})[\\\](\d{4}))", startDate)) != []:
				match = re.findall("((\d{1,2})[\\\](\d{1,2})[\\\](\d{4}))", startDate)
				for x in match[0]:
					if x == startDate:
						startDate = valiDate(startDate, '\\', None)
			elif (re.findall("((\d{1,2})[/](\d{1,2})[/](\d{4}))", startDate)) != []:
				match = re.findall("((\d{1,2})[/](\d{1,2})[/](\d{4}))", startDate)
				for x in match[0]:
					if x == startDate:
						startDate = valiDate(startDate, '/', None)
			elif (re.findall("((\d{1,2})[-](\d{1,2})[-](\d{4}))", startDate)) != []:
				match = re.findall("((\d{1,2})[-](\d{1,2})[-](\d{4}))", startDate)
				for x in match[0]:
					if x == startDate:
						startDate = valiDate(startDate, '-', None)
			elif (re.findall("((\d{1,2})[.](\d{1,2})[.](\d{4}))", startDate)) != []:
				match = re.findall("((\d{1,2})[.](\d{1,2})[.](\d{4}))", startDate)
				for x in match[0]:
					if x == startDate:
						startDate = valiDate(startDate, '.', None)
			elif (re.findall("((\d{1,2})(\d{1,2})(\d{4}))", startDate)) != []:
				match = re.findall("((\d{1,2})(\d{1,2})(\d{4}))", startDate)
				for x in match[0]:
					if x == startDate:
						stMonth = startDate[:2]
						stDay = startDate[2:4]
						stYear = startDate[4:]
						startDate = stMonth + '-' + stDay + '-' + stYear
						startDate = valiDate(startDate, '-', None)
			# if match.match > 0:
			# 	# check for '\'
			# 	match = re.search('[\\\]', startDate)
			# 	if match != None:
			# 		startDate = valiDate(startDate, '\\', None)
			# 	else:
			# 		# check for '/'
			# 		match = re.search('[/]', startDate)
			# 		if match != None:
			# 			startDate = valiDate(startDate, '/', None)
			# 		else:
			# 			# check for '-'
			# 			match = re.search('[-]', startDate)
			# 			if match != None:
			# 				startDate = valiDate(startDate, '-', None)
			# 			else:
			# 				# check for '.'
			# 				match = re.search('[.]', startDate)
			# 				if match != None:
			# 					startDate = valiDate(startDate, '.', None)
			#
			# 				# no separators; check length
			# 				elif len(startDate) == 8:
			# 					stMonth = startDate[:2]
			# 					stDay = startDate[2:4]
			# 					stYear = startDate[4:]
			# 					startDate = stMonth + '-' + stDay + '-' + stYear
			# 					startDate = valiDate(startDate, '-', None)
			else:
				error = 1
				# set_time_rng(error)
				main_loop(error)

			# Take input for end date
			defaultEnd = date.today().strftime('%m-%d-%Y')
			print('[{}]'.format(defaultEnd))
			endDate = input("End Date: ") or defaultEnd

			# endDate = input("End Date: ")

			if endDate.lower() == "exit":
				exit = True
				error = 11
				break
			elif endDate == '':
				error = 4
				error_msg(error)
			else:
				# ([\d{8}])
				# match = re.match("((\d{1,2})[\\\](\d{1,2})[\\\](\d{4}))", startDate)
				# match = re.findall("((\d{1,2})[\\\](\d{1,2})[\\\](\d{4}))", startDate)
				if (re.findall("((\d{1,2})[\\\](\d{1,2})[\\\](\d{4}))", endDate)) != []:
					match = re.findall("((\d{1,2})[\\\](\d{1,2})[\\\](\d{4}))", endDate)
					for x in match[0]:
						if x == endDate:
							endDate = valiDate(startDate, '\\', endDate)
							exit = True
				elif (re.findall("((\d{1,2})[/](\d{1,2})[/](\d{4}))", endDate)) != []:
					match = re.findall("((\d{1,2})[/](\d{1,2})[/](\d{4}))", endDate)
					for x in match[0]:
						if x == endDate:
							endDate = valiDate(startDate, '/', endDate)
							exit = True
				elif (re.findall("((\d{1,2})[-](\d{1,2})[-](\d{4}))", endDate)) != []:
					match = re.findall("((\d{1,2})[-](\d{1,2})[-](\d{4}))", endDate)
					for x in match[0]:
						if x == endDate:
							endDate = valiDate(startDate, '-', endDate)
							exit = True
				elif (re.findall("((\d{1,2})[.](\d{1,2})[.](\d{4}))", endDate)) != []:
					match = re.findall("((\d{1,2})[.](\d{1,2})[.](\d{4}))", endDate)
					for x in match[0]:
						if x == endDate:
							endDate = valiDate(startDate, '.', endDate)
							exit = True
				elif (re.findall("((\d{1,2})(\d{1,2})(\d{4}))", endDate)) != []:
					match = re.findall("((\d{1,2})(\d{1,2})(\d{4}))", endDate)
					for x in match[0]:
						if x == endDate:
							endMonth = endDate[:2]
							endDay = endDate[2:4]
							endYear = endDate[4:]
							endDate = endMonth + '-' + endDay + '-' + endYear
							endDate = valiDate(startDate, '-', endDate)
							exit = True

			#
			#
			# if endDate.lower() == "exit":
			# 	exit = True
			# 	error = 11
			# 	break
			# else:
			# 	match = re.match("((\d{1,2})[\\\/\-.](\d{1,2})[\\\/\-.](\d{4}))|([\d{8}])", endDate)
			# 	if match != None:
			# 		# check that end date >= start date
			#
			# 		# check for '\'
			# 		match = re.search('[\\\]', endDate)
			# 		if match != None:
			# 			endDate = valiDate(startDate, '\\', endDate)
			# 			exit = True
			# 		else:
			# 			# check for '/'
			# 			match = re.search('[/]', endDate)
			# 			if match != None:
			# 				endDate = valiDate(startDate, '/', endDate)
			# 				exit = True
			# 			else:
			# 				# check for '-'
			# 				match = re.search('[-]', endDate)
			# 				if match != None:
			# 					endDate = valiDate(startDate, '-', endDate)
			# 					exit = True
			# 				else:
			# 					# check for '.'
			# 					match = re.search('[.]', endDate)
			# 					if match != None:
			# 						endDate = valiDate(startDate, '.', endDate)
			# 						exit = True
			#
			# 					# no separators; check length
			# 					elif len(endDate) == 8:
			# 						endMonth = endDate[:2]
			# 						endDay = endDate[2:4]
			# 						endYear = endDate[4:]
			# 						endDate = endMonth + '-' + endDay + '-' + endYear
			# 						endDate = valiDate(startDate, '-', endDate)
			# 						exit = True
			# 					else:
			# 						error = 12
			# 						set_time_rng(error)
			#
			# 	elif errorCnt == 0:
			# 		error = 1
			# 		set_time_rng(error)
			# 		errorCnt += 1
			# 	elif errorCnt >= 5:
			# 		error = 0
			# 		set_time_rng(error)
			# 		exit = True
			# 		break
			# 	else:
			# 		error = 2
			# 		errorCnt += 1
			# 		set_time_rng(error)

	if error != 0:
		if errorCnt == 0:
			errorCnt +=1
			# set_time_rng(error)
			main_loop(error)
		elif errorCnt >= 5:
			# error = 10
			print(tooManyErrors_msg10)
			# set_time_rng(error)
			main_loop(error)
		else:
			error = 2
			errorCnt += 1
			# set_time_rng(error)
			main_loop(error)

	dateRange = pandas.date_range(start=startDate, end=endDate)
	dateRange = pandas.Series(dateRange.format())

	return dateRange


def create_paths(dateRange):
	for date in dateRange:
		year, month, day = date.split('-')
		paths.append('G:\\WPy-3661\\python\\USF-997\\IntIn-DEV\\#{}\\{}\\{}\\'.format(year, month, day))
	return paths


def find_dir(paths):
	paths2 = []
	for path in paths:
		try:
			os.chdir(path)
			good_path = True
		except FileNotFoundError:
			# paths.remove(path)
			good_path = False

		if good_path == True:
			dirs = os.listdir()
			for dirty in dirs:
				paths2.append(path + dirty + '\\')
				# loop through paths2 and check files
	if len(paths2) == 0:
		# no files for this range
		error = 6
		error_msg(error)
	return paths2


# quick check for doc type and partner num
def check_file(paths2):
	status = 'SCANNING DOCUMENTS . . .'
	statusOutput(status)

	global segmentFiles
	global numFiles
	global validDocList
	global validDoc
	global invalidDocs

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

					statusOutput(status)

				else:
					validDoc == False
					invalidDocs += 1

					statusOutput(status)
			else:
				pass
				invalidDocs += 1

				statusOutput(status)

	with open('G:\\WPy-3661\\python\\USF-997\\Logs\\usf997_{}.txt'.format(datetime.datetime.today().strftime('%m-%d-%y_%I%M%S')), 'w+') as log_file:
		for item in validDocList:
			log_file.write(str(item) + '\n')

	statusOutput(status)
	return segmentFiles


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


def reject_check(segment_files, last810, last855):
	ak5 = []
	ak2 = []
	newDocs = False
	status = 'SCANNING DOCUMENTS . . .'

	for fileKey in segment_files:
		file = segment_files[fileKey]
		for key in file:
			if (file[key])[0] == 'AK2':
				# Ak2/AK5 segments
				# Check for 'R'
				if (file[key])[4] == 'A':
					# Save document num, type and accept/reject symbol to list
					outputA[fileKey] = [(file[key])[1], (file[key])[2], (file[key])[4]]
					if (file[key])[1] == '810':
						if int(last810) < int((file[key])[2]):
							usf_ctrl_nums.iloc[0,1] == (file[key])[2]
							newDocs = True
					elif (file[key])[1] == '855':
						if int(last855) < int((file[key])[2]):
							usf_ctrl_nums.iloc[2,1] == (file[key])[2]
							newDocs = True
				elif (file[key])[4] == 'R':
					# Save document num, type and accept/reject symbol to list
					outputR[fileKey] = [(file[key])[1], (file[key])[2], (file[key])[4]]
					statusOutput(status)
				else:
					unknown[fileKey] = [(file[key])[1], (file[key])[2], (file[key])[4]]
					statusOutput(status)

	if newDocs == True:
		usf_ctrl_nums.to_csv('G:\\WPy-3661\\python\\USF-997\\US_Foods_Ctrl_Nums.csv', header=None, index=False)
	status = "FINISHED !"
	statusOutput(status)


def statusOutput(status):
	if status == "SELECT DATE RANGE . . .":
		os.system('cls')
		print('Last document numbers:')
		print("810: {}".format(last810))
		print("855: {}".format(last855))
		print('\n')
		print(status)
		print('\n')
		print(instruction_msg1)
	elif status == 'FINDING FILES WITHIN DATE RANGE . . .':
		os.system('cls')
		print('Last document numbers:')
		print("810: {}".format(last810))
		print("855: {}".format(last855))
		print('\n')
		print(status)
		print('\n')
	elif status == 'SCANNING DOCUMENTS . . .':
		os.system('cls')
		print('Last document numbers:')
		print("810: {}".format(last810))
		print("855: {}".format(last855))
		print('\n')
		print(status)
		print('\n')
		print('Total documents scanned:', numFiles)
		print("US Foods 997's: ", len(validDocList))
		print('Non USF 997 documents scanned:', invalidDocs)
		print('\n')
	elif status == "FINISHED !":
		os.system('cls')
		print('Last document numbers:')
		print("810: {}".format(last810))
		print("855: {}".format(last855))
		print('\n')
		print(status)
		print('\n')
		print('Total documents scanned:', numFiles)
		print("US Foods 997's: ", len(validDocList))
		print('Non USF 997 documents scanned:', invalidDocs)
		print('\n')

		if outputR != {}:
			print("997's with rejected documents:")
			print(outputR)
		elif unknown != {}:
			print("997's with unknown issue:")
			print(unknown)
		elif len(validDocList) == 0:
			print("No new USF 997's for this date range")
		else:
			print("No 997's containing rejected documents were found!")
			print("The 'US Foods Control Numbers.xlxs' file was updated with the latest document numbers")
		print("\nA log of the USF 997's scanned is located here: 'X:\DEVELOPMENT\EDI\\'")


#______________________________________________________________________________________________________________________#
instruction_msg1 = "Please enter dates with the month, followed by day, followed by year\n. - \\ / or no separators may be used\nEnter 'exit' to close the program\n"
instruction_msg2 = "Press 'Enter' to use the [Default Date]"
file_not_found_msg = "Could not open the US Foods Control Numbers document!\nMake sure the file is in the correct location:\n'G:\\WPy-3661\\python\\USF-997\\US Foods Control Numbers.csv'"
no_dir_for_range = "No directories were found matching this date range.\nThere may be no inbound files for the specified dates."
invalidDate_msg1 = "Please enter a valid date.\n"
invalidDate_msg2 = "Dates may use . - \\ / or no separators may be used to separate month, day, and year.\nIf using no separators, enter an 8 digit string (ie. March 9, 1994 as 03091994)"
invalidDate_msg3 = "The End Date must be later than the Start Date"
invalidDate_msg4 = "You cannot select a date that is in the future."
tooManyErrors_msg10 = "Are you sure you're entering a date?"
exit_msg = "BYE."
#______________________________________________________________________________________________________________________#

def error_msg(error):
	if error == 1:
		# invalid 1
		statusOutput(status)
		print(invalidDate_msg1, invalidDate_msg2)
		os.system("pause")
		error = 0
	if error == 2:
		# invalid 2
		statusOutput(status)
		print(invalidDate_msg1, invalidDate_msg2)
		os.system("pause")
		error = 0
	if error == 3:
		# end date is before start date
		statusOutput(status)
		print(invalidDate_msg1, invalidDate_msg2)
		print('\n')
		print(invalidDate_msg3)
		os.system("pause")
		error = 0
	if error == 4:
		# date is in the future
		statusOutput(status)
		print(invalidDate_msg1, invalidDate_msg2)
		print('\n')
		print(invalidDate_msg4)
		os.system("pause")
		error = 0
	if error == 5:
		# date is in the future
		print(file_not_found_msg)
		print(exit_msg)
		os.system("pause")
		quit()
	if error == 6:
		# no applicable files found
		print(no_dir_for_range)
		print("Would you like to try another date range? [y/N]")
		restart = input('')
		if restart.lower() == 'y':
			error = 0
			# set_time_rng(error)
			main_loop(error)
		elif restart.lower() == 'n':
			print(exit_msg)
			quit()
		else:
			error = 7
			error_msg(error)
	if error == 7:
		# no applicable files found
		print(no_dir_for_range)
		print("Please enter 'y' for yes, or 'n' for no.")
		print("Would you like to try another date range? [y/N]")
		restart = input('')
		if restart.lower() == 'y':
			error = 0
			# set_time_rng(error)
			main_loop(error)
		elif restart.lower() == 'n':
			print(exit_msg)
			quit()
		else:
			error = 7
			error_msg(error)

	if error == 10:
		# more than 5 errors
		statusOutput(status)
		print(invalidDate_msg1, invalidDate_msg2)
		print('\n')
		print(tooManyErrors_msg10)
		os.system("pause")
		error = 0
		exit = True
	if error == 11:
		# exiting; no error
		print(exit_msg)
		os.system("pause")
		quit()

def check_cwd():
	print(os.getcwd())

def main_loop(error):
	global usf_ctrl_nums
	global status
	os.chdir('G:\\WPy-3661\\python\\USF-997\\IntIn-DEV\\')
	try:
		usf_ctrl_nums = pandas.read_csv('G:\\WPy-3661\\python\\USF-997\\US Foods Control Numbers.csv', header=None)
	except FileNotFoundError:
		error = 5
		error_msg(error)

	last810, last855 = last_accepted(usf_ctrl_nums)
	dateRange = set_time_rng(error)
	status = 'FINDING FILES WITHIN DATE RANGE . . .'
	statusOutput(status)

	paths = create_paths(dateRange)
	paths2 = find_dir(paths)
	segmentFiles = check_file(paths2)
	reject_check(segmentFiles, last810, last855)


main_loop(error)
