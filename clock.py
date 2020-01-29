#Importations
import os
import time
#Clear Screen
def cls():
    os.system('cls')
#Clock Program
def clock():
    hour = 0
    minute = 0
    second = 0
    timeday = 1
    day = 'am'
    while True:
        print ("            H M S")
        print ("The time is: %s" % str(hour) + ":%s" % str(minute) + ":%s" % str(second) + " %s" % day)
        time.sleep(1)
        cls()
        second += 1
        if second == 60:
            minute += 1
            second = 0
        if minute == 60:
            hour += 1
            minute = 0
        if hour == 12:
            timeday += 1
            hour = 0
        if timeday == 1:
            day = 'am'
        if timeday == 2:
            day = 'pm'
        if timeday == 3:
            timeday = 1
#Launch Function
if __name__ == "__main__":
    clock()
