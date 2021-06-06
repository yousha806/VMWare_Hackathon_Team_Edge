import csv

MAIL = 'youshasunil@gmail.com'



ALERT = True

file=open("output.csv")
reader=csv.reader(file)
lines= len(list(reader))
Threshold=lines-1
# Threading ON/OFF
Thread = False
# Simple log to log the counting data
Log = False

Scheduler = False

Timer = False

