"""
Problem:

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""


def product_array(nums):
    """
    :param nums: List[int], input array of integers
    :return: List[int], product array of integers
    """
    
    # Initialize arrays for the left and right product and the result
    n = len(nums)
    left = [1] * n
    right = [1] * n
    result = [1] * n
    
    # Fill the left product array
    for i in range(1, n):
        left[i] = left[i - 1] * nums[i - 1]
    
    # Fill the right product array
    for i in range(n - 2, -1, -1):
        right[i] = right[i + 1] * nums[i + 1]
    
    # Fill the result array with product of left and right arrays
    for i in range(n):
        result[i] = left[i] * right[i]

    return result


if __name__ == "__main__":
    # Test cases
    nums1 = [1, 2, 3, 4, 5]
    print(f"Input: {nums1} -> Output: {product_array(nums1)}")  # Expected: [120, 60, 40, 30, 24]

    nums2 = [3, 2, 1]
    print(f"Input: {nums2} -> Output: {product_array(nums2)}")  # Expected: [2, 3, 6]

"""
Time complexity: O(n)
Space complexity: O(n)
"""
