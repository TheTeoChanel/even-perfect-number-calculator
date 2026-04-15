# Perfect number calculator
 Hello, this is even perfect number calculator that I made in python!

# Table of contents
- [Table of contents](#1-table-of-contents)
- [How to run](#2-how-to-run)
- [How does it work](#3-how-does-it-work)
- [Declaring variables](#4-declaring-variables)
- [Actually calculating it lol](#5-actually-calculating-it-lol)
- [Calculating divisors](#6-calculating-divisors)
- [Final code](#7-final-code)

# How to run
I guess you can run basic python files without issues.
Libraries : `none`
python 3.13
# How does it work
So, this calculator uses [mersenne primes](https://en.wikipedia.org/wiki/Mersenne_prime) to calculate perfect numbers. If `p` is prime and `(2^p)-1` is also prime, then `2^(p-1) * ((2^p)-1)` is a perfect number!

Lets review the code :

### Step 1. Declaring variables
```python
p = 2
number = 1
divisors = []
prime = True
```

`p` will be our [mersenne prime](https://en.wikipedia.org/wiki/Mersenne_prime).
`number` is calculated perfect number.
`divisors` is optionally calculated divisors list (see soon).
`prime` is boolean to break out of prime number checking while loops.

### Step 2. Actually calculating it lol
I declare a function that calculates next `p` as a prime number.
```python
def next_p_prime():
    global p
    global prime
    while not prime:
        p += 1
        prime = True
        for i in range(2, int(p ** 0.5) + 1):
            if p % i == 0:
                prime = False
```
Then i check if `(2^p)-1` is a prime. If not then I run function again until `(2^p)-1` becomes prime. Here is the code:
```python
while not prime:
	next_p_prime() # <-- Here is this function used
	for i in range(2, int((2 ** p - 1) ** 0.5) + 1):
		if (2 ** p - 1) % i == 0:
			prime = False
```
Finally after this I set `number` to `2^(p-1) * ((2^p)-1)`!

```python
number = 2 ** (p - 1) * ((2 ** p) - 1)
```

### Step 3. Calculating divisors
This is optional because this slows down calculation **massively**.
```python
if input('Calculate divisors? It can slow down calculation (y/n)').lower() == 'y':
    calculateDivisors = True
else:
    calculateDivisors = False
```
This code asks user to enable or disable this.
`calculateDivisors` is used to decide calculating divisors or not in this code below:
```python
    if calculateDivisors:
        for i in range(1, int(number ** 0.5) + 1):
            if number % i == 0:
                divisors.append(i)
                if not i == (number / i):
                    divisors.append(round((number / i)))
        print(f'{iteration + 1}. perfect number is {number}. Mersene prime is {p}. Divisors are: {sorted(divisors)}.')
    else:
        print(f'{iteration + 1}. perfect number is {number}. Mersene prime is {p}.')
```
The list `divisors` is used here. I check every number until `ceil(sqrt(number))` because that is enough to calculate all of divisors. To not use any libraries I used `int()` function instead of `math.ceil()` and `number ** 0.5` instead of `math.sqrt()`.

After all of this I clear `divisors` list and reset `prime` to `False`.

# Final code
```python
print('Welcome to my (even) perfect-number calculator!')
input('Enter anything to start...')
if input('Calculate divisors? It can slow down calculation (y/n)').lower() == 'y':
    calculateDivisors = True
else:
   calculateDivisors = False

toCalculate = 20 #this number can be changed

p = 2
number = 1
divisors = []
prime = True

def next_p_prime():
    global p
    global prime
    while not prime:
        p += 1
        prime = True
        for i in range(2, int(p ** 0.5) + 1):
            if p % i == 0:
                prime = False

for iteration in range(toCalculate):
    while not prime:
        next_p_prime()
        for i in range(2, int((2 ** p - 1) ** 0.5) + 1):
            if (2 ** p - 1) % i == 0:
                prime = False

    number = 2 ** (p - 1) * ((2 ** p) - 1)
    if calculateDivisors:
        for i in range(1, int(number ** 0.5) + 1):
            if number % i == 0:
                divisors.append(i)
                if not i == (number / i):
                    divisors.append(round((number / i)))
        print(f'{iteration + 1}. perfect number is {number}. Mersene prime is {p}. Divisors are: {sorted(divisors)}.')
    else:
        print(f'{iteration + 1}. perfect number is {number}. Mersene prime is {p}.')
    divisors.clear()
    prime = False
input('Press any key to exit...')
```
Thats all guys, thank you for reading this :)
Bye!
