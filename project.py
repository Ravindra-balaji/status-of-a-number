Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
... a=int(input("enter starting number of range: "))
... b=int(input("enter ending number of range: "))
... number=random.randrange(a,b,1)
... print("Randomly picked number is ",number)
... if number%2==0:
...     print(number,"is a even number")
... else:
...     print(number,"is a odd number")
... if number>0:
...      print(number,"is a positive number")
... else:
...     print(number,"is a negative number")
... if number==1:
...     print(number,"is a neither prime nor composite")
... elif number==2:
...     print(number,"is a prime number")
... else:
...     factorcount=0
...     for j in range(1,number+1):
...         if number%j==0:
...             factorcount=factorcount+1
...     if factorcount>2:
...         print(number,"is a composite number")
...     else:
