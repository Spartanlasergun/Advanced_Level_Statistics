# Notes on this exercise

This Exercise deals with calculations of the Standard Deviation and Variance.

The formula given for Standard Deviation is $\sigma$ = $\sqrt{(\Sigma (x - \mu)^2) \over n} $

The standard deviation represents the average distance of each data point from the mean. The orginal formula was known as the 'Root Mean Square Error'; this is because
the principle behind its derivation results from trying to reconcile the error that occurs when calculating $\Sigma (x - \mu)$. Hence, it is sometimes referred to as
the standard error of the mean.

### Derivation of the Standard Deviation: Basic Principles and Thoughts

This part of the standard deviaton equation $\Sigma (x - \mu)$ , calculates the distance from the mean for each data point.

* The mean itself is the center of the data. So, the sum of the distances for each data point from the center is equal to zero, i.e the sum of the deviations from the
mean for each data point is zero. To avoid this zero error, the distances are squared and we get the formula: 
$\Sigma (x - \mu)^2$

* Of Course, we want the average of this distance for the entire dataset, so we divide by the size of the sample 'n'. The result is the equation: 
$\Sigma (x - \mu)^2 \over n$

* Finally, we need to remember that we squared the initial value for the deviation. For the standard error of the mean to be representative of the original sample, we
need to find it's square root. The result is the equation for standard deviation as we know it: 
$\sqrt {\Sigma (x - \mu)^2 \over n} $

Ulitmately, measures of standard deviation based on the 'root mean square error' are less precise than it's counterpart - the Mean Absolute Deviation. The principle
behind the two equations are the same - the difference arises in the way that they handle the error that results from trying to sum the deviations from the mean.
Instead of taking the square, the Mean Absolute Deviation takes the modulus: $\Sigma |x - \mu| \over n$.

The question then inevitably arises; Why use the 'Root Mean Square Error', when the 'Mean Absolute Deviation' is more precise?

The answer is not exactly a simple one, but looking at the Variance ( $\sigma^2$ ), we can get a sense of what these statistical measurments really represent and how
they function in the real world. To begin, we need to answer the following question: "What is the Variance?"

In the simplest terms, the Variance is a number that represents the spread of a data set. Looking at this number by itself does not really say much about any given
dataset - in this respect, it is an attribute of a dataset that changes as the data within the dataset itself changes. Because of the root mean square error, the
changes in variance are much more pronounced than an absolute statistic such as the "Mean Absolute Deviation". This means that for correlation to exist between
multiple variances across multiple sets of data, a much higher level of relation needs to exist between the data points themselves. When it comes to making predictions
this quality of the variance as being much more fickle a statistic, makes it invaluable when compared to absolute values such as the 'Mean Absolute Deviation'.


