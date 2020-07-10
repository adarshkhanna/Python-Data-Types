#Fundamental Data Types
print('int + int: ', type(2 + 4))  # int + int = int
print('int - int: ', type(2 - 4))  # int - int = int
print('int * int: ', type(2 * 4))  # int * int = int
print('int / int: ', type(2 / 4))  # int / int = float
print('number with decimal: ', type(5.00001)) 
print('add number with decimal: ', type(9.9+1.1)) 
print('power of: ', 2 ** 2)  # to the power of

"""
  floor division follows below formula:
      n = d * (n // d) + (n % d)
  For +ve numbers, it is floor(n/d) 
  For -ve numbers, it follows formula    
"""
print('floor division(13 // 4): ', 13 // 4)  # for +ver #'s - returns an integer rounded down
print('remainder(13 % 4): ', 13 % 4)   # modulo operator - returns remainder

print('floor division(-13 // 4): ', -13 // 4)  # for +ver #'s - returns an integer rounded down
print('remainder(-13 % 4): ', -13 % 4)   # modulo operator - returns remainder

"""
  floor & truncate are not the same for -ve numbers
"""
from math import floor
from math import trunc
print('floor division(floor(6/4)): ', floor(6/4))
print('floor division(floor(-6/4)): ', floor(-6/4))

print('trunc(floor(6/4)): ', trunc(6/4))
print('trunc(floor(-6/4)): ', trunc(-6/4))



# math functions
print(round(3.1))
print(round(3.9))

print(abs(-2.1))

# How large an integer can be ??

"""
Some languages (Java, C...) provide multiple distinct data types that use a fixed number of bits and some languages also provide unsigned data types
Example : Java 
    byte  = signed - 8 bit 
    short = signed - 16 bit 
    int   = signed - 32 bit 
    long  = signed - 64 bit 
"""

"""
Python does not work that way !!
  * int objects use variable number of bits 
  * since int is an object, it has a fixed memory overhead
  * large integers will use more memory and operations will be slower (as it requires multiple operations to load data & perform arithmetic)
"""
import sys

# Everything is an object 
# Let's find how much memory overhead an integer object has  

print('Overhead of int(0) object: ', sys.getsizeof(0))  # 24 bytes = overhead of integer object

print('Overhead of int(1) object: ', sys.getsizeof(1))  # 28 - 24 = 4 additional bytes to store 1

print('Overhead of int (2**1000) object: ', sys.getsizeof(2**1000))  # 160 - 24 = 158 additional bytes to store 2**1000

from fractions import Fraction
from decimal import Decimal

"""
  Four main types of numbers
    Z = Integer numbers (0, +/-1, +/-2..) = int
    Q = Rational numbers (p/q where p,q belong to Z and q<>0) = Fraction
    R = Real numbers (0, -1, 0.125, 1/3...) = float, decimal
    C = Complex numbers (a + bi) = complex

  z -subset- Q -subset- R -subset- C

  Boolean : 0 = False, 1 = True
"""

"""
  Fraction is more accurate but takes more memory
"""
print('Fraction: ', Fraction(2,3))
print('Decimal: ', Decimal(2/3))

"""
  Float's inernal representation is approximate (sign, exponent, significant digit)
  1.2345, 12345000000, 0.00012345, 12345e-50 -> 5 significant digits 
"""
a = 0.1 + 0.1 + 0.1
b = 0.3
print('0.1 + 0.1 + 0.1 = ', format(a, '.25f'))
print('0.3 = ',format(b, '.25f'))
print('is a == b ? ', a == b)