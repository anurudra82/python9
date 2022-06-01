##ternary operator.............................

# a=23
# b=44
# c=55

# x=6 if a>b else 3
# print(x)

# x=14 if a>b else 20 if b>c else 45
# print(x)

# a=int(input("enter the first number :"))
# b=int(input("enter the second number :"))
# min= a if a<b else b
# print('minimum value is : ',min)


a=int(input("enter the first number :"))
b=int(input("enter the second number :"))
c=int(input("enter the third number :"))


min= a if a<b and a<c else b if b<c else c
print('minimum value is : ',min)


max= a if a>b and a>c else b if b>c else c
print('maximum value is : ',max)