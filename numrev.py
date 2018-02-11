#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Aravinthan
#
# Created:     02/02/2018
# Copyright:   (c) Aravinthan 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def main():
 n=int(input("Enter number: "))
 rev=0
 while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
    print("Reverse of the number:",rev)

if __name__ == '__main__':
    main()