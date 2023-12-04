import re

with open('day1input.txt', 'r') as f:
    lista = f.read().splitlines()
    
def first_and_last_number(line):
    digits = [int(i) for i in line if i.isdigit()]
    last_and_first = digits[0] * 10 + digits[-1]
    return last_and_first

sum_calibration = sum([first_and_last_number(line) for line in lista])
print(sum_calibration)

# B

valid = {
    "zero": "0",
    "one" : "1",
    "two" : "2",
    "three" : "3",
    "four" : "4",
    "five" : "5",
    "six" : "6",
    "seven" : "7",
    "eight": "8",
    "nine" : "9",
}

def multiple_replace(replacements, text):
    # Create a regular expression from the dictionary keys
    regex = re.compile("(%s)" % "|".join(map(re.escape, replacements.keys())))
    # For each match, look-up corresponding value in dictionary
    return regex.sub(lambda mo: replacements[mo.group()], text) 


tot = 0
for line in lista: 
    print(first_and_last_number(multiple_replace(valid, line)))
    print(line)
    tot += first_and_last_number(multiple_replace(valid,line))
    
print(tot)