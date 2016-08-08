fizz_buzz_set = range (1,100)
for n in fizz_buzz_set:
    if (n % 3 )==0 and ( n % 5)==0:
        print("fizzbuzz")
    elif n % 3 == 0:
        print "fizz"
    elif n % 5 ==0:
        print ("buzz")
    else:
        print(n)