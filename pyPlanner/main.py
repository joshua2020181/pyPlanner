import datetime as dt
import calendar
import time
import threading

def run():
    while(True):
        time.sleep(0.5)
        print('hello')

def update():
    return dt.datetime.now()

class DateTime():
    now = update()
    def setNow():
        now = update()
    year = now.year
    month = now.month
    monthList = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    monthName = monthList[month]
    day = now.day
    hour = now.hour
    minute = now.minute
    second = now.second
    current = str(month) + '/' + str(day) + "/" + str(year) + ' ' + str(hour) + ':' + str(minute) + ':' + str(second)
    currentName = monthName + ' ' + str(day) + 'th, ' + str(year)

class CalendarData():
    def firstDayOfMonth(year, month): #day of the week of the first day of the month
        temp = calendar.monthrange(year, month)
        if(temp[0] == 6):
            return 0
        else:
            return temp[0] + 1
    def monthLength(year, month): #number of days in the month
        temp = calendar.monthrange(year, month)
        return temp[1]
    month = 5 #month that is being viewed
    def monthName(month):
        temp = calendar.month_name[month]
        return temp
    year = 5 #year that is being viewed

    def lengthBetween(first, second): #dates in the form of ['9/1/17', '9/1/18']
        first = first.split('/')
        second = second.split('/')
        d0 = dt.date(2000 + int(first[2]), int(first[0]), int(first[1]))
        d1 = dt.date(2000 + int(second[2]), int(second[0]), int(second[1]))
        return(d1-d0)

class SettingsData():
    name = ''
    schoolYearName = ''
    schoolYear = ''
    holidayNames = []
    holidays = [] #dates ex: 11/10/17
    nBlocks = 8
    nBlocksPerDay = 4
    dayRotation = 2 #how many day rotation scheduel (2)
    nClasses = 0 #number of classes
    classes = [] #list of classes (nClasses long)
    classLength = [] #length of that class (minutes) (nClasses long)

#class AssignmentsData():

while(False):
    DateTime
    DateTime.now = dt.datetime.now()
    print(DateTime.current)
    temp = dt.datetime.now()
    print(temp)
    time.sleep(1)
    th = threading.Thread(target = run)
    th.run()
