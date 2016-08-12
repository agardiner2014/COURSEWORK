# COT 4930  Python Programming
# name: Aldrick Gardiner
# id  : agardiner2014
# lab : 02

def main ():

    #Getting the upper bound variable
    upperbound =(int(input("Enter the upper bound: ")))

    
    if upperbound >= 2 and upperbound <= 300:
        printprimes(eratos(upperbound))

    else:
        print("Upper bound is out of range and terminate the execution.")
        sys.exit(0)
    


    
# a function that produces the sieve of eratosthenes
def eratos(uppbound):
    uppboundn = uppbound+1
    primes = dict()
    for i in range(2, uppboundn): primes[i] = True

    for i in primes:
        factors = range(i,uppboundn, i)
        for f in factors[1:]:
            primes[f] = False
    return [i for i in primes if primes[i]==True]

# a function that prints the prime numbers in block form

def printprimes(primes):
    n = len(primes)
    for i in range(0, len(primes), 10):
        outputString = (str(primes[i:i+10])).replace(",", "    ").replace("[","").replace("]","")
        print(outputString)

main()




    
