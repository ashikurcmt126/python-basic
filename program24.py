
# Returning Value from function

def large(a,b):
    if a>b:
        return a
    else:
        return b

maximum = large(10,20)
print(maximum)

maximum1 = large
print(maximum1(20,15))
