
n = input("Enter the text of number: ")
# 10 20 30 40 50
list = n.split() # 10, 20, 30, 40, 50

sum = 0
for x in list:
    sum+=int(x)

print(sum)
