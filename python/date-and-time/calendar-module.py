import calendar

entry = input().split(" ")
month, day, year = int(entry[0]), int(entry[1]), int(entry[2]) #This format is so stupid

c = calendar.weekday(year, month, day)
print(calendar.day_name[c].upper())