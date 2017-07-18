import sys

def get_time(hours, minutes, seconds):
    return str(hours).zfill(2) + ':' + str(minutes).zfill(2)  + ':' + str(seconds).zfill(2)

def timeConversion(s):
    is_PM  = s[8:] == 'PM'
    hours, minutes, seconds = map(int, s[:8].split(':'))
    if is_PM and hours < 12:
        hours += 12
    elif not is_PM and hours == 12:
        hours = 0
    return get_time(hours, minutes, seconds)

s = input().strip()
result = timeConversion(s)
print(result)