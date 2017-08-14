counter = 0
largest_odd_number = 0
input_numbers = [None, None, None]
while counter <= 2:
    x = input("Enter a number: ")
    # line= sys.stdin
    if type(int(x)) == int:
        input_numbers[counter] = x
        counter += 1
        for numb in input_numbers:
            # print(type(numb))
            if isinstance(numb, str) and int(numb) % 2 != 0:
                # print(numb)
                if (int(largest_odd_number) < int(numb)):
                    largest_odd_number = numb

print("Largets odd number is " + largest_odd_number)
