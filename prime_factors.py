

class PrimeFactors:

    def of(number):
        factors = []

        if number < 1:
            return []

        for factor in range(2, number + 1):
            while number % factor == 0:
                factors.append(factor)
                number = number / factor

        return factors
