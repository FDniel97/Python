import sys

if len(sys.argv) < 2:
	print "Missing argument!"
	sys.exit()

class account:
	
	def __init__(self,name,balance,date,update):
		self.name = name
		self.balance = balance
		self.date = date
		self.update = update

	def acc_update(self, update, date):
		self.date = date
		self.balance += update
		self.update = update

	def __str__(self):
		return '%s %d %s %+d' % (self.name,self.balance,self.date,self.update)

bank = {}

try:
	f = open(sys.argv[1])
except:
	print "Input file does not exists!"
	sys.exit()

for line in f:
	line = line.split() 
	a = account(" ".join(line[1:-3]), int(line[-3]), line[-2], int(line[-1]))
	bank[line[0]] = a
	
f.close()
try:
	f = open("update.txt")
except:
	print "Input file does not exists!"
	sys.exit()

	
for line in f:
	line = line.split()
	a = line[2]
	if bank.has_key(a):
		bank[a].acc_update(int(line[-1]), line[0]) 
	else:
		b = account(" ".join(line[3:-1]), int(line[-1]), line[0], int(line[-1]))
		bank[a] = b

f.close()

bank = bank.items()
bank.sort()

f = open("newdata.txt",'w') 
f.write('\n'.join(map(lambda x: x[0] + ' ' + str(x[1]), bank)))
f.close()