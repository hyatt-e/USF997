import os, re, datetime, pandas


# GLOBAL VARIABLES #
doctype = None

invalidDate_msg1 = "Please enter a valid date."
invalidDate_msg2 = "Dates may use '.' '-' '\\' or '/' to separate month, day, and year.\nYou may choose to use no separators, and instead enter an 8 digit string (ie. March 9, 1994 as 03091994)"
invalidDate_msg3 = "The End Date must be later than the Start Date"
invalidDate_msg4 = "You cannot select a date that is in the future."
tooManyErrors_msg10 = "Are you sure you're entering a date?"
exit_msg = "BYE."

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
startDate = ''
endDate = ''
singleDate = False
error = 0


usf_ctrl_nums = pandas.read_csv('G:\\WPy-3661\\python\\USF-997\\US Foods Control Numbers.csv', header=None)
# print(usf_ctrl_nums)
# usf_ctrl_nums.columns = ['DocType', 'LastDoc#']
last810 = None
last855 = None

status = None
# ---------------------------------------------------------------------- #


# usf_ctrl_nums = open('G:\\WPy-3661\\python\\USF-997\\US Foods Control Numbers.csv')
# usf_ctrl_nums = pandas.read_csv('G:\\WPy-3661\\python\\USF-997\\US Foods Control Numbers.csv', header=None)
# usf_ctrl_nums = pandas.read_csv('G:\\WPy-3661\\python\\USF-997\\US_Foods_Ctrl_Nums.csv', header=None)
# print(usf_ctrl_nums)
# usf_ctrl_nums = usf_ctrl_nums.drop([2,3,4], axis=1)
# usf_ctrl_nums.to_csv('G:\\WPy-3661\\python\\USF-997\\US_Foods_Ctrl_Nums.csv', header=None, index=False)
# usf_ctrl_nums.columns = ['DocType', 'LastDoc#']


def last_accepted(usf_ctrl_nums):
	docType = usf_ctrl_nums.iloc[0,0]
	if docType == "810's":
		last810 = int(usf_ctrl_nums.iloc[0, 1])

	docType = usf_ctrl_nums.iloc[2,0]
	if docType == "855's":
		last855 = int(usf_ctrl_nums.iloc[2, 1])

	print('Last document numbers:')
	print("810: {}".format(last810))
	print("855: {}".format(last855))
	return last810, last855


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
		# invalid 1
		# statusOutput(status)
		print(invalidDate_msg1, invalidDate_msg2)
		os.system("pause")
		error = 0
	if error == 2:
		# invalid 2
		# statusOutput(status)
		print(invalidDate_msg1, invalidDate_msg2)
		os.system("pause")
		error = 0
	if error == 3:
		# end date is before start date
		# statusOutput(status)
		print(invalidDate_msg1, invalidDate_msg2)
		print('\n')
		print(invalidDate_msg3)
		os.system("pause")
		error = 0
	if error == 4:
		# date is in the future
		# statusOutput(status)
		print(invalidDate_msg1, invalidDate_msg2)
		print('\n')
		print(invalidDate_msg4)
		os.system("pause")
		error = 0

	if error == 10:
		# more than 5 errors
		# statusOutput(status)
		print(invalidDate_msg1, invalidDate_msg2)
		print('\n')
		print(tooManyErrors_msg10)
		os.system("pause")
		error = 0
		exit = True
	if error == 11:
		print(exit_msg)
		os.system("pause")
		quit()


def set_time_rng(error):
	exit = False
	errorCnt = 0

	status = "SELECT DATE RANGE . . ."

	# TODO: add this back in
	# statusOutput(status)

	error_msg(error)

	while exit == False:
		# Take input for start date
		startDate = input("Start Date: ")

		if startDate.lower() == "exit":
			exit = True
			error = 11
			break
		else:
			mat = re.match("((\d{1,2})[\\\/\-.](\d{1,2})[\\\/\-.](\d{4}))|([\d{8}])", startDate)
			if mat != None:
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

				if endDate.lower() == "exit":
					exit = True
					error = 11
					break
				else:
					mat = re.match("((\d{1,2})[\\\/\-.](\d{1,2})[\\\/\-.](\d{4}))|([\d{8}])", endDate)
					if mat != None:
						# check that end date >= start date

						# check for '\'
						mat = re.search('[\\\]', endDate)
						if mat != None:
							endDate = valiDate(startDate, '\\', endDate)
							exit = True
						else:
							# check for '/'
							mat = re.search('[/]', endDate)
							if mat != None:
								endDate = valiDate(startDate, '/', endDate)
								exit = True
							else:
								# check for '-'
								mat = re.search('[-]', endDate)
								if mat != None:
									endDate = valiDate(startDate, '-', endDate)
									exit = True
								else:
									# check for '.'
									mat = re.search('[.]', endDate)
									if mat != None:
										endDate = valiDate(startDate, '.', endDate)
										exit = True

									# no separators; check length
									elif len(endDate) == 8:
										endMonth = endDate[:2]
										endDay = endDate[2:4]
										endYear = endDate[4:]
										endDate = endMonth + '-' + endDay + '-' + endYear
										endDate = valiDate(startDate, '-', endDate)
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

	if error != 0:
		error_msg(error)

	dateRange = pandas.date_range(start=startDate, end=endDate)
	dateRange = pandas.Series(dateRange.format())

	return dateRange


# TODO: refactor start to end: is there an end date being passed?
def valiDate(start, separator, end):
	if end == None:
		stMonth, stDay, stYear = start.split(separator)
		stMonth, stDay = dbl_digit(stMonth, stDay)
		startDate = stMonth + '-' + stDay + '-' + stYear
		future_date_chk(startDate)
		startDateList = [int(stMonth),int(stDay),int(stYear)]
		# print(months[startDate[0]-1], stDay + ',', stYear)
		print(months[int(stMonth)-1], stDay + ',', stYear)
		return startDate
	elif end != None:
		endMonth, endDay, endYear = end.split(separator)
		endMonth, endDay = dbl_digit(endMonth, endDay)
		endDate = endMonth + '-' + endDay + '-' + endYear
		future_date_chk(endDate)
		endDateList = [int(endMonth), int(endDay), int(endYear)]
		start_end_chk(start, endDate)
		# print(months[endDate[0] - 1], endDay + ',', endYear)
		print(months[int(endMonth)-1], endDay + ',', endYear)
		os.system("pause")
		return endDate


os.chdir('G:\\WPy-3661\\python\\USF-997\\IntIn-DEV\\')
dateRange = set_time_rng(error)


