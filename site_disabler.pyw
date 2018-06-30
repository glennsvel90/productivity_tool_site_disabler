import time
from datetime import datetime as dt


sites_that_consume_time = ['facebook.com', 'www.facebook.com', 'gmail.com', 'www.gmail.com',]

hosts_path = r'C:\Windows\System32\drivers\etc\hosts'
redirect = '127.0.0.1'

print(dt.now())

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 6) < dt.now() < dt(.now().year, dt.now().month, dt.now().day, 16):
        print('Working Hours Are On: ')
        with open(hosts_path,'r+') as file:
            content = file.read()
