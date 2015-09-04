#coding=utf-8

from sys import argv
from os.path import exists

#script shi py de wen jian ming
script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file,to_file)

inkou = open(from_file)
indate = inkou.read()
print "the %s is exist: %s , long byte is %d" % (to_file, exists(to_file), len(indate))
with open(to_file, 'a') as a:
    a.write(indate)

inkou.close()
print "ok"

