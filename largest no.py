#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Aravinthan
#
# Created:     27/01/2018
# Copyright:   (c) Aravinthan 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
  ch=input("enter character")
  if((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
    print(ch,"is a character")
  else:
    print(ch,"not a character")


if __name__ == '__main__':
    main()
