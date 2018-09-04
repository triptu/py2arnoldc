a = 1
a = int(raw_input())
a = a + 1
ans = 1
curr = 1
cond = 1
cond = a > curr
while cond:
    ans = ans * curr
    curr = curr + 1
    cond = a > curr
print ans
