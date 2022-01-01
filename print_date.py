
from datetime import datetime
import pytz

dt = datetime.now(pytz.timezone('Asia/Kolkata'))
print(dt.strftime("%H:%M %p"))
