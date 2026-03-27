#2.check if a single character is a vowel or not.

char=input()
if char.lower() in "aeiou":
  print("It is a vowel")
else:
  print("it is not a vowel")

#3.check if a number is even or odd where the number is taken as input.

num = int(input("Enter a number"))
if num % 2 == 0:
    print("Given number is even")
else:
    print("Given number is odd")

#4. the first and last number of a list is same or not

num=[1,2,3,4,5,1,1]
if num[0]==num[-1]:
  print(" the num is Same ")
else:
  print("the num is not same")

#5.  calculate percentage of a student through 5 subjects.


a=int(input("Enter the mark for tamil:"))
b=int(input("Enter the mark for english:"))
c=int(input("Enter the mark for maths:"))
d=int(input("Enter the mark for chemistry:"))
e=int(input("Enter the mark for physics:"))
f=int(input("Enter the mark for bio :"))
sub_mark= a+b+c+d+e+f
total_mark=int(input("enter the total mark"))
percentage=(sub_mark/total_mark)*100

if percentage <90:
   print("Excellent")
elif percentage <=90 and percentage >80:
    print("very good")
elif percentage<=80 and percentage >70:
    print("good")
elif percentage<=70 and percentage>60:
    print ("average")
elif percentage<=60 and percentage>50:
     print("bad")
else:("Fail")

#6. Python program to check whether a string starts with vowel or not. 


word = input("Enter a Word")
if word[0].lower() in "aeiou":
    print("True")
else:
    print("False")


