a=int(input("a="))
b=int(input("b="))
operation=input("add/sub/mul/divi:")
if(operation=="add"):
    print(a+b)
elif(operation=="sub"):
    print(a-b)
elif(operation=="mul"):
    print(a*b)
elif(operation=="divi"):
    print(a/b)
else:
    print("Invalid operation")
