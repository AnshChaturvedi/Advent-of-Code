# read input
file1 = open('day3.txt', 'r')
lines = file1.readlines()

# --------------------------- Part 1 ---------------------------

length = len(lines[0]) - 1

# consumes lines of text returns the gamma binary number
def get_gamma_number(lines):

    number = []

    for i in range(length):
        zero_count = 0
        one_count = 0
        for line in lines:
            if line[i] == "0":
                zero_count += 1
            else: 
                one_count += 1
        
        if zero_count > one_count:
            number.append(0)
        else: number.append(1)
    
    final_number = ("".join([str(i) for i in number]))
    return final_number

# consumes gamma number (binary) and returns epsilon number
def get_epsilon_number(number):
    gamma = list(str(number))
    new_epsilon = []
    for num in gamma:
        if num == "0":
            new_epsilon.append("1")
        elif num == "1":
            new_epsilon.append("0")
    
    new_epsilon = ("".join([str(i) for i in new_epsilon]))
    return new_epsilon


gamma = get_gamma_number(lines)
epsilon = get_epsilon_number(gamma)
# print(int(gamma, 2) * int(epsilon, 2))

# --------------------------- Part 2 ---------------------------

# gets the value needed to strip by
def get_larger_value(lines, i):
    zero = 0
    one = 0

    for line in lines:
        if line[i] == "0":
            zero += 1
        else: one += 1
    
    if zero > one: return str(0)
    else: return str(1)

# sorts the number based by number (could've used map here)
def strip_by_num(lines, num, i):
    stripped = []
    for line in lines:
        if line[i] == str(num):
            stripped.append(line)
    
    return stripped

# helper to run main recursive function
def get_oxygen(lines):
    return get_oxygen_rec(lines, 0)

def get_oxygen_rec(lines, i):
    if len(lines) == 1:
        return lines[0].rstrip("\n")
    else:
        num_to_strip = get_larger_value(lines, i)
        stripped = strip_by_num(lines, num_to_strip, i)
        return get_oxygen_rec(stripped, i+1)

# gets the smaller value needed to strip by
def get_smaller_value(lines, i):
    zero = 0
    one = 0

    for line in lines:
        if line[i] == "0":
            zero += 1
        else: one += 1
    
    if zero > one: return str(1)
    else: return str(0)

# helper to call main recursive function
def get_co2(lines):
    return get_co2_rec(lines, 0)

def get_co2_rec(lines, i):
    if len(lines) == 1:
        return lines[0].rstrip("\n")
    else:
        num_to_strip = get_smaller_value(lines, i)
        stripped = strip_by_num(lines, num_to_strip, i)
        #print(stripped)
        return get_co2_rec(stripped, i+1)

# get the answers!
oxygen = int(get_oxygen(lines), 2)
co2 = int(get_co2(lines), 2)
print(oxygen * co2)



