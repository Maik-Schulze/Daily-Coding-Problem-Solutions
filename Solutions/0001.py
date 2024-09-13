"""
Problem:

Given a list of numbers, return whether any two sums to k. For example, given
[10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

def two_sum(nums, k):
    # Initialize an empty set to keep track of the numbers we have seen
    seen = set()
    # Iterate through each number in the list
    for num in nums:
        # Calculate the complement of the current number with respect to k
        complement = k - num
        # Check if the complement is already in the set
        if complement in seen:
            # If it is, we found a pair that sums to k
            return True
        # Add the current number to the set of seen numbers
        seen.add(num)
    
    return False
# If we complete the loop without finding a pair, return False
if __name__ == "__main__":
    print(check_target_sum([], 17))
    print(check_target_sum([10, 15, 3, 7], 17))
    print(check_target_sum([9, 15, 3, 7], 17))

"""
Time Complexity:   O(n)
Space Complexity:  O(n)
"""
