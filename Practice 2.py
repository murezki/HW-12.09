from datetime import datetime

string = "1 февраля 2008 06:09"
format1 = '%d %B %Y %H:%M'
format2 = '%Y-%m-%d %H:%M:%S'

parsed_datetime = datetime.strptime(string, format1)
output_date_string = parsed_datetime.strftime(format2)
print(output_date_string)

