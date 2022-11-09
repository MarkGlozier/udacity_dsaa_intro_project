"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


area_codes = set()
count_bangalore_to_bangalore = 0
count_bangalore_to_any = 0

for call in calls:
    if call[0][0:5] == "(080)":
        area_code = ""
        if call[1][0:2] == "(0":
            for n in call[1][1:]:
                if n == ")":
                    break
                area_code += n
                if area_code == "080":
                  count_bangalore_to_bangalore += 1
        elif call[1][0:3] == "140":
            area_code = 140
        else:
            area_code = call[1][0:4]
        area_codes.add(area_code)
        count_bangalore_to_any += 1
        

print("The numbers called by people in Bangalore have codes:", *sorted(area_codes), sep="\n")

percentage_bangalore_to_bangalore = 100 * count_bangalore_to_bangalore / count_bangalore_to_any

# Round manually (without using built-in round function)
for idx, i in enumerate(str(percentage_bangalore_to_bangalore)):
  if i == ".":
    idx_dot = idx
    break

if int(str(percentage_bangalore_to_bangalore)[idx_dot+1:idx_dot+4][-1]) < 5:
  percentage_bangalore_to_bangalore_2dp = str(percentage_bangalore_to_bangalore)[:idx_dot+3]
else:
  percentage_bangalore_to_bangalore_2dp = str(float(str(percentage_bangalore_to_bangalore)[:idx_dot+3]) + 0.01)[:idx_dot + 3]

# Round using round function (Disabled, unsure whether this is allowed for this project)
# percentage_bangalore_to_bangalore = round(percentage_bangalore_to_bangalore, 2)

print(f"{percentage_bangalore_to_bangalore_2dp} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
