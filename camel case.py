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
     inpu = input("Enter a string \n").lower()
     words = inpu.split(' ')
     capitalized = []
     for word in words:
      final_words = word[0].upper() + word[1:]
     capitalized.append(final_words)
     output = ' '.join(capitalized)
     print (output)

if __name__ == '__main__':
    main()
