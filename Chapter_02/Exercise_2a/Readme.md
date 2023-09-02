# Notes on this exercise

This exercise is based on calculating and plotting regression functions based on the method of least squares. 

The relevant formulae are:

$$s_{xx} = \frac{\Sigma x^2}{n} - \bar x^2$$

$$s_{xy} = \frac{\Sigma y^2}{n} - \bar y^2$$

$$s_{xy} = \frac{\Sigma xy}{n} - \bar x\bar y$$

or:

$$ S_{xx} = \Sigma x^2 - \frac{(\Sigma x)^2}{n} $$

$$ S_{yy} = \Sigma y^2 - \frac{(\Sigma y)^2}{n} $$

$$ S_{xy} = \Sigma xy - \frac{\Sigma x\Sigma y}{n} $$

For the regression function, the gradient is given by:

$$ b = \frac{s_{xy}}{s_{xx}}, \ \ or \ \ b = \frac{S_{xy}}{S_{xx}} $$

And, the y intercept is given by:

$$ a = \bar y - b\bar x $$
