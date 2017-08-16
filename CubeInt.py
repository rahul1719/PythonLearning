number = input("Enter the integer :")
if int(number) > 0:
    iterationSquare = int(number)
    iterationCube = iterationSquare
    ans = 0

    while iterationSquare != 0:
        ans = ans + int(number)
        iterationSquare = iterationSquare - 1
    cubeAns = ans
    while iterationCube != 1:
        ans = ans + int(cubeAns)
        iterationCube = iterationCube - 1
    print("Cube of %s is %s :" % (number, ans))
