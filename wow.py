noun = "wow.i"
if not any(value in noun for value in ("+", ".","/","-","$")):
    print(noun)
else:
    print("wtf")