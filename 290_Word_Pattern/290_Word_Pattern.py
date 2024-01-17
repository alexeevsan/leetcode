def wordPattern(pattern, s):
    """
    :type pattern: str
    :type s: str
    :rtype: bool
    """
    dict1 = {}
    words = s.split(' ')
    if len(pattern) != len(words):
        return False

    for i in range(len(pattern)):
        key = pattern[i]
        value = words[i]

        for k, v in dict1.items():
            if v == value:
                if k != key:
                    return False

        if key in dict1:
            if dict1[key] != value:
                return False
        else:
            dict1[key] = value

    return True


# Example 1:
# Input:
# pattern = "abba"; s = "dog cat cat dog"
# Output: true

# Example 2:#
# Input:
# pattern = "abba"; s = "dog cat cat fish"
# Output: false

# Example 3:#
# Input:
# pattern = "aaaa"; s = "dog cat cat dog"
# Output: false

# Example 4:#
# Input:
pattern = "abba"; s = "dog dog dog dog"
# Output: false


print(wordPattern(pattern, s))

