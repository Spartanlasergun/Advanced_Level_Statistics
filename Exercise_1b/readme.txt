The term histogram was coined by Karl Pearson, who in doing research involving 
historical statistics, thought that the histogram would be particularly useful
in such endeavours as it represented continuous data. Of course, there is nothing
in a histogram itself that makes it more so suited to the task of representing
continuous quantitative data than any other. However, this fact has misled many 
to beleive that the histogram is used primarily with reference to historical data.

There are some issues with plotting histograms using the matplotlib module, as well
as other modules. The primary issue is that the dataplot produced by matplotlib 
does not calculate or use frequency density as part of its plot. Instead, the 
frequency is plotted directly against the interval width. In addtion, their does
not seem to be any way to plot bivariate data using matplotlib, and the module
can only process the raw data set - this essentially means that in answering the
questions where the sorted data is provided, I am left with the task of recreating
the raw data set for use with matplotlib.