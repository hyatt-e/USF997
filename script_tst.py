import os, time, re
from time import mktime
# import DateTimeRange
from datetime import datetime

# GLOBAL
invalidDate_msg1 = "Please enter a valid date."
invalidDate_msg2 = "Dates may use '.' '-' '\\' or '/' to separate month, day, and year.\nYou may choose to use no separators, and instead enter an 8 digit string (ie. March 9, 1994 as 03091994 "
tooManyErrors_msg = "You're not worthy of this application. BYE."

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


def set_time_rng():
	exit = False
	errorCnt = 0


	os.system('cls')
	print("Please enter dates with the month, followed by day, followed by year.\n"
	      "'.' '-' '\\' or '/' are acceptable separators\n")

	while exit == False:

		os.system('cls')

		# Take input for start date
		startDate = input("Start Date: ")
		mat = re.match("((\d{1,2})[\\\/\-.](\d{1,2})[\\\/\-.](\d{2,4}))|([\d{8}])", startDate)
		if startDate.lower() == "exit":
			exit = True
			break
		elif mat != None:
			# TODO: parse/split date and reprint in 'MONTH dd, YYYY' format; as success message

			# check for '\'
			mat = re.search('[\\\]', startDate)
			if mat != None:
				stMonth, stDay, stYear = startDate.split("\\")
				print(months[stMonth], stDay, ',', stYear)
			else:
				# check for '/'
				mat = re.search('[/]', startDate)
				if mat != None:
					stMonth, stDay, stYear = startDate.split("/")
					print(months[stMonth], stDay, ',', stYear)
				else:
					# check for '-'
					mat = re.search('[-]', startDate)
					if mat != None:
						stMonth, stDay, stYear = startDate.split("-")
						print(months[stMonth], stDay, ',', stYear)
					else:
						# check for '.'
						mat = re.search('[.]', startDate)
						if mat != None:
							stMonth, stDay, stYear = startDate.split(".")
							print(months[stMonth], stDay, ',', stYear)

						# no separators; check length
						elif len(startDate) == 8:
							stMonth = int(startDate[:2])
							stDay = startDate[2:4]
							stYear = startDate[4:]
							print(months[stMonth], stDay, ',', stYear)
						else:
							print(invalidDate_msg1, invalidDate_msg2)


			print("cool!")
			#
			# Take input for end date
			#
			endDate = input("End Date: ")
			# matEnd = re.match("(\d{1,2})[\\\/\-.](\d{1,2})[\\\/\-.](\d{2,4})", endDate)
			mat = re.match("((\d{1,2})[\\\/\-.](\d{1,2})[\\\/\-.](\d{2,4}))|([\d{8}])", endDate)
			if startDate.lower() == "exit":
				exit = True
				break
			elif mat != None:
				# TODO: parse/split date and reprint in 'MONTH dd, YYYY' format; as success message
				# TODO: check that end date >= start date
				print("cool!")
			elif errorCnt == 0:
				print(invalidDate_msg1)
				errorCnt += 1
			elif errorCnt >= 5:
				print(tooManyErrors_msg)
				exit = True
				break
			else:
				print(invalidDate_msg2)
				errorCnt += 1

		elif errorCnt == 0:
			print(invalidDate_msg1)
			errorCnt +=1
		elif errorCnt >= 5:
			print(tooManyErrors_msg)
			exit = True
			break
		else:
			print(invalidDate_msg2)
			errorCnt += 1


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


set_time_rng()
