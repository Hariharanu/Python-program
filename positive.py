#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ARAVINTHAN
#
# Created:     07/02/2018
# Copyright:   (c) ARAVINTHAN 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
 num = float(input("Input a number: "))
 if num > 0:
   print("Number is positive number")
 elif num == 0:
   print("Number is Zero")
 else:
   print("Number is a negative number")

if __name__ == '__main__':
    main()
