from datetime import datetime
number_of_testcases = int(input())
dates = []

date_format = '%a %d %b %Y %H:%M:%S %z'
for i in range(number_of_testcases):
    initial_date = datetime.strptime(input(), date_format)
    final_date = datetime.strptime(input(), date_format)
    dates.append({
        'initial': initial_date,
        'final': final_date
    })


for date_pair in dates:
    seconds = (abs(date_pair['initial'] - date_pair['final'])).total_seconds()
    print(int(seconds))