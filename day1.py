with open('day1input.txt', 'r') as f:
    list = f.read().splitlines()
    
def first_and_last_number(line):
    digits = ''

    for char in line.split():
        if char.isdigit():
            digits.append(char)
    return digits
    

print(list[0])
print(first_and_last_number(list[0]))
