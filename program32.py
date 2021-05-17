
# Exception
try:
     list = [20,0,30]
     result = list[0] / list[3]
     print(result)
     print("Done")
except ZeroDivisionError:
    print("Dividing by zero is not possible")
except IndexError:
    print("Index error")
finally:
    print("This section must work.")
print("Successful.")

# Another example
print("=================Another example=================")
try:
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))
    result = num1/num2
    print(result)
except (ValueError,ZeroDivisionError):
    print("You have entered incorrect input. ")
finally:
    print("Thanks.")


# raise keyword
def voter (age):
    if age < 18:
        raise ValueError("Invalid Voter")
    return "You are allowed to vote"
try:
    print(voter(19))
    print(voter(17))

except ValueError as e:
    print(e)



