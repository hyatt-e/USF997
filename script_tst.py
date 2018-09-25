import os, time, re
from time import mktime
# import DateTimeRange
import datetime

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
							stMonth = int(startDate[:2])
							stDay = int(startDate[2:4])
							stYear = int(startDate[4:])
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
					# endMonth, endDay, endYear = endDate.split("\\")
					# endDate = [int(endMonth),int(endDay),int(endYear)]
					# start_end_chk(startDate, endDate)
					# future_date_chk(endDate)
					# print(months[endDate[0]-1], endDay + ',', endYear)
					# os.system("pause")
				else:
					# check for '/'
					mat = re.search('[/]', endDate)
					if mat != None:
						endDate = valiDate(endDate, '/', startDate)
						exit = True
						# endMonth, endDay, endYear = endDate.split("/")
						# endDate = [int(endMonth), int(endDay), int(endYear)]
						# start_end_chk(startDate, endDate)
						# future_date_chk(endDate)
						# print(months[endDate[0] - 1], endDay + ',', endYear)
						# os.system("pause")
					else:
						# check for '-'
						mat = re.search('[-]', endDate)
						if mat != None:
							endDate = valiDate(endDate, '-', startDate)
							exit = True
							# endMonth, endDay, endYear = endDate.split("-")
							# endDate = [int(endMonth), int(endDay), int(endYear)]
							# start_end_chk(startDate, endDate)
							# future_date_chk(endDate)
							# print(months[endDate[0] - 1], endDay + ',', endYear)
							# os.system("pause")
						else:
							# check for '.'
							mat = re.search('[.]', endDate)
							if mat != None:
								endDate = valiDate(endDate, '.', startDate)
								exit = True
								# endMonth, endDay, endYear = endDate.split(".")
								# endDate = [int(endMonth), int(endDay), int(endYear)]
								# start_end_chk(startDate, endDate)
								# future_date_chk(endDate)
								# print(months[endDate[0] - 1], endDay + ',', endYear)
								# os.system("pause")

							# no separators; check length
							elif len(endDate) == 8:
								endMonth = int(endDate[:2])
								endDay = int(endDate[2:4])
								endYear = int(endDate[4:])
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


	# tm = time.localtime()
	# # TODO: allow for time range
	# # TODO: adjust time to fit the range specified by user
	# # default time range: last 36hrs
	#
	# dt = datetime.fromtimestamp(mktime(tm))
	# dt[0] = 2018
	# dt[1] = 9
	# dt[2] = 10
	# print(tm)


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


set_time_rng(error)
