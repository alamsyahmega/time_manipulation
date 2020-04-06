import calendar
import time
time_end = 1640995200
time_start = 1577836800


def looping_time_per_month(time_start, time_end):
    start = time_start
    date = time.strftime('%m/%Y', time.gmtime(start))
    get_month = date.split("/")
    long_day = calendar.monthrange(int(get_month[1]), int(get_month[0]))[1]
    end = start + (60*60*24*long_day)

    while end <= time_end:
        print(f'start: {start},  end: {end} ')
        date = time.strftime('%d/%m/%Y', time.gmtime(start))
        get_month = date.split("/")
        month = int(get_month[1])
        year = int(get_month[2])
        month_next = 1
        if month == 12:
            year += 1
            month = 1
            month_next = 0
        print(month, year, month_next)
        long_day = calendar.monthrange(year, month + month_next)[1]
        print(date, 'long day: ', long_day)

        start = end
        end = start + (60*60*24*long_day)

looping_time_per_month(time_start, time_end)