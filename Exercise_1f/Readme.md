# Notes on this exercise

This Exercise deals with calculations of the Standard Deviation and Variance.

The formula given for Standard Deviation is $\sigma = \sqrt \Sigma (x - \mu)^2 / n $

The standard deviation represents the average distance of each data point from the mean. Hence, it is sometimes referred to as the standard error of the mean.

### Derivation of the Standard Deviation: Basic Principles and Thoughts

The part of the equation $\Sigma (x - \mu)$ is essentially calculating the distance from the mean for each data point.

* The mean itself is the center of the data. So, the sum of the distances for each data point from the center is equal to zero. 
To avoid this zero error, the distances are squared and we get the formula: 
$\Sigma (x - \mu)^2$

* Of Course, we want the average of this distance for the entire dataset, so we divide by the size of the samle 'n'. 
The result is the equation:
$\Sigma (x - \mu)^2 / n$

* Finally, we need to remember that we squared the initial value for the deviation. For the standard error of the mean
to be representative of the original sample, we need to find it's square root. The result is the equation for
standard deviation as we know it: $\sigma = \sqrt \Sigma (x - \mu)^2 / n $



