
while True:
    a = input('Num 1:')
    if not a.isdigit():
        print("You need to use numbers!")
        continue
    b = input('Num 2:')
    if not b.isdigit():
        print("You need to use numbers!")
        continue
    c = input('(+, -, *, /) Operator:')
    if c not in ["+", "-", "*", "/"]:
        print("You need to use +, -, *, or / !")
    else:
        print("Ok Calculating...")
        print(eval(a + c + b))
