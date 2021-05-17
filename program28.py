


num = [1,2,3,4,5]

result = list(map(lambda x: x*x, num))
print(result)

# comprehensive_list
num = [1,2,3,4,5]
result = [x*x for x in num]
print(result)

# comprehensive_list use instead of filter lambda()
num = [1,2,3,4,5]
#result = list(filter(lambda x: x%2==0,num))
result = [x for x in num if x%2==0]
print(result)