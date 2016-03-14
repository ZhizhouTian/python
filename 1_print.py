#!/user/bin/python

print "hello, world!"
print abs(-4)

myString="hello, world!"
print myString

print "%s is number %d!" % ("Python", 1)

user=raw_input('Enter your name:')
print "My name is :%s." %(user)

num=raw_input('Now enter a number:')
print "num*4=%d" %(int(num, 16)*4)

print not 1

n = 6.23+1.5j
print n

print myString[0]
print myString[0:3]
print myString[0:-1]

iscool="is cool"
print "Python"+iscool
print myString+iscool

aDir={1: "daidai"}
aDir[2]="zizi"
print aDir[1]
print aDir.keys()

for k in aDir.keys():
	print k, aDir[k]

x=10
if x < 0:
	print "x must at least 0"
else:
	print "x is higher than 0"

counter=0
while counter<3:
	print counter
	counter+=1

print 'I\' like use net to:',
for item in ['item', 'net-surfing', 'homework', 'chat']:
	print item,
print
for i in range(10):
	print i,

