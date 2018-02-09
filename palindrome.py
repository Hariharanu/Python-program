#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Aravinthan
#
# Created:     30/01/2018
# Copyright:   (c) Aravinthan 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
 my_str =input("enter a string")
 my_str = my_str.casefold()
 rev_str = reversed(my_str)
 if list(my_str) == list(rev_str):
   print("It is palindrome")
 else:
   print("It is not palindrome")

if __name__ == '__main__':
    main()
