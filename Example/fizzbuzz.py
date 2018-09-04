i = 1
s = 1
temp = 1
cond1 = 1
cond2 = 1
cond3 = 1
s = 101 > i
while s:
    temp = i % 3
    cond1 = temp == 0
    temp = i % 5
    cond2 = temp == 0
    cond3 = cond1 and cond2
    if cond3:
        print "FizzBuzz"
    else:
        if cond1:
            print "Fizz"
        else:
            if cond2:
                print "Buzz"
            else:
                print i
    i = i + 1
    s = 101 > i
