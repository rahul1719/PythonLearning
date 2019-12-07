inp_str = (input("Enter an integer"))
if type(inp_str) == int and inp_str % 2 == 0:
    print("Even number")
elif type(inp_str) == int and inp_str % 2 != 0:
    print("Odd number")
else:
    print("Not a number")
