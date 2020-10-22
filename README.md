# Math Test Data
 
Data generated by [mpmath](http://mpmath.org) for testing the accuracy of Math

### Usage ###

For a function without additional parameters, data on the complex plane is generated with

```
python complex.py function
```

The default domain is [-49.5,49.5] in unit steps in both directions. The function name is that of mpmath, while the resulting file name corresponds to the name in Math.

For a function with additional parameters before the main argument, include a list with comma-separated values. Examples are

```
python complex.py besselj [0]
python complex.py hyp2f1 [.5,.3]
```

For a function with additional parameters after the main argument, include an empty list before the list of comma-separated values. For example

```
python complex.py ellipf [] [.5]
python complex.py sn [] [.5]
```

For a function with additional parameters both before and after the main argument, include two comma-separated lists. For example

```
python complex.py ellippi [1] [.5]
```

The imaginary unit is "j" in Python. The resulting file name will contain an "i" in its place for legibility.

### Visualizations ###

[Complex Plane Viewer](https://paulmasson.github.io/math-test-data/complex-plane-viewer.html)
