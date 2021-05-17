
# Regular expression
import re
pattern = "Colour"
if re.match(pattern, "Colour is a colour, I love red colour"):
    print("Match")
else:
    print("Not Matched")

if re.search(pattern, "Colour is a colour, I love red colour"):
    print("Match")
else:
    print("Not Matched")

print(re.findall(pattern, "Red is a Colour, I love red Colourful"))

print("===================Another example=============")
pattern = r"colour"
text = "My favourite colour is Red"
match = re.search(pattern,text)
if match:
    print(match.start())
    print(match.end())
    print(match.span())

# Search And Replace
pattern = r"colour"
text1 = "My favourite colour is Red. I love Red colour as well"
text2 = re.sub(pattern,"color",text1)
pattern = r"Red"
text3 = re.sub(pattern,"Blue",text1,count=1)

print(text2)
print(text3)