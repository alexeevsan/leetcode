def isIsomorphic(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """

    # ---------------------------------------------------------------------

    # dict1 = {ch: s.count(ch) for ch in s}
    # dict2 = {ch: t.count(ch) for ch in t}
    #
    # for val1, val2 in zip(dict1.values(), dict2.values()):
    #     if val1 != val2:
    #         return False
    #
    # return True

    # ---------------------------------------------------------------------

    count_cases = len(set(list(zip(s, t))))
    set_s = len(set(s))
    set_t = len(set(t))

    return count_cases == set_s == set_t


# s = "egg"; t = "add"
# s = "foo"; t = "bar"
# s = "paper"; t = "title"
s = "bbbaaaba"; t = "aaabbbba"


print(isIsomorphic(s, t))





