sub1=int(input("Tamil:"))
sub2=int(input("English:"))
sub3=int(input("Maths:"))
sub4=int(input("Science:"))
sub5=int(input("Social:"))
Total=sub1+sub2+sub3+sub4+sub5
avg=Total/5
if(avg<35):
    print("Additional class is required")
else:
    print("You are good to go")

