# read contents
file1 = open('test.txt', 'r')
lines = file1.readlines()

# --------------------------- Part 1 ---------------------------

# solves the puzzle
def solve1(lines):
    forward = 0
    depth = 0

    for line in lines:
        dir = line.split()
        if dir[0] == 'up':
            depth-=int(dir[1])
        elif dir[0] == 'down':
            depth+=int(dir[1])
        elif dir[0] == 'forward':
            forward+=int(dir[1])
    
    return forward * depth

# gets the answer!
print(solve1(lines))

# --------------------------- Part 2 ---------------------------

# solves the puzzle
def solve2(lines):
    forward = 0
    depth = 0
    aim = 0

    for line in lines:
        dir = line.split()
        if dir[0] == 'up':
            aim-=int(dir[1])
        elif dir[0] == 'down':
            aim+=int(dir[1])
        elif dir[0] == 'forward':
            forward+=int(dir[1])
            depth+=(int(dir[1])*aim)
    
    return forward * depth

# gets the answer!
print(solve2(lines))
