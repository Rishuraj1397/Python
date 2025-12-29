a = 4
b = 4
print(a is b)     # True, because both refer to the same integer object in memory
print(a == b)     # True, because the values are equal
c = a ** 2
d = a * b
e = c + d
print( "the value of sum is: " ,e ) 

f = 8 * 4
print (e is f)
print (e == f)