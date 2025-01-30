salary=int(input("Enter your salary:"))
age= int(input("Enter your age:"))
if(salary>=20000 or age<=25):
    Loan=int(input("Enter your loan amount:"))
    if(Loan<=50000):
        print("You are eligible for loan")
    else:
        print("Maximum loan amount is 50000")    
else:
    print("You are not eligible for loan")
