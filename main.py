#Fundamental Data Types
"""
  Numbers (immutable)
    Integral
      Integers (int)
      Boolean (bool)
    Non-Integral
      Float (float) - implemented as C double
      Complex (complex)
      Decimal (decimal.Decimal) 
      Fractions (fractions.Fraction)
  
  Collections
    Sequences
      Lists (list)   - mutable
      Tuples (tuple) - immutable
      Strings (str)  - immutable
    
    Sets (implemented as hashmap)
      Sets (set) - mutable
      Frozensets (frozenset) - immutable
    
    Mappings (implemented as hashmap)
      Dictionaries (dict) - mutable
  
  Singletons
    None
    NotImplemented
    Ellipsis (...) operator
"""
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
print('round(3.1): ', round(3.1))
print('round(3.9): ', round(3.9))

print('abs(-2.1): ',abs(-2.1))

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

"""
  define function
"""
def hello_world():
  print('Hello World!')

"""
  call a  function
"""
hello_world()

"""
  Function parameters : 
     positional args - order in which it is passed
     keyword / named args - use parm name when passing value
"""
## if a positional parm is defined with default value, all sunsequent params must have default value 
def my_func(a,b=10, c=5):
  pass

my_func(10,20)
my_func(5)

## if using named arg, all subsequent args must also be named args
my_func(a=1, c=2)  # a=1, b=10, c=2
my_func(1, c=2) # a=1, b=10,c=2

"""
  Passing variable amount of position args 
  The recieving parm *c will be a tuple
  Cannot add positional arg after *c, but can add keyword/named arg
"""
def my_func(a,b,*c,d):
  print('multiple arg as one :',a,b,c,d)

my_func(10,20,'a','b',d=10)

"""
  make positional args optional
"""
def my_func(*args,d):
  print('optional positional args: ',args,d)

my_func(1,2,d=10)
my_func(d=2)

"""
  make a function with no positional args
"""

def my_func(*,d):
  print('no position args: ',d)

my_func(d=10)

# 1 What would be the output of the below 4 print statements? 
#Try to answer these before you click RUN!

print("Hello {}, your balance is {}.".format("Cindy", 50))

print("Hello {0}, your balance is {1}.".format("Cindy", 50))

print("Hello {name}, your balance is {amount}.".format(name="Cindy", amount=50))

print("Hello {0}, your balance is {amount}.".format("Cindy", amount=50))

# 2 How would you write this using f-string? 
name = 'Cindy'
amount = 50
print(f"Hello {name}, your balance is {amount}.")

#Guess the output of each print statement before you click RUN!
# [start:stop:stepover]
python = 'I am PYHTON'
print('string = ', python)
print('[1:4] = ',python[1:4])
print('[1:] = ', python[1:])
print('[:] = ', python[:])
print('[1:100] = ', python[1:100])
print('[-1] = ', python[-1])   # -ve index start at end
print('[-4] = ', python[-4])
print('[:-3] = ', python[:-3])
print('[-3:] = ', python[-3:])
print('[::-1] = ', python[::-1])
