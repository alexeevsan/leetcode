def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    for i in range(len(nums) - 1):
        required = target - nums[i]

        if required in nums[i + 1:]:
            retrieved_i = nums[i + 1:].index(required) + i + 1
            return [i, retrieved_i]

    return []


# Example 1:#
# Input:
# nums = [2, 7, 11, 15]; target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:#
# Input:
# nums = [3, 2, 4]; target = 6
# Output: [1,2]

# Example 3:#
# Input:
# nums = [3, 3]; target = 6
# Output: [0,1]

# Example 3:#
# Input:
nums = [3, 2, 3]; target = 6
# Output: [0,2]

print(twoSum(nums, target))
