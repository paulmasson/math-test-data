
from mpmath import *
import sys

function = sys.argv[1]

file = open( 'functions.txt' )
d = dict( [line.split() for line in file] )

f = open( 'data/' + d[function] + '.txt', 'w' )

start = -49.5
step = 1

x = y = start

while x <= -start:
  while y <= -start:
    z = eval( '{}({}+{}j)'.format( function, x, y ) )
    f.write( '[{},{},{:.9e},{:.9e}]\n'.format( x, y, float(z.real), float(z.imag) ) )
    y += step
  x += step
  y = start

f.close()
