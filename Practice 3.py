import datetime

current_time = datetime.datetime.now().time()
print(current_time.strftime('%H: %M: %S.%f')[:-3])