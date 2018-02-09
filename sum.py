#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Aravinthan
#
# Created:     29/01/2018
# Copyright:   (c) Aravinthan 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
  num = int(input("enter a number"))
  if num < 0:
   print("Enter a positive number")
  else:
   sum = 0

   while(num > 0):
       sum += num
       num -= 1
   print("The sum is",sum)

if __name__ == '__main__':
    main()
