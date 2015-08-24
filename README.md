# Computing Pi

An algorithm for computing Pi was originally added to Apache Hadoop as an example of a job that exercised the computational resources of the cluster but not the storage. It has since also become a common example on Apache Spark as a good demonstration of the Monte Carlo method. However the Monte Carlo method is not deterministic: it can give you a different answer every time. This implementation is deterministic and is more appropriate if your goal is to actually compute Pi, or if you suffer from OCD. It is intended to be pasted into the PySpark shell (adjust the values of split\_count and split\_size as desired):

    $ pyspark

## The Monte Carlo Method

See: https://en.wikipedia.org/wiki/Monte_Carlo_method

The Monte Carlo method for computing Pi is to generate many random coordinate pairs (x, y) inside a 1 x 1 grid. Each set of coordinate can be classified is being inside or outside of the upper-right quadrant of a unit circle (circle centered at the origin with radius 1) by using the Pythagorean theorem: x^2 + y^2 <= 1 is true for all points inside the circle. With enough coordinate pairs, you can approximate the ratio of the area inside the quarter circle (pi x 1^2 x 1/4) to the area inside the square (1 x 1). From that, you can solve for Pi. The code for the Monte Carlo method is very simple, but it is not deterministic.

## The Leibniz Formula

See: https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80

The Leibniz formula is an infinite series that converges to Pi. It alternates between adding and subtracting fractions with 4 in the numerator, and increasing positive odd integers in the denominator, starting at 1.

    Pi = 4 x (1/1 - 1/3 + 1/5 - 1/9 ...)

In this implementation, we group the first (i.e. most significant) terms of the series into subsets, compute the sum of each subset in parallel, add these intermediate sums together, and multiply by 4.

