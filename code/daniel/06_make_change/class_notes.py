import csv

# with open('location.csv', 'w') as file:
#     writer = csv.writer(file)
#     writer.writerow(['City', 'State', 'Zip'])
#     writer.writerow(['Portland', 'OR', '97202'])
#     writer.writerow(['Lake Oswego', 'OR', '97304'])


# with open('location.csv') as file:
#     reader = csv.reader(file)
#     print(list(reader))

#     for row in reader:
#         # print(row)
#         if len(row) > 1:
#             print(row)



# import time
# # print(time.time())


# def send_communication():
#     for i in range(30000):
#         pass

# start_time = time.time()
# send_communication()
# end_time = time.time()
# duration = end_time - start_time
# # print(duration)

# print(f'It took {duration} seconds to update 30k patients')



# import datetime

# dt = datetime.datetime(2022, 1, 1)
# print(dt)





# from datetime import datetime
# dt = datetime(2022, 1, 1)
# print(dt)

from datetime import datetime
# from django.forms import DateTimeInput


# dt = datetime.strptime("2022/01/01", "%Y/%m/%d")
# print(f'{dt.year}/{dt.month}')



# dt = datetime.now()
# print(dt.strftime("%Y/%m"))


# dt_start = datetime(2022, 1, 1)
# dt_end = datetime.now()
# duration = dt_end - dt_start
# print(duration)
# print('days', duration.days)
# print('seconds', duration.seconds)
# print('total_seconds', duration.total_seconds())



# dt_plus1 = datetime(2022, 1, 1) + timedelta(days=1, seconds=1)


# print(dt_plus1)



import random

# print(random.random(), 'random')
# print(random.randint(1, 25), 'ranint')
# print(random.choice([10, 20, 30, 40]), 'choice')
# print(random.choices([10, 20, 30, 40], k=2), 'choices')



# print(random.choices(['sljkhj'], k=2 ))
# print(''.join(random.choices('sljkhj')))
# print(','.join(random.choices('sljkhj')))

import string

# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.digits)


# print(''.join(random.choices(string.ascii_letters + string.digits, k=7)))


# special_chars = string.punctuation
# print(special_chars)


import webbrowser
print('Checking site')
webbrowser.open('http://pdxcodeguild.com')









































