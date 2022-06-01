
# x=eval("10+20+30+40")
# print(x)

#......................................................................................................................................................................

# x=eval(input("enter the expression :"))

# print(x)

#......................................................................................................................................................................

# x=eval(input("enter the list :"))
# print(type(x))
# print(x)

# x=eval(input("enter the tuple :"))
# print(type(x))
# print(x)

# x=eval(input("enter the boolean :"))
# print(type(x))
# print(x)


a,b,c,d=[eval(x) for x in input("enter 4 number:").split(',')]
print(type(a))
print(type(b))
print(type(c))
print(type(d))

print(a)
print(b)
print(c)
print(d)


