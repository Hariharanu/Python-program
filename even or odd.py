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
 num = int(input("Enter a number: "))
 if (num % 2) == 0:
   print("{0} is Even".format(num))
 else:
   print("{0} is Odd".format(num))
if __name__ == '__main__':
    main()
