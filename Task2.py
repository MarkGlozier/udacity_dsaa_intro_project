"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

calls_dict = {}
time_max = 0

for call in calls:
    number_in = call[0]
    number_out = call[1]
    time = call[3]

    try:
        calls_dict[number_in] += int(call[3])
    except KeyError:
        calls_dict[number_in] = int(call[3])
    
    try:
        calls_dict[number_out] += int(call[3])
    except KeyError:
        calls_dict[number_out] = int(call[3])
    
    if calls_dict[number_in] > time_max:
        time_max = calls_dict[number_in]
        number_max = number_in
    
    if calls_dict[number_out] > time_max:
        time_max = calls_dict[number_out]
        number_max = number_out

print(f"{number_max} spent the longest time, {time_max} seconds, on the phone during September 2016.")

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

