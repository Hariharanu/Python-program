#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Deepa
#
# Created:     24/01/2018
# Copyright:   (c) Deepa 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
   theFile = open("filename.txt", "r")
   theInts = []
   for val in theFile.read().split():
    theInts.append(int(val))
    theFile.close()

if __name__ == '__main__':
    main()
