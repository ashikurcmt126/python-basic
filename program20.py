
num1 = {1,2,3,4,5}
num2 = set([4,5,6])

num2.add(7)
num2.remove(7)

print(7 in num2)

print(num1 | num2)
print(num1 & num2)
print(num1 - num2)
print(num2 - num1)