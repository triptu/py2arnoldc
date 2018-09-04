'''Converts a given python program written strictly using pep8 guidelines into an arnoldc file.
Not all python statements are possible. Restrictions on py file:-
* A line can be variable declaration/assignment, if ..., while ..., or comment. Nothing else.
* Every varaible mus be declared before its use of any kind. You have to write a = 1 before a = b + c.
* Varaibles used in loop must be declared before.
* Arithmetic/logical operations follow  'result = op1 operation op2' eg. 'c = a + 2',  'd = p or q'
* Only binary arithmetic/logical operations allowed. Which means 'a = (2 + b)*3' will be written as
  a = 2 + b
  a = a * 3
* Operations available - [+, -, *, /, %, ==, >, or, and]
* For using if or while the only supported format is 'if cond:' or 'while cond:'. You have to evaluate cond
  elsewhere.
* You can comment using '#' which will be omitted in arnoldc file. No inline comments allowed.
* Method declaration not supported.
* For putting variable a in b i.e 'b = a' write 'b = a + 0'
* for variable declared before(eg. flag) instead of 'flag = 1', write 'flag = 1 + 0'
* arnoldc supports only integers so don't use variables containing string.
'''


inpfile = 'ques5.py'
outfile = 'ques5.arnoldc'
out = open(outfile, 'w')

inp = open(inpfile)

out.write("IT'S SHOWTIME\n")

ops = {
    '+': 'GET UP',
    '-': 'GET DOWN',
    '*': "YOU'RE FIRED",
    '/': "HE HAD TO SPLIT",
    '==': 'YOU ARE NOT YOU YOU ARE ME',
    '>': 'LET OFF SOME STEAM BENNET',
    'or': 'CONSIDER THAT A DIVORCE',
    'and': 'KNOCK KNOCK',
    '%': 'I LET HIM GO'
}

lines = []
for line in inp:
    lines.append(line)

prevlevel = 0
level = 0
ifwhile = [0]
linenum = 1
for line in lines:
    line = line.rstrip()
    new = line.strip()
    spaces = len(line) - len(new)
    level = spaces / 4

    if prevlevel > level:
        while prevlevel > level:
            temp2 = ifwhile.pop()
            if temp2 == 'else':
                out.write('YOU HAVE NO RESPECT FOR LOGIC\n')
            elif temp2 == 'while':
                out.write('CHILL\n')
            elif temp2 == 'if' and (new.split()[0] != 'else:' or (prevlevel - level) > 1):
                out.write('YOU HAVE NO RESPECT FOR LOGIC\n')
            prevlevel -= 1

    if new == '' or new[0] == '#':
        continue

    if new[:5] == 'print':
        out.write('TALK TO THE HAND ')
        out.write(new[6:])
        out.write('\n')
    elif len(new.split()) >= 2 and new.split()[1] == '=':
        pars = new.split()
        if new.split()[2][:3] == 'int':
            pars = new.split()
            out.write('GET YOUR ASS TO MARS ' + pars[0] + '\n')
            out.write('DO IT NOW\n')
            out.write('I WANT TO ASK YOU A BUNCH OF QUESTIONS AND I WANT TO HAVE THEM ANSWERED IMMEDIATELY\n')
        elif len(pars) == 3:
            out.write('HEY CHRISTMAS TREE ' + pars[0] + '\n')
            out.write('YOU SET US UP ' + pars[2] + '\n')
        else:
            out.write('GET TO THE CHOPPER ' + pars[0] + '\n')
            out.write('HERE IS MY INVITATION ' + pars[2] + '\n')
            out.write(ops[pars[3]] + ' ' + pars[4] + '\n')
            out.write('ENOUGH TALK\n')
    elif new.split()[0] == 'if':
        ifwhile.append('if')
        pars = new.split()
        pars[1] = pars[1][:-1]
        out.write("BECAUSE I'M GOING TO SAY PLEASE " + pars[1] + '\n')
    elif new.split()[0] == 'else:':
        ifwhile.append('else')
        pars = new.split()
        out.write('BULLSHIT\n')
    elif new.split()[0] == 'while':
        ifwhile.append('while')
        pars = new.split()
        pars[1] = pars[1][:-1]
        out.write('STICK AROUND ' + pars[1] + '\n')
    else:
        print "Line number ", linenum, "--> '", line, "' can't be resolved."

    prevlevel = level
    linenum += 1

level = 0
if prevlevel > level:
    while prevlevel > level:
        temp2 = ifwhile.pop()
        if temp2 == 'else':
            out.write('YOU HAVE NO RESPECT FOR LOGIC\n')
        elif temp2 == 'while':
            out.write('CHILL\n')
        elif temp2 == 'if' and (new.split()[0] != 'else:' or prevlevel != level):
            out.write('YOU HAVE NO RESPECT FOR LOGIC\n')
        prevlevel -= 1


out.write("YOU HAVE BEEN TERMINATED")
out.close()
inp.close()

# Output
with open(outfile) as handle:
    for line in handle:
        print line,
