
# map function()
def square(x):
    return x*x

num = [10,20,30,40]
a = list(map(square,num))

print(a)

# filter()
num = [1,2,3,4,5]

result = list(filter(lambda x:x%2==0,num))
print(result)