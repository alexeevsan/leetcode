import time


def time_of_function(function):
    def wrapped(*args):
        start_time = time.perf_counter_ns()
        res = function(*args)

        diff = (time.perf_counter_ns() - start_time) / 1000000
        print('{:0.6f}'.format(diff) + ' ms')
        return res

    return wrapped


# ------------------------

# @time_of_function
# def containsNearbyDuplicate(nums, k):
#     answer = False
#     dict1 = {}
#
#     for i in range(len(nums)):
#         if nums[i:].count(nums[i]) > 1:
#             diff = abs(i - (nums[i+1:].index(nums[i]) + i + 1))
#             if nums[i] in dict1:
#                 if dict1[nums[i]] > diff:
#                     dict1[nums[i]] = diff
#             else:
#                 dict1[nums[i]] = diff
#
#     for val in dict1.values():
#         if val <= k:
#             answer = True
#
#     return answer

# ------------------------

# @time_of_function
# def containsNearbyDuplicate(nums, k):
#     for i in range(len(nums)):
#         if nums[i:].count(nums[i]) > 1:
#             if nums[i+1:].index(nums[i]) + 1 <= k:
#                 return True
#
#     return False

# ------------------------

# @time_of_function
# def containsNearbyDuplicate(nums, k):
#     for i in range(len(nums)):
#         try:
#             diff = abs(nums.index(nums[i], i + 1, i + k + 1) - i)
#             if diff <=k:
#                 return True
#         except:
#             continue
#
#     return False

# ------------------------

# @time_of_function
# def containsNearbyDuplicate(nums, k):
#     dct = {}
#     for i in range(len(nums)):
#         if nums[i] in dct.keys():
#             if abs(i - dct[nums[i]]) <= k:
#                 return True
#             else:
#                 dct[nums[i]] = i
#         else:
#             dct[nums[i]] = i
#
#     return False

# ------------------------

@time_of_function
def containsNearbyDuplicate(nums, k):
    seen = set()
    for i, num in enumerate(nums):
        if num in seen:
            return True

        seen.add(num)
        if i >= k:
            seen.remove(nums[i - k])

    return False


assert containsNearbyDuplicate([1, 2, 3, 1], 3) is True
assert containsNearbyDuplicate([1, 0, 1, 1], 1) is True
assert containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2) is False
assert containsNearbyDuplicate([0, 1, 2, 3, 4, 0, 0, 7, 8, 9, 10, 11, 12, 0], 1) is True
