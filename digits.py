#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Deepa
#
# Created:     29/01/2018
# Copyright:   (c) Deepa 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
  count = 0
  a = int(input("Enter a number "))
  while (a > 0):
   count = count + 1
   a = a//10
   print ("Total number of digits : ",count)

if __name__ == '__main__':
    main()
