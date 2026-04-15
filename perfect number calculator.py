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