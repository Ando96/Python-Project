# Arash's coursework template

# Ryan Anderson, ra111                               <--- so we know who you are
# F28PL Coursework 2, Python                         <--- sanity check


# You may assume variables, procedures, and functions defined in earlier questions
# in your answers to later questions, though you should add comments in code explaining
# this if any clarification might help read your code.


################################################################################
# Question 1   <--- Yes, so we know what question you think you're answering


"""
The complex numbers are explained here (and elsewhere):
 http://www.mathsisfun.com/algebra/complex-number-multiply.html
Represent a complex integer as a pair of integers, so (4,5) represents 4+5i (or 4+5j, depending on the complex numbers
notation you use).
1a. Using def, define functions cadd and cmult representing complex integer addition and
tymultiplication.
For instance,
 cadd((1,0),(0,1))
should compute
 (1,1j).
1b. Python has its own native implementation of complex numbers. Write translation functions
tocomplex and fromcomplex that map the pair (x1,y1) to the complex number x1+(y1)j and vice 
versa. You may use the python methods real and imag without comment, but not complex 
(use j directly instead).
"""
#  <--- always have the question under your nose

#####################################
# Question 1a


# adds two tuples together and returns a complex number, in complex number addition the real numbers 
# are added together and then the imaginary numbers are added together. So I can use c1[0] to retrieve 
# the first number in the first tuple and then c2[0] to get the first number of the second tuple and 
# do the same for the imaginary numbers, only after adding the imaginary numbers the result must be 
# multiplied by 1j to make the numbers complex so the result will be (n1 + n2j) instead of (n1 , n2)
def cadd(c1, c2):
    answer = c1[0] + c2[0] + ((c1[1] + c2[1]) * 1j) # Add both tuples and then make complex
    return answer # Return answer


# cmult uses the same logic as cadd and follows the rule for complex multiplication 
# (a+bi)(c+di) = (ac−bd) + (ad+bc)i
def cmult(c1,c2):
    answer = c1[0] * c2[0] - c2[0] * c2[1] + ((c2[0] * c1[1] + c1[0] * c2[1] *1j)) # Multiply tuples and 
    return answer # Return answer                                                  # make complex


#####################################
# Question 1b


# A complex number is 2 parts, a real number and an imaginary number
# x1 is assigned to real
# And y1 is assigned to imaginary, but in order to convert y1 to complex it first must be multiplied by 1j
# the unit for a imaginary number
def tocomplex(x1, y1):
    real = x1 # Assign x1 to real number
    imag = y1 * 1j # Assign y1 to imaginary number
    answer = real + imag # Combine both values to make complex number (x1 + y1j)
    return answer # Return answer


# As previously mentioned a complex number is made up of two values, real and imaginary,
# and so to convert from complex, built in python functions can be used to retrieve the real
# and imaginary parts of the complex number and assign them to variables which can then be combined into
# a tuple
def fromcomplex(c):
    first = c.real # Get the real number
    second = c.imag # Get the imaginary number
    answer = (first,second) # Create a tuple of the two numbers
    return answer # Return answer


# END ANSWER TO Question 1
################################################################################


################################################################################
# Question 2


"""
2a. Using def, write iterative functions seqaddi and seqmulti that implement pointwise
addition and multiplication of integer sequences.
For instance
 seqaddi([1,2,3],[-1,2,2])
should compute
 [0,4,5]
You need not write error-handling code to handle the cases that sequences have different
lengths.
2b. Do as for 2a, but make your functions recursive (like OCaml).
Call them seqaddr and seqmultr.
2c. Do it again. This time use list comprehensions instead of iteration or recursion.
"""

#####################################
# Question 2a


# seqaddi takes two lists (l1,l2) and iterativly adds them both together, the length of l1 is used to 
# create a counter and then for each position in the counter add the matching positions in the lists
# e.g counter = 0 would be
#  li[0] + l2[0] and so on until the counter has no values left
def seqaddi(l1, l2):
    counter = range(len(l1)) # Create counter from length of l1 (if l1 = 5 then counter = [1,2,3,4,5])
    answer = [l1[i] + l2[i] for i in counter] # Add both lists together iterativly
    return answer # Return answer


# seqmulti is the same as seqaddi, instead of adding each position they are instead multiplied
def seqmulti(l1, l2):
    counter = range(len(l1)) # Create counter from length of l1 (if l1 = 5 then counter = [1,2,3,4,5])
    answer = [l1[i] * l2[i] for i in counter] # Multiply both lists together iterativly
    return answer # Return answer


#####################################
# Question 2b


# Adds the two lists together recursivly, to do this first the heads of the lists are added together and 
# then the function is called again and passed the same two lists however the lists will only contain 
# values from [1] by using [1:] and onwards. So when the heads of the lists are added together again [1] 
# will now be [0] and this will continue until there are no values left.
def seqaddr(l1, l2):
    if len(l1) == 0: # Check to see if the length of l1 is 0
        return l2 # If l1 is empty return l2
    if len(l2) == 0: # Check to see if the length of l2 is 0
        return l1 # If l2 is empty return l1
    return [l1[0] + l2[0]] + seqaddr(l1[1:] , l2[1:]) # Add the head of the lists together, and then 
                                                      # recursivly call the function passing it the remainder   
                                                      # of lists l1 l2
   

# seqmultr uses the same logic as above, recursivly calling the function multiplying the two heads 
# of the lists while slicing the lists to remove the value already multiplied.
def seqmultr(l1, l2):
    if len(l1) == 0: # If the length of l1 is 0
        return l2 # Return l2
    if len(l2) == 0: # If the length of l2 is 0
        return l1 # Return l1
    return [l1[0] * l2[0]] + seqmultr(l1[1:] , l2[1:]) # Multiply the heads of the lists, then call the 
                                                       # function and pass it the remainder of the lists


#####################################
# Question 2c

# Adds x + y, x from l1 and y from l2, if the index of x in l1 matches the index of y in l2
def seqaddlc(l1,l2):
   answer = [x + y for x in l1 for y in l2 if l1.index(x) == l2.index(y)]
   return answer # Return the answer

# Uses the same logic as seqaddlc to multiply the two lists together
def seqmultlc(l1,l2):
    answer = [x * y for x in l1 for y in l2 if l1.index(x) == l2.index(y)]
    return answer # Return the answer


# END ANSWER TO Question 2
################################################################################

################################################################################
# Question 3

"""
Write functions
● ismatrix
This should input a list of list of integers (henceforth an intmatrix) and test whether a list
of lists of integers represents a matrix (so the length of each row should be equal).
● matrixshape
This should input an intmatrix and return the size of the matrix, which is the number of rows and the number of columns 
(traditionally the number of rows is given first, but if you have done it the other way around that’s fine; 
just make sure to clearly explain your code). 

● matrixadd
Matrix addition, which is simply pointwise addition.
● matrixmult
Similarly for matrix multiplication.
You do not need to write error-handling code, e.g. for the cases that inputs do not represent
matrices or represent matrixes of the wrong shapes; so for instance your matrixshape may 
assume that the argument has successfully passed the test ismatrix.
Your answer can use iteration, recursion, list comprehension, or anonymous functions. You
should not appeal to any libraries, e.g. for matrix processing.  Don't use zip.
"""

#Matrix is a list of lists , these are used for testing the matrix functions
A = [[1, 4, 5], # Valid matrix
    [-5, 8, 9]]

B = [[1, 4, 5], # Valid matrix
    [-5, 8, 9]]

C = [[1, 4], # Valid matrix
    [-5, 8],
     [3,4]]

D = [[]] # Empty matrix

E = [[1, 4, 5], # valid matrix
    [-5, 8, 9],
    [1 ,2, 3]]

notMatrix = [[1, 4],  #Invalid matrix
            [-5, 8, 9]]


#Check the length of each sublist in the matrix as the all have to be the same length to be a valid matrix
def ismatrix(m):
    if m == [[]]: # Checks to see if the matrix is empty and is a valid matrix
        return True # Return true
    for sublist in m: # If the matrix is not empty, seperate it into its sublists
        if len(sublist) == len(m[0]): # Check the length of the sublists against another sublist
            return True # Return true if they are the same length
        if len(sublist) != len(m[0]): # If the lengths do not match
            return False # Return false if they are not the same length


# matrixshape returns the number of Rows and Columns the matrix has, including if it is empty as it is 
# still a valid matrix
def matrixshape(m):
    if m == []: # If the matrix is empty return 
        return (0,1)
    elif m == [[]]:
        return (0,1)
    matrixRow = len(m) # Get the length of the matrix as it is the number of rows (3 sublists is 3 rows)
    matrixCol = len(m[0]) # Get the length of the first sublist
    print("Rows =",matrixRow) # Print number of rows
    print("Col =", matrixCol) # Print number of columns


# matrixadd uses the same logic as the lists addition, in m1 first the row is seprated from the matrix 
# and then a element is seperated from that row, which is then added to a value from a row in m2
# this process continues for the length of the row and for the length of the entire matrix.
def matrixadd(m1,m2):
    answer = [[m1[row][element] + m2[row][element] # Add the two elements together
    for element in range(len(m1[0]))] # For the length of the row
    for row in range(len(m1))] # For the length of the matrix
    return answer # Return answser


# Multiplies two matrices together
def matrixmult(m1,m2):
    answer = [] # Create a empty list to hold answer  
    rowLen = len(m2[0])*[0] # Generate empty rows the length of matrix 2
    answer.append(rowLen[:]) # Append the rows to the empty list
    for row in range(len(m1)): # For the length of row in matrix 1
        for col in range(len(m2[0])): # For the length of the column in matrix 2
            sum = 0 # To hold the sum of the matrix multiplication
            for element in range(len(m1[0])): # For each element  for the length of matrix 1
                sum += m1[row][element] * m2[element][col] # Multiply the element of row m1 to column element in m2
            answer[row][col] = sum # Make the answer to the sum of the multiplication
    return answer # Return answer


# END ANSWER TO Question 3
################################################################################


###############################################################################
# Question 4


"""
Write an essay on Python data representation. Be clear, to-the-point, and concise. Convince
your marker that you understand:

● Mutable vs immutable types. Give at least two examples of each, with explanation.

    Mutable types are 'values' that can be changed using methods. 

    Immutable types are 'values' that cannot be changed.

    An example of a mutable type would be lists:
    let l1 = [1,2,3,4,5]
    There are methods available that let you change the values within the list such as append,
    l1.append(6)
    and the result would now be [1,2,3,4,5,6]
    alternativly you can also use l1.remove(5) and the result would be [1,2,3,4,6]
    There are a number of other methods you can use to modify the data such as reverse and sort
    l1.reverse() would result in [6,4,3,2,1] and
    l1.sort() would result in [1,2,3,4,6]
    All of these methods modify the data

    """
def mutable():
    l1 = [1,2,3,4,5] # Create a list of numbers
    l1.append(6) # Add 6 to list
    print(l1) # Print the list
    l1.remove(5) # Remove 5 from the list
    print(l1) # Print the list
    l1.reverse() # Reverse the order of the list
    print(l1) # Print the list
    l1.sort() # Sort the list in ascending order
    print(l1) # Print the list

    """
    An example of a immutable type would be frozenset, similar to set however it does not have methods 
    to modify data stored within it, using the list from the mutable example,
    let newSet = frozenset(l) which creates a frozenset of the values stored in the list.
    Attempting to use methods that you would normally use with set will not modify the data.
    frozSet.add(5) would result in 'newset' object has no attribute 'add'
    If you were to attempt to do the same with set, the result would be [1,2,3,4,5,6]

    """
   
def immutable():
    l1 = [1,2,3,4,5] # Create a list of numbers
    frozSet = frozenset(l1) # Create a frozen set from the list of numbers
    frozSet.add(5) # Attempt to add 5 to frozen set, error is intended

def mutableSet():
    l1 = [1,2,3,4,5] # Create a list of numbers
    newSet = set(l1) # Create a set from the list
    newSet.add(6) # Add 6 to the set
    print(newSet) # Print the set


    """
● Integer vs float types.
    In python we can use both integers(int) and floating point numbers(float), the main difference between
    the two is the decimal point ( 1.123 ).
    num1 = 5 - which is an integer
    num2 = 3.2 - which is a float

    You can also check this within python itself using the type() function which will tell you the type 
    of the value you have given it. You can also 'convert' ints to floats and vice versa on demand which 
    is known as coercion, normally this is done automatically '5 + 3.2 = 8.2' but it is also possible
    to do it yourself using built in functions, float(5) = 5.0 and int(2.3) = 2.

    integers are infinite precision in Python and floats aren’t

    """
def intAndfloat():
    num1 = 5
    num2 = 3.2
    print(type(num1))
    print(type(num2))
    num3 = num1 + num2
    print(num3)
    print(type(num3))
    print(float(5))
    print(float(2.3))

    """
● Assignment = vs equality == vs identity is.

    Assignment is done by using '=' is storing a value within a variable, for example x = [], 
    which would assign an empty  list to the variable x, and printing x would output the empty list.

    """

def assignment():
    x = []
    y = 1
    print(x)
    print(y)

    """
    Equality is done by using '==' and is checking if one value is the same as another value, for example
    if x = 1 and y = 1 and then if you check if x == y the output would be 'true', it can also be used 
    in different situations such as lists, if x = [1] and if y = [] the result would be 'false' as
    these two variables are no longer equal, x contains a value within the list.


    """

def equality():
    x = 1 # Assign 1 to x 
    y = 1 # Assign 2 to y
    print(x == y) # Print x == y
    x = [1] # Change x to a list containing 1
    print (x == y) # Print the result

    """

    Identity, not to be confused with equality, relates to the id of an object, each object is given 
    a id during runtime in python and sometimes this id may be the same as another object.
    An example of identity would be if x = 1 and y = x, x is assigned value 1 and y points to x,
    these two variables will now have the same id as they both 'point' to the same location (or id).
    Running id(x) will return a series of numbers and running id(y) will return the same series of numbers.

    """

def identity():
    x = 1 # Assign 1 to x 
    y = x # Point y to x
    print(x is y) # Print result of x is y
    print(id(x)) # Print result of id of x
    print(id(y)) # Print result of id of y

    """

● The computational effects of a call to list on an element of range type, as in
list(range(5**5**5)).

Attempting to run this code is immposible as the number of values generated is too large and the
'OverflowError: Python int too large to convert to C ssize_t' error occurs 
But what the code is attempting to do is generate a computation for list of values 
within the range of 0 to 5 ^ 5 ^ 5.
Even attempting to run the code list(range(5**5)) returns a list with values [0 to 3124].


● Slices, with examples. Including an explanation of the difference in execution between
 list(range(10**10)[10:10]) and List triggers evaluation. fast
 list(range(10**10))[10:10] now evaluates first then slices slow

An example of a silce would be  list(range(10)[1:5])    , which will output [1, 2, 3, 4], this is because
range will generate a computation for a list of numbers 0 - 10 and then slice will evaluate the range to
numbers between 1 - 4.

The first execution list(range(10**10)[10:10]) will execute fast as the list will trigger evaluation,  
meaning 

The second execution list(range(10**10))[10:10] will execute incredibly slowly, this is because range 
will generate a computation of 10 to the power of 10 for a range of numbers 
first and then the slice will evaluate after the computation has happened.


Include short code-fragments where appropriate (as I do when lecturing) to illustrate your
observations.
"""


# END ANSWER TO Question 4
################################################################################


###############################################################################
# Question 5
print()
print('Question 5')

"""
Write a general encoding function encdat that will input an integer, float, complex number, or
string, and return it as a string.

So
• encdat(-5) should return '-5'
• encdat(5.0) should return '5.0'
• encdat(5+5j) should return '5+5j' (not '(5+5j)'; see hint below).
• encdat('5') should return '5'

"""

# Takes input and returns the same input as a String by using the method str
def encdat(dat):
    return str(dat).strip('()') # Return the input converted to string, strip is used to remove brackets
                                # from complex numbers

# END ANSWER TO Question 5
################################################################################


###############################################################################
# Question 6


"""
An encoding f of numbers in lists is as follows:
• f(0) = [] (0 maps to the empty list)
• f(n+1) = [f(n),[f(n)]] (n+1 maps to the list that contains f(n) and singleton f(n))
Implement encode and decode functions in Python, that map correctly between nonnegative
integers and this representation. Call them fenc and fdec.
"""


def fenc(i): 
    if i == 0: # If the input is equal to 0 
        return [] # Return an empty list
    else: # Otherwise if the input is not 0
        return [fenc(i - 1), [fenc(i - 1)]] # Return


def fdec(l):
    if l == []: # If the input list is empty
        return 0 # Return 0
    else: # Otherwise if the input list is not empty
        return fdec([l[0]]) + 1 # Return
        
# END ANSWER TO Question 6
################################################################################


###############################################################################
# Question 7


"""
Implement a generator cycleoflife such that if we assign
 x = cycleoflife()
then repeated calls to
 next(x)
return the values
 eat
 sleep
 code
 eat
 sleep
 code
 ...
in an endless cycle. If you can’t manage an endless cycle, do a program that runs for 1000
cycles then stops.
Note that this question is not asking you to program an endless loop that prints these values.
In effect, I am asking you to implement what is called a stream (infinite list)
 x = [eat, sleep, code, eat, sleep, code, ...].
This does not mean the whole infinite datastructure is in memory at any time (which is 
impossible for a machine with finite memory), but for any finite but unbounded number of calls 
to next your generator behaves as if it were the infinite datastructure illustrated above.
"""

# cycleoflife creates a infinite list of words, the first word in the list is appended onto the 
# end of the list and is then yielded, the for loop then moves onto the next word which is again added on
# to the end of the list and again yielded and so what you have is a cycle of words being added onto the end
# almost like a queue
def cycleoflife():
    list = ["Eat","Sleep","Code","Repeat"] # Create a list of Strings
    for word in list: # For every word stored within the list 
        list.append(word) # Add the first word in the list to end of the list
        yield word # And also yield that word


# END ANSWER TO Question 7
################################################################################


#################################################################################
# Question 8

"""
Call a *datum* something that is either an integer, or a list of data (datums).

Write a flatten function gendat that converts a datum to a list of integers.

So
- gendat(5) should return [5]
- gendat([])should return []
- gendat([5,[5,[]],[],[5]]) should return [5,5,5]

Do not use str.  You may find it useful to consider isinstance or the following code fragment
   type(5) == type([]) 
"""


def gendat(datum):
    answer = [] # Create an empty list to store the result
    if type(datum) == type(5): # If the type of the input is the same as the type of 5 (int and int)
        answer.append(datum) # Append the datum to the empty list 
        return answer # And return the result 
    elif len(datum) == 0: # If the length of the datum is 0 
        return [] # Return an empty list
    else: # If the datum makes it past the two if statements
        for sublist in range(len(datum)): # For each sublist contained within the datum
            if type(datum[sublist]) != type(5): # If the type of the sublist != int
                temp = datum[sublist] # Assign the sublist to a temp value
                for element in range(len(temp)): # For each element for the length of temp
                    if temp[element] != []: # If the element is not a empty list
                        answer.append(temp[element]) # Add that element to answer                               
            elif datum[sublist] != []: # Else if the sublist is not empty list   
                answer.append(datum[sublist]) # Add the sublist to answer
    return answer # Return the answer


# END ANSWER TO Question 8
################################################################################


##########################################################
# Question 9

"""
Implement the Sieve of Eratosthenes
 https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
as a Python generator eratosthenes such that if we assign
 x = eratosthenes()
then repeated calls to
 next(x)
return the primes, starting from 2.
"""

#Helper function to find prime numbers
def isPrime(n):
    if n <= 1: # Prime can't be less than 1
        return False # So return false always
    elif n == 2: # Check to see if n is 2 as it is the only even number that is prime also
        return True # Return true if it is
    elif n % 2 == 0: # If the number is divisable by 2 with 0 remainder then it cannot be a prime number
        return False # So return false
    counter = 3 # Set new value after starting after 2
    while counter <= (n**0.5): # While the counter is less than or equal to n to the power of 0.5
        if n % counter == 0: 
            return False
        counter = counter + 2 # Increment i in jumps of 2
    return True # Prime found


def eratosthenes():
    value = 1 # Set starting value
    while True: # While loop if true
        value =+ 1 # Increment value
        if isPrime(value): # Check to see if value is prime number
            yield value # If it is yield it


# END ANSWER TO Question 9
################################################################################