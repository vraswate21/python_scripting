a= float(input(" enter a number "))
b = float(input(" enter a number "))
op = input("choose option(-, +, *, /)")

if op == "+":
    print("result", a+b)
elif op == "-":
    print("result", a-b)
elif op == "*":
    print("result", a*b)
elif op == "/":
    print("result", a/b)
else:
    print("invalid input")