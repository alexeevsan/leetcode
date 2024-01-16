def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    mag = magazine

    for ch in ransomNote:
        if ch in mag:
            mag = mag.replace(ch, '', 1)
        else:
            return False

    return True


ransomNote = "aa"
magazine = "aab"

print(canConstruct(ransomNote, magazine))
