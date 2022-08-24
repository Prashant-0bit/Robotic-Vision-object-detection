n1 = int(input("Enter Number 1: "))
n2 = int(input("Enter Number 2: "))
n3 = int(input("Enter Number 3: "))
n4 = int(input("Enter Number 4: "))

if (n1>n4):
    f1 = n1
else:
    f1 = n4

if (n2>n3):
    f2 = n2
else:
    f2 = n3

if (f1>f2):
    print(str(f1) + " is greaterst")
else:
    print(str(f2) + " is greaterst")