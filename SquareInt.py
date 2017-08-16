number = input("Enter the integer :")
if int(number) > 0:
    iteration = int(number)
    ans = 0
    while iteration != 0:
        ans = ans + int(number)
        iteration = iteration - 1
    print("Square of %s is %s :" % (number, ans))
