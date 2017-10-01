def isPalindrome(str):
    str = str.lower ()
    counter = 0
    isPal = False
    for c in str:
        if c == str[ -1 - counter ]:
            isPal = True
        else:
            isPal = False
        counter += 1
    print ("This is a palindrom {} ".format (isPal))


isPalindrome (input ("Enter string: "))
