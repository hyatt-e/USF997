import os, re, datetime, pandas, pickle
from datetime import timedelta, date


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


yesterday = date.today() - timedelta(1)
yesterday = yesterday.strftime('%m-%d-%Y')
print(yesterday)