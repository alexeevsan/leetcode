def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    return ''.join(sorted(s)) == ''.join(sorted(t))


# Example 1:#
# Input:
# s = "anagram"; t = "nagaram"
# Output: true

# Example 2:#
# Input:
s = "rat"; t = "car"
# Output: false

print(isAnagram(s, t))
