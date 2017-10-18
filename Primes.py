#   File: Primes.py
#   Kevin Nakashima
#   finds the first 100,000 prime numbers using two different algorithms
#   timing both will find their relative efficiency
#=================================================================================
import math
import time
#=================================================================================
NUM_PRIMES = 100000
NUM_PRINTS = 10000
#=================================================================================
def trialDiv():
    number = 2
    primesList = []
    primesList.append(number)
    index = 0
    triDivStartTime = time.clock()
    while len(primesList) < NUM_PRIMES:
        number += 1         #increment number to check
        root = math.sqrt(number)
        root = int(root)
        for i in range(len(primesList)):#find prime in list equal to or one above the root
            if root <= primesList[i]:
                index = i
                break
            else:
                continue
        for j in range(index,-1,-1):    #check primes in list for divisibility
            if number % primesList[j] == 0:
                break
        else:
            primesList.append(number)
        number += 1         #second increment to only check odds after 2
    triDivstopTime = time.clock()
    
#    for i in range(NUM_PRINTS):
#        print(primesList[i])
    return number - 1, triDivstopTime - triDivStartTime
#=================================================================================
def Sieve(nthPrime):
    not_prime = set()
    prime = []
    sieveStartTime = time.clock()
    for i in range(2, nthPrime + 1):
        if i not in not_prime:
            prime.append(i)
            for j in range(i*i, nthPrime + 1, i):
                not_prime.add(j)
                
    sieveStopTime = time.clock()
    
    for i in range(NUM_PRINTS - 1):
        print(prime[i])
        
    return prime[9999], (sieveStopTime - sieveStartTime)
#=================================================================================
def main():
    lastPrime, dTime = trialDiv()
    tenkPrime, sTime = Sieve(lastPrime)

    print("10,000th Prime Calculated: ", tenkPrime)
    print("100,000th Prime Calculated: ", lastPrime)
    print("Trial Division Elapsed Time:        ", dTime)
    print("Sieve of Eratosthenes Elapsed Time: ", sTime)

main()
