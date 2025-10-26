# Q1)
name = "Aryan"
print(f"Good Afternoon {name}") 

# Q2)
letter = '''Dear <Name>, 
You are Selected !
<Date>'''

print(letter.replace("<Name>", "Aryan").replace("<Date>", "24th sept"))

# Q3)
sent = "ahj dfks  fjas ads  asijjd"
print(sent.find("  ")) # prints the index at which doulble space is
print(sent.replace("  ", " "))