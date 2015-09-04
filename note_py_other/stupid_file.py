#coding=utf-8

from sys import argv

name, filepath = argv
print name
print filepath
#with open(filepath) as txt:
#    print txt.read()

print "Type the filename again:"
file_again = raw_input(">>>>")

with open(file_again) as txt2:
    print txt2.read()
