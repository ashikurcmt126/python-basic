
# xargs
def student(*details):
    print(details)
    print(details[0])

student(101,"Ashikur Rahman Rashid",1.1)
student("ashikur")

def sum(*number):
    sum=0
    for x in number:
        sum+=x
    print(sum)

sum(10,20,30)

#xxargs
def student(** details):
    print(details)
    print(details["id"])

student(id="101",name="Ashikur Rahman Rashid")