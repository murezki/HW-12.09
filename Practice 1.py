import datetime


current_datetime = datetime.datetime.now()
print("текущая дейттайм", current_datetime)

current_year = current_datetime.year
print("Текущий год:", current_year)

current_month = current_datetime.strftime("%B")
print("месяц года", current_month)

week_number = current_datetime.strftime("%U")
print("номер недели в году", week_number)

weekday = current_datetime.strftime("%A")
print("будний день недели", weekday)

day_of_year = current_datetime.timetuple().tm_yday
print("день года", day_of_year)

day_of_month = current_datetime.day
print("день месяца", day_of_month)

day_of_week = current_datetime.weekday() + 1
print("день недели", day_of_week)





def visokosniy(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
god = 2020
if visokosniy(god):
    print(f"високосный {god}")
else:
    print(f"не високосный{god}")



