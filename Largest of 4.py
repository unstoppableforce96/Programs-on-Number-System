# Largest of 4 numbers
'''Rule 1: At least one number will differ
   Rule 2: if there are more than one largest number
   print the first  one
   a = 1
   b = 2
   c = 2
   d = 1
   answer b is greater.'''
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if(a>b):
    e = a
else:
    e = b

if(c>d):
    f = c
else:
    f = d
if(e > d):
    print(e, 'is greater')
else:
    print(f, 'is greater')

    
