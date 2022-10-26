# INSTRUCTIONS

'''Write a function that takes an array of numbers (integers for the tests) and a target number. It should find two different items in the array that, when added together, give the target value. The indices of these items should then be returned in a tuple / list (depending on your language) like so: (index1, index2).

For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.

The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers; target will always be the sum of two different items from that array).

Based on: http://oj.leetcode.com/problems/two-sum/

two_sum([1, 2, 3], 4) # returns [0, 2] or [2, 0]'''

# SOLUTION

def two_sum(arr, target_sum):
    possible_ans = []
    
    for num1 in range(len(arr)):
        for num2 in range(len(arr)):
            if arr[num1] + arr[num2] == target_sum and num1 != num2:
                return [num1, num2]

# RESOURCES

# https://www.codewars.com/kata/52c31f8e6605bcc646000082

#SAMPLE TEST

test.assert_equals(sorted(two_sum([1,2,3], 4)), [0,2])
test.assert_equals(sorted(two_sum([1234,5678,9012], 14690)), [1,2])
test.assert_equals(sorted(two_sum([2,2,3], 4)), [0,1])
