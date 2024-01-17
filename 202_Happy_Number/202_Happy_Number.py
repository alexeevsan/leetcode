def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """

    if n == 1:
        return True

    def summ_digits(num):
        return sum([int(i) ** 2 for i in str(num)])

    out = n

    while out != 1:
        summ = summ_digits(out)
        if len(str(summ)) == 1:
            if summ == 1:
                return True
            elif 1 < summ < 7:
                return False
        out = summ


# Example 1:#
# Input:
n = 19
# Output: true
# Explanation:
# 1**2 + 9**2 = 82
# 8**2 + 2**2 = 68
# 6**2 + 8**2 = 100
# 1**2 + 0**2 + 0**2 = 1

# Example 2:#
# Input:
# n = 2
# Output: false

print(isHappy(n))
