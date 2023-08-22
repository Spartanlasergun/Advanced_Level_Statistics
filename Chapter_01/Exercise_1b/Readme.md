# Notes on this exercise

The term histogram was coined by Karl Pearson, who in doing research involving historical statistics, thought that the histogram would be particularly useful in such
endeavours as it represented continuous data. Of course, there is nothing in a histogram itself that makes it more so suited to the task of representing continuous 
quantitative data than any other. However, this fact has misled many to beleive that the histogram is used primarily with reference to historical data.

There are some issues with plotting histograms using the matplotlib module, as well as other modules. The primary issue is that the dataplot produced by matplotlib 
does not calculate or use frequency density as part of its plot. Instead, the frequency is plotted directly against the interval width. In addtion, the module can only
process the raw data set - this essentially means that in answering the questions where the sorted data is provided, I am left with the task of recreating the raw data
set for use with matplotlib.

Since the text specifically asks for a histogram plot that utilizes frequency density, some of the answers provided may not be accurate with respect to the question
itself. However, since the dataplot for the raw frequencies only vary from the frequency density plot where the intervals are non-uniform, many of the answers given will
still appear as accurate data visualizations.
