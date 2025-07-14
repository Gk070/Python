def isAnagram(s, t):
    s = s.lower()
    t = t.lower()
    if len(s) != len(t):
        return False
    dict1 = {}
    for ch in s:
        if ch in dict1:
            dict1[ch] += 1
        else:
            dict1[ch] = 1
    dict2 = {}
    for ch in t:
        if ch in dict2:
            dict2[ch] += 1
        else:
            dict2[ch] = 1
    if dict1 != dict2:
        return False
    return True

s = "anagram"
t = "nagaram"
print(isAnagram(s, t))