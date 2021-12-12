noun = "wow.i"
if not any(value in noun for value in ("+", ".","/","-","$")):
    print(len(noun))
else:
    print("haha")

print(len(noun))