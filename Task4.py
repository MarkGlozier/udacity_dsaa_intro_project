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


# If number makes a call, that number could be a telemarketer, unless conditions below are met
telemarketer_dict = {call[0]: True for call in calls} 

for call in calls:
    telemarketer_dict[call[1]] = False # If number receieves a call, that number is not a telemarketer

for text in texts:
    telemarketer_dict[text[0]] = False # If number sends a text, that number is not a telemarketer
    telemarketer_dict[text[1]] = False # If number receives a text, that number is not a telemarketer

telemarketer_numbers = set()

for k,v in telemarketer_dict.items():
    if v is True:
        telemarketer_numbers.add(k)

print("These numbers could be telemarketers: ", *sorted(telemarketer_numbers), sep="\n")

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

