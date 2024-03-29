# INSTRUCTIONS

'''
Finish the solution so that it sorts the passed in array of numbers. If the function passes in an empty array or null/nil value then it should return an empty array.

For example:

solution([1,2,3,10,5]) # should return [1,2,3,5,10]
solution(None) # should return []
'''

# SOLUTION


def solution(nums):
    if nums == None:
        return []
    else:
        return sorted(nums)

# RESOURCES

# https://www.codewars.com/kata/5174a4c0f2769dd8b1000003

# SAMPLE TEST


"""import codewars_test as test
from solution import solution

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(solution([1,2,3,10,5]), [1,2,3,5,10])
        test.assert_equals(solution(None), [])
        test.assert_equals(solution([]), [])
        test.assert_equals(solution([20,2,10]), [2,10,20])
        test.assert_equals(solution([2,20,10]), [2,10,20])
    
@test.describe("Random Tests")
def random_tests():
    
    from random import randint,random
        
    def random_generator():
        a = random()
        return None if a <= 0.05 else [] if a <= 0.1 else [randint(-100, 100) for i in range(randint(1,100))]
    
    def sol(a):
        return sorted(a) if a else []
    
    for _ in range(100):
        arr = random_generator()
        expected = sol(arr)
        @test.it(f"Testing for solution({arr})")
        def test_case():
            test.assert_equals(solution(arr), expected)
"""
