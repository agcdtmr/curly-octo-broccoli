# INSTRUCTIONS

'''
We need a simple function that determines if a plural is needed or not. It should take a number, and return true if a plural should be used with that number or false if not. This would be useful when printing out a string such as 5 minutes, 14 apples, or 1 sun.

You only need to worry about english grammar rules for this kata, where anything that isn't singular (one of something), it is plural (not one of something).

All values will be positive integers or floats, or zero.
'''

# SOLUTION

def plural(n):
    return n != 1

# RESOURCES

# https://www.codewars.com/kata/52ceafd1f235ce81aa00073a/

# SAMPLE TEST

'''
import codewars_test as test
from solution import plural

@test.describe("Sample tests")
def _():
    @test.it("Tests")
    def __():
        test.assert_equals(plural(0), True)
        test.assert_equals(plural(1), False)
        test.assert_equals(plural(100), True)
'''