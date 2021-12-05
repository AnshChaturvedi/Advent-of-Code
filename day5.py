# read input file
file = open('day5.txt', 'r')
lines = file.readlines()

# clean input and store all points
points = []

for line in lines:
    current_line = line.split("->")
    points.append([tuple(map(int, current_line[0].split(","))), tuple(map(int, current_line[1].split(",")))])

# --------------------------- Part 1 ---------------------------

# points1 = [point for point in points if point[0][0] == point[1][0] or point[0][1] == point[1][1]]

# hashmap1 = {}

# # Note the number of occurences of each point in each line segment
# # Add info to hashmap1 for info retrieval after
# for point in points1:

#     x1, x2 = point[0][0], point[1][0]
#     y1, y2 = point[0][1], point[1][1]

#     x1y1 = point[0]
#     x2y2 = point[1]

#     if x1y1 in hashmap1:
#         hashmap1[x1y1] += 1
#     else: hashmap1[x1y1] = 1

#     if x2y2 in hashmap1:
#         hashmap1[x2y2] += 1
#     else: hashmap1[x2y2] = 1

#     # x coordinates are the same, we iterate on y
#     if x1 == x2:

#         # if y1 < y2
#         if y1 < y2:
            
#             while y1 != y2 - 1:
#                 y1 += 1
#                 new_point = (x1, y1)
#                 if new_point in hashmap1:
#                     hashmap1[new_point] += 1
#                 else: hashmap1[new_point] = 1

#         # if y1 > y2
#         elif y1 > y2:

#             while y1 != y2 + 1:
#                 y1 -= 1
#                 new_point = (x1, y1)
#                 if new_point in hashmap1:
#                     hashmap1[new_point] += 1
#                 else: hashmap1[new_point] = 1

#     # y coordinates are the same, we iterate on x
#     elif y1 == y2:

#         # if x1 < x2
#         if x1 < x2:

#             while x1 != x2 - 1:
#                 x1 += 1
#                 new_point = (x1, y1)
#                 if new_point in hashmap1:
#                     hashmap1[new_point] += 1
#                 else: hashmap1[new_point] = 1
            
#         # if x1 > x2
#         elif x1 > x2 + 1:

#             while x1 != x2 + 1:
#                 x1 -= 1
#                 new_point = (x1, y1)
#                 if new_point in hashmap1:
#                     hashmap1[new_point] += 1
#                 else: hashmap1[new_point] = 1
    
#     else:
#         points1.remove(point)

# # get count of points with an occurence >= 2
# score = 0
# for item in hashmap1:
#     if hashmap1[item] >= 2:
#         score += 1

# # prints out the answer
# # print(score)

# --------------------------- Part 2 ---------------------------

points2 = [point for point in points]

hashmap2 = {}

for point in points2:

    x1, x2 = point[0][0], point[1][0]
    y1, y2 = point[0][1], point[1][1]

    x1y1 = point[0]
    x2y2 = point[1]

    if x1y1 in hashmap2:
        hashmap2[x1y1] += 1
    else: hashmap2[x1y1] = 1

    if x2y2 in hashmap2:
        hashmap2[x2y2] += 1
    else: hashmap2[x2y2] = 1

        # x coordinates are the same, we iterate on y
    if x1 == x2:

        # if y1 < y2
        if y1 < y2:
            
            while y1 != y2 - 1:
                y1 += 1
                new_point = (x1, y1)
                if new_point in hashmap2:
                    hashmap2[new_point] += 1
                else: hashmap2[new_point] = 1

        # if y1 > y2
        elif y1 > y2:

            while y1 != y2 + 1:
                y1 -= 1
                new_point = (x1, y1)
                if new_point in hashmap2:
                    hashmap2[new_point] += 1
                else: hashmap2[new_point] = 1

    # y coordinates are the same, we iterate on x
    elif y1 == y2:

        # if x1 < x2
        if x1 < x2:

            while x1 != x2 - 1:
                x1 += 1
                if (x1, y1) in hashmap2:
                    hashmap2[(x1, y1)] += 1
                else: hashmap2[(x1, y1)] = 1
            
        # if x1 > x2
        elif x1 > x2 + 1:

            while x1 != x2 + 1:
                x1 -= 1
                if (x1, y1) in hashmap2:
                    hashmap2[(x1, y1)] += 1
                else: hashmap2[(x1, y1)] = 1
    
    # both coordinates are not the same
    else:
        if x1 < x2 and y1 < y2:

            while x1 != x2 - 1:
                x1 += 1
                y1 += 1
                if (x1, y1) in hashmap2:
                    hashmap2[(x1, y1)] += 1
                else: hashmap2[(x1, y1)] = 1
        
        if x1 > x2 and y1 > y2:

            while x1 != x2 + 1:
                x1 -= 1
                y1 -= 1
                if (x1, y1) in hashmap2:
                    hashmap2[(x1, y1)] += 1
                else: hashmap2[(x1, y1)] = 1
        
        if x1 < x2 and y1 > y2:
            
            while x1 != x2 - 1:
                x1 += 1
                y1 -= 1
                if (x1, y1) in hashmap2:
                    hashmap2[(x1, y1)] += 1
                else: hashmap2[(x1, y1)] = 1
        
        if x1 > x2 and y1 < y2:
            while x1 != x2 + 1:
                x1 -= 1
                y1 += 1
                if (x1, y1) in hashmap2:
                    hashmap2[(x1, y1)] += 1
                else: hashmap2[(x1, y1)] = 1

score2 = 0

# counts instances of count > 2
for item in hashmap2:
    if hashmap2[item] > 1:
        score2 += 1

# prints the result!
# print(score2)