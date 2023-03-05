# Notes on this exercise

This exercise deal with the manipulation of datasets to change the mean or standard deviation to a specified value

To understand how this is done, we must examine the effect of basic arithmetic operation on datasets.

Consider the dataset {1, 2, 3, 4, 5, 6, 7}

* The mean $\bar x$, of this dataset is = 4
* It's standard deviation $\sigma$, is = 2

What happens if add a constant value ' $c$ ', to each number in the dataset? How does the mean and standard deviation change?

Let's examine this using our dataset {1, 2, 3, 4, 5, 6, 7}

Adding '5' to each number in the dataset, (i.e. $f(x) = x_n + 5$ ) gives the following:

{6, 7, 8, 9, 10, 11, 12}

The new mean $\bar x$, is = 7, and the standard deviation is unchanged (i.e. $\sigma = 2$)

On closer observation, we can generalize this understanding as follows: 

* If each number in the dataset is increased by a constant $c$, :
  * The mean is increased by $c$, that is to say, $\bar x + c$ 
  * and, the standard deviation remains unaltered
  
 So we know what happens to the mean and standard deviation when we add a constant to each value, but what happens when we multiply each value by the constant $k$ ?
 
 Lets examine this using our dataset {1, 2, 3, 4, 5, 6, 7}
 
 Multiplying each number in the dataset by the number 2, (i.e. $f(x) = x * 2$ ) gives the following:
 
 {2, 4, 6, 4, 10, 12, 14}
 
 The new mean $\bar x$, is = 8, and the new standard deviation $\sigma$, is = 4

As with addition operations, we can generalize the understanding for multiplication as follows:

* If each number in the dataset is muliplied by a constant $k$, :
  * The mean of the dataset is multiplied by $k$, i.e. $\bar x * k$
  * and, the standard deviation is also multiplied by $k$, i.e. $\sigma * k$












