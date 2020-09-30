import time
import os
import pandas

while True:
    if os.path.exists('files/temp.csv'):
       data = pandas.read_csv('files/temp.csv')
       print(data.mean())
    else:
        print('error')

    time.sleep(5)


