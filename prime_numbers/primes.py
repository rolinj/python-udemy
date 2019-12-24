def my_primes(num):
    '''
    Expected input number is 2 or above. 2 is the smallest prime number.
    Returns a list of prime numbers up to the given number.
    '''

    #List that will hold numbers determined as prime.
    prime_list = []

    #Start loop with 2 as it is the first prime number.
    for x in range(2, num+1):
        #List that will hold result of modulus operation.
        mod_result = []

		#Test each numbers with single prime numbers (2, 3, 5, 7).
		#If x number is not equal to y number, perform modulus operation
        #and append result to list. (Equal x and y will result to 0 in modulus.)
        mod_result = [ (x % y) for y in (2, 3, 5, 7) if x != y ]

		#If result 0 is not on the list, then the number is prime.
        if 0 not in mod_result:
            prime_list.append(x)
				
    return prime_list

print(my_primes(20))