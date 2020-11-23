
from mpmath import *
import sys

def sn( x, m ):
  return ellipfun( 'sn', x, m )

def cn( x, m ):
  return ellipfun( 'cn', x, m )

def dn( x, m ):
  return ellipfun( 'dn', x, m )

function = sys.argv[1]

s = pre = post = ''

# sys.argv entries are all strings!
if len( sys.argv ) > 2:
  s = s.join( sys.argv[2:] )
  s = s.replace( 'j', 'i' )
  if len( sys.argv[2] ) > 2:
    pre = sys.argv[2].replace( '[', '' ).replace( ']', '' ) + ','
  if len( sys.argv ) == 4:
    post = ',' + sys.argv[3].replace( '[', '' ).replace( ']', '' )

file = open( 'functions.txt' )
d = dict( [line.split() for line in file] )

f = open( 'unit-circle/' + d[function] + s + '.txt', 'w' )

start = -1.5
step = 1 / float(33)

x = y = start

while x <= -start:
  while y <= -start:
    z = eval( '{}({}{:.9e}+{:.9e}j{})'.format( function, pre, x, y, post ) )
    f.write( '[{:.9e},{:.9e},{:.9e},{:.9e}]\n'.format( x, y, float(z.real), float(z.imag) ) )
    y += step
  x += step
  y = start

f.close()
