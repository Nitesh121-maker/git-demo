from datetime import date
import calendar
yy=int(input("Enter the Year:"))

current_date = date.today()
print(current_date,calendar.day_name[current_date.weekday()])
print(calendar.calendar(yy))