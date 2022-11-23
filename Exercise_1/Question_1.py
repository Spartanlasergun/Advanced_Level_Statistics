# Question 1:
# (a) Draw a stemplot to show the masses, correct to the nearest kilogram, of 30 men.
#     Use intervals 50-54, 55-59, 60-64,...
# (b) Write down the modal mass.
#     74  52  67  68  71  76  86  81  73
#     68  64  75  71  61  63  57  67  57
#     59  72  79  64  70  74  77  79  65
#     68  76  83

import matplotlib.pyplot as plot

data = [74, 52, 67, 68, 71, 76, 86, 81, 73, 68, 64, 75, 71, 61, 63, 57, 67, 57, 59, 72, 79, 64, 70, 74, 77, 79, 65, 68, 76, 83]

stems = [5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8]

plot.ylabel("Stem")
plot.xlabel("Data")
plot.xlim(50, 90)
plot.stem(stems, data, orientation="horizontal")
plot.show()





