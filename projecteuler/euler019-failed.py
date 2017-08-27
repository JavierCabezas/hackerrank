#Project Euler #19: Counting Sundays

from collections import namedtuple
number_of_testcases = int(input())
Date = namedtuple('Date', 'year, month, day')
DateRange = namedtuple('DateRange', 'start, end')
dates = []
max_year = 1899

for date in range(number_of_testcases):
    initial_temp = list(map(int, input().split(" ")))
    ending_temp= list(map(int, input().split(" ")))
    initial_date = Date(year=initial_temp[0], month=initial_temp[1], day=initial_temp[2])
    ending_date = Date(year=ending_temp[0], month=ending_temp[1], day=ending_temp[2])
    if ending_date.year > max_year:
        max_year = ending_date.year
    dates.append(DateRange(start=initial_date, end=ending_date))

def get_days_per_month(month_number, year):
    if month_number in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    if month_number > 2:
        return 30
    else: #feb
        if year % 4 != 0 or year % 400 == 0:
            return 28
        else:
            return 29

days_per_year = {}
def fill_year_array(end_year):
    global days_per_year
    for y in range(1900, end_year+1):
        days_per_year[y] = 337 + get_days_per_month(2, y)
fill_year_array(max_year)


def get_days_in_interval_same_year(start, end):
    if start.month == end.month:
        return end.day - start.day
    days = 0
    days += get_days_per_month(start.month, start.year) - start.day
    days += end.day
    for month in range(start.month + 1, end.month):
        days += get_days_per_month(month, start.year)
    return days

def get_days_in_interval(start, end):
    total_days = 0
    if start.year == end.year:
        return  get_days_in_interval_same_year(start, end)
    else:
        end_of_start_year = Date(year=start.year, month=12, day=31)
        start_of_end_year = Date(year=end.year, month=1, day=1)
        total_days += get_days_in_interval_same_year(start, end_of_start_year)
        total_days += get_days_in_interval_same_year(start_of_end_year, end)
        for year in range(start.year +1, end.year):
            total_days += days_per_year[year]

        return total_days

for date in dates:
    days_difference = get_days_in_interval(date.start, date.end)
    print(days_difference // 7)