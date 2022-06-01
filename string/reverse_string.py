# s=input("enter the string!! :")
# n=len(s)
# i=0

# print("forward direction!!!")
# while i<n:
#     print(s[i],end=' ')
#     i=i+1

# print()

# print('backward direction!!!')
# i=n-1
# while i>=0:
#     print(s[i],end=' ')
#     i=i-1


s=input("enter something :")
print('Forward direction!!')
n=len(s)

for i in s:
    print(i,end=' ')

print()
print('Backward direction!!')

for i in s[::-1]:
    print(i,end=' ')

