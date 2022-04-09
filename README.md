# Math Test Data
 
Data generated by [mpmath](http://mpmath.org) for testing the accuracy of Math

### Usage ###

For a function without additional parameters, data on the complex plane is generated with

```
python plane.py function
```

The default domain is [-49.5,49.5] in unit steps in both directions. The function name is that of mpmath, while the resulting file name corresponds to the name in Math.

For a function with additional parameters before the main argument, include a list with comma-separated values. Examples are

```
python plane.py besselj [0]
python plane.py hyp2f1 [.5,.3]
```

For a function with additional parameters after the main argument, include an empty list before the list of comma-separated values. For example

```
python plane.py ellipf [] [.5]
python plane.py sn [] [.5]
```

For a function with additional parameters both before and after the main argument, include two comma-separated lists. For example

```
python plane.py ellippi [1] [.5]
```

The imaginary unit is "j" in Python. The resulting file name will contain an "i" in its place for legibility.

Data on the complex unit circle and the complex axes are generated similarly using the Python files `circle.py` and `axes.py` and following the same conventions for additional parameters. The complex unit circle data has the domain [-1.5,1.5] in both directions and the complex axes [-49.5,49.5] in both directions.

### Visualizations ###

[Complex Plane Viewer](https://paulmasson.github.io/math-test-data/complex-plane-viewer.html)
