fib_length = input("enter the lenght of the fibonacci series : ")
x = 0
y = 1
counter = 2
if int(fib_length) <= 2 and int(fib_length) == 1:
    print("the fibo series is : %d  " % x)
elif int(fib_length) <= 2 and int(fib_length) == 2:
    print("the fibo series is : %d  " % y)
elif int(fib_length) > 2:
    while counter <= int(fib_length):
        next_num = x + y
        x = y
        y = next_num
        counter += 1
    print("the fibonaci series is : %d " % next_num)
else:
    print("Enter number greater than 0")
