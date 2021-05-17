
subjects = ["C","C++","Android","OS","TOS","JAVA","C++"]

print(subjects)
print(subjects[0])
print(subjects[2:])
print(subjects[-1],subjects[-2])

print("C++" in subjects)
print("C-" not in subjects)

print(subjects+ ["Python"])
print(subjects)

print(subjects*3)

print(len(subjects))

subjects.append("Swift")
print(subjects)

subjects.insert(1,"Machine learning")
print(subjects)

subjects.remove("Swift")
print(subjects)

subjects.sort()
print(subjects)

subjects.reverse()
print(subjects)

subjects.pop()
subjects.pop()
print(subjects)

#subjects.clear()
#print(subjects)

pos = subjects.index("C++")
print(pos)

subjects2 = subjects.copy()
print(subjects2)

count = subjects.count("C++")
print(count)