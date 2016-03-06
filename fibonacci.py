import random

fib = [0,1,1];
rabbits = random.randint(3,10**5);
#rabbits = 10**5;
for n in range(0,rabbits+1):
	if n > 2:
		fib.append(fib[1]+fib[2]);
		fib.pop(0);

print fib[2];