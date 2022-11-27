# Question 1:
# (a) Draw a stemplot to show the masses, correct to the nearest kilogram, of 30 men.
#     Use intervals 50-54, 55-59, 60-64,...
# (b) Write down the modal mass.
#     74  52  67  68  71  76  86  81  73
#     68  64  75  71  61  63  57  67  57
#     59  72  79  64  70  74  77  79  65
#     68  76  83

import matplotlib.pyplot as plot

# Data set for the problem above
data = [74, 52, 67, 68, 71, 76, 86, 81, 73, 68, 64, 75, 71, 61, 63, 57, 67, 57, 59, 72, 79, 64, 70, 74, 77, 79, 65, 68, 76, 83]
data.sort()   # sort the data in ascending order for the stemplot

# sort the data based on the interval range specified for the problem
range_50_54 = []
range_55_59 = []
range_60_64 = []
range_65_69 = []
range_70_74 = []
range_75_79 = []
range_80_84 = []
range_85_89 = []
for number in data:
    if (number >= 50) and (number <= 54):
        range_50_54.append(number)
    elif (number >= 55) and (number <= 59):
        range_55_59.append(number)
    elif (number >= 60) and (number <= 64):
        range_60_64.append(number)
    elif (number >= 65) and (number <= 69):
        range_65_69.append(number)
    elif (number >= 70) and (number <= 74):
        range_70_74.append(number)
    elif (number >= 75) and (number <= 79):
        range_75_79.append(number)
    elif (number >= 80) and (number <= 84):
        range_80_84.append(number)
    elif (number >= 85) and (number <= 89):
        range_85_89.append(number)
intervals = [range_50_54, range_55_59, range_60_64, range_65_69, range_70_74, range_75_79, range_80_84, range_85_89]

# create stem data based on ranges
stems = []
unit = 50
for interval in intervals:
    count = len(interval)
    while count != 0:
        stems.append(unit)
        count = count - 1
    unit = unit + 5

leaves = []
for leafs in data:
    leafs = str(leafs)
    leaf = leafs[1]
    leaves.append(int(leaf))

print(stems)
print(leaves)

plot.ylabel("Stem")
plot.xlabel("Data")
plot.xlim(0, 10)
plot.stem(stems, leaves, orientation="horizontal")
plot.show()





