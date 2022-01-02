# import sys
# for path in sys.path:
#     print(path)


# from datetime import datetime
# import pytz
# dt = datetime.now(pytz.timezone('Asia/Kolkata'))
# print(dt.strftime("%H:%M %p"))
#

from common import Date
dt = Date.now()
print(repr(dt))
