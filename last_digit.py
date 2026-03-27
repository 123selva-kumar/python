#1.display the last digit of a number.


num=int(input())
if num <10:
  print(num)
else:
   last=num%10
   print(last)