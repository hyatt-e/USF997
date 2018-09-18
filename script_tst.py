import os, time
from time import mktime
# import DateTimeRange
from datetime import datetime


# TODO: use ttkCalendar


def set_time_rng():
	tm = time.localtime()
	# TODO: allow for time range
	# TODO: adjust time to fit the range specified by user
	# default time range: last 36hrs

	dt = datetime.fromtimestamp(mktime(tm))
	dt[0] = 2018
	dt[1] = 9
	dt[2] = 10
	print(tm)


set_time_rng()
