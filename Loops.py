#For
primes = [2, 3, 5, 7]
for prime in primes:
	print(prime)

#Range
print
for x in range(5):
	print(x)
print
for x in range(3,8):
	print(x)
print
for x in range(3,8,2):
	print(x)
print

#While
count = 0 
while count < 5:
	print(count)
	count += 1
print

#Break and Continue

count = 0 
while True:
	print(count)
	count += 1
	if count >= 5:
		break
print

for x in range(10):
	if x % 2 == 0:
		continue
	print(x)
print

count = 0 
while ( count  < 5 ):
	print(count)
	count += 1
else:
	print("Count value reached %d" % count)
print

for i in range(1,10):
	if(i % 5 == 0):
		break
	print(i)
else:
	print("This is not printed because for loop is terminated because of break but not due to fail in condition")