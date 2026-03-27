#5.  calculate percentage of a student through 5 subjects.

a=int(input("Enter the mark for tamil:"))
b=int(input("Enter the mark for english:"))
c=int(input("Enter the mark for maths:"))
d=int(input("Enter the mark for chemistry:"))
e=int(input("Enter the mark for physics:"))
f=int(input("Enter the mark for bio :"))
submark= a+b+c+d+e+f
totalmark= 600
percentage=(submark/totalmark)*100

if percentage >= 90:
    print("Excellent")
elif percentage > 80:
    print("Very good")
elif percentage > 70:
    print("Good")
elif percentage > 60:
    print("Average")
elif percentage > 50:
    print("Bad")
else:
    print("Fail")
