# Notes on this exercise

There is a formula given in this exercise that calculates the growth of the radius of a pie chart in relation to a growth of a population. The idea is that as the
poulation grows, the pie chart itself should become larger in diameter to represent that growth. The formula is as follows:

` r_1 / r_2 = (sqrt(F_1)) / (sqrt(F_2))`

r_1 is the radius of the initial pie chart

F_1 and F_2 are the population sizes

In the real world of data, the purpose of data visualization is to present data in a way that's easy to read, and accurate. With this in mind, it does not matter if you
use the formula above to calculate the growth of a pie chart - a simple percentage calculation would work just as well. Ultimately, the limitations are based on the
size of the canvas in question, i.e. the piece of paper, or the screen that you are using. 

As it concerns the accuracy of the pie chart, the most suitable formula for representing the population would be the Circumference of a Circle, or the Area of a circle:

` n = (pi * r)^2`

or

` n = 2 * pi * r`

Where n is the population size. This way, the growth of the pie-chart will be uniform with respect to its center.
