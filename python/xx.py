# INSTRUCTIONS

'''
The male gametes or sperm cells in humans and other mammals are heterogametic and contain one of two types of sex chromosomes. They are either X or Y. The female gametes or eggs however, contain only the X sex chromosome and are homogametic.

The sperm cell determines the sex of an individual in this case. If a sperm cell containing an X chromosome fertilizes an egg, the resulting zygote will be XX or female. If the sperm cell contains a Y chromosome, then the resulting zygote will be XY or male.

Determine if the sex of the offspring will be male or female based on the X or Y chromosome present in the male's sperm.

If the sperm contains the X chromosome, return "Congratulations! You're going to have a daughter."; If the sperm contains the Y chromosome, return "Congratulations! You're going to have a son.";
'''

# SOLUTION


def chromosome_check(sperm):
    if sperm == "XX":
        return "Congratulations! You're going to have a daughter."
    else:
        return "Congratulations! You're going to have a son."

# RESOURCES

#https://www.codewars.com/kata/56530b444e831334c0000020/

# SAMPLE TEST


'''
import codewars_test as test
from solution import chromosome_check

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(chromosome_check('XY'), 'Congratulations! You\'re going to have a son.')
        test.assert_equals(chromosome_check('XX'), 'Congratulations! You\'re going to have a daughter.')
'''