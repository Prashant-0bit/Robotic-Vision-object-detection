sub1 = int(input("Enter Subject Marks 1: "))
sub2 = int(input("Enter Subject Marks 2: "))
sub3 = int(input("Enter Subject Marks 3: "))

if (sub1<33 or sub2<33 or sub3<33):
    print("You are failed due to less amount of marks")
elif(sub1+sub2+sub3)/3 <40:
    print("You are failed due to less percentage")
else:
    print("congratulations! You passed")