num = 1
num = int(raw_input())
n = 2
cond = 1
cond = num > n
flag = 0
cond2 = 0
while cond:
    cond2 = num % n
    cond2 = cond2 == 0
    if cond2:
        flag = 1 + 0
    n = n + 1
    cond = num > n
cond2 = flag == 0
if cond2:
    print "prime number"
else:
    print "Composite Number"
