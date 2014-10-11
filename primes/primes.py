import math

class PrimesMaker:

    @staticmethod
    def get_primes(max_value):
        """
        This method is obsolete, and will be removed in
        favor of the generator
        """
        if (max_value < 2):
            return []

        cs = list(range(2,max_value+1))
        primes = []
        while cs:
            prime = cs.pop(0)
            primes.append(prime)
            if (prime < math.sqrt(max_value)):
                #sieve
                np = prime*2
                i=1
                while i<len(cs):
                    candidate = cs[i]
                    if (candidate >= np):
                        if candidate == np:
                            cs.pop(i)
                        else:
                            while candidate >np:
                                np += prime
                            if candidate == np:
                                cs.pop(i)
                            else:
                                i+=1
                    else:
                        i+=1

        return primes

def generate_primes(max_value):
    # they said in code review I had to make a generator.
    result = PrimesMaker.get_primes(max_value)
    for prime in result:
        yield prime
