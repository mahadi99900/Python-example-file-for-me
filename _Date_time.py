import calendar
from datetime import datetime

yy = datetime.now().year
mm = datetime.now().month
time = datetime.now()
full_month = calendar.month(yy,mm)
today = datetime.today()
day_name = calendar.day_name[today.weekday()]

print(f"Today datetime;\nTime; {time}\nDay name; {day_name}\nDate; {mm}\nYear; {yy}\nand Calendar: \n{full_month}")
