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

"""
  String immutability
"""
s = 'abcde'
print('string slice [0]', s[0])
# s[0]='z'

print('len of string: ',len(s))

print('upper: ', s.upper(),
      '\ncapitalize: ',s.capitalize(),
      '\nfind: ', s.find('bc'),
      '\nreplace: ',s.replace('bc','zz'),
      '\nrepeat X 2: ',s*2,
      '\noriginal: ',s,)

"""
  Lists - can contain heterogenous data types
"""
li = [1,2,3]
print('li: ',li)

li2=['a','b','c']
print('li2: ',li2)

li3=[1,2,'a',True]
print('li3: ',li3)

# list is mutable
li[0]=10
print('li mutated: ',li)

# Matrix
matrix = [
  [1,0,1],
  [0,1,0],
  [1,0,1]
]

print('matrix: ', matrix)

print('matrix 1st row: ', matrix[0],
'\nmatrix 1st row, 1st element: ',matrix[0][0])

#What is the output of this code?
#Before you clikc RUN, guess the output of each print statement!
new_list = ['a', 'b', 'c']
print(new_list[1])
print(new_list[-2])
print(new_list[1:3])
new_list[0] = 'z'
print(new_list)

my_list = [1,2,3]
bonus = my_list + [5]
my_list[0] = 'z'
print(my_list)
print(bonus)

# append elemets to a list
basket = [1,2,3,4,5]
print('basket before append: ', basket)
basket.append(6)
print('basket after append: ',basket)

basket.insert(5,100)
print('basket after insert: ',basket)

basket.extend([120]) # extend takes an iterable
print('basket after extend: ',basket)

# removing
basket.pop()  # removes from end of list
print('basket after pop: ',basket)

basket.pop(0) # remove from index=0
print('basket after pop at index 0: ',basket)

basket.remove(4) # remove the value 4
print('basket after remove: ',basket)

basket.clear() # removes all items from list
print('basket after clear: ',basket)

# using this list, 
basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# 1. Remove the Banana from the list

# 2. Remove "Blueberries" from the list.

# 3. Put "Kiwi" at the end of the list.

# 4. Add "Apples" at the beginning of the list

# 5. Count how many apples in the basket

# 6. empty the basket

print(basket)

basket = ['x','y','a','b','c','d','e']
# print(basket.index('d',0,3))

# to avoid error 
print('d' in basket)
print(basket.count('d')) # number of times 'd' occurs 
basket.sort()
print(basket)

print(sorted(basket)) # returns a new sorted array, does not change basket

basket.reverse()  # reverse the list
print(basket)

### generate list quickly
print(range(1,100))
print(list(range(101)))

### join list
sentence = '!'
new_sentence = sentence.join(['hi','my','name','is','Adarsh']
)
print(new_sentence)

new_sentence = ' '.join(['hi','my','name','is','Adarsh']
)
print(new_sentence)

### list unpacking
a,b,c,*d = [1,2,3,4,5,6]
print(a,b,c,d)


#fix this code so that it prints a sorted list of all of our friends (alphabetical). Scroll to see answer
friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']

# new_friend = ['Stanley']
# a = friends.sort() + new_friend
# print(friends.sort() + new_friend)

"""
  Dictionaries (unordered key-value pair - not next to each other like in list)

  key = has to be immutable & unique
"""
dictionary = {
  'a':1,
  'b':2,
  'b':4
}

print('dictionary element: ', dictionary['b'])

my_list = [{
  'a': [1,2,3],
  'b': 'hello',
  'x': True
}]
print('list of dict: ', my_list[0]['a'])

"""
  List : use it when you want order 
  Dict : stores more info (key-value)
  tuple : immutable list
  set : unordered collection of unique objects
"""

my_tuple = (1,2,3,4,5)  # just like list but immutable
my_tuple = (1,2,3,4,5,5) # can have duplicates

#1 Create a user profile for your new game. This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'

#2 iterate and print all the keys in the above user.

#3 Add a new weapon to your user

#4 Add a new key to include 'is_banned'. Set it to false

#5 Ban the user by setting the previous key to True

#6 create a new user2 my copying the previous user and update the age value and username value. 

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

print('set difference: ', my_set.difference(your_set))

# You are working for the school Principal. We have a database of school students:
school = {'Bobby','Tammy','Jammy','Sally','Danny'}

#during class, the teachers take attendance and compile it into a list. 
attendance_list = ['Jammy', 'Bobby', 'Danny', 'Sally']
