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
            for site in sites_that_consume_time:
                if site in content:
                    pass
                else:
                    file.write(redirect + '  ' + site + '\n')
    else:
        with open(hosts_path,'r+') as file:
            # the readlines method will produce a list with each str item
            content = file.readlines()
            # then check the readlines against our sites that consume time list, and if items are there in the host file,
            # I want to get rid of those lines. Once the readline is complete the point will be sitting at the very end of the
            # file, so any append writing will add from the poin of the pointer. The seek method will place the point were
            #we want in the beginning of the file.
            file.seek(0)
            for line in content:
                # check if there is a no time consuming site on the line, if no time consuming site on the line,
                # paste the same line as it was before no time consuming site was present, (nothing is changed, just recopy the
                # line)
                if not any(site in line for site in sites_that_consume_time):
                    file.write(line)
                    # truncate method will delete all things under the specified section bottom the pointer
            file.truncate()
            print('Non-working time: On; you may use the sites)
    time.sleep(120000)
