'''
Return the next five digits of a string of primes starting from the given index
'''

import math

prime_str = "2357111317192329"
prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def isprime(n):
	ret = True
	if  n == 2:
		return True
	elif n%2 == 0 or n == 1:
		return False
	else:
		for x in prime_list:
			if x > int(math.sqrt(n)):
				break
			if n%x == 0:
				ret = False
				break
	return ret

def prime(n):
	global prime_str
	global prime_list
	number = 31
	while(len(prime_str) <= n+5):
		if isprime(number):
			prime_str += str(number)
			prime_list.append(number)
		number += 2
	return

def answer(n):
    # your code here
    prime(n)
    req_substr = prime_str[n:n+5]
    return req_substr

print answer(10000)
print prime_list[2286]
print prime_list