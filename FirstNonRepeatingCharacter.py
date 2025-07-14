s = "swiss"

def nonRepeating(s):
    
    for i in range(len(s)):
        count = 0
        for j in range(len(s)):
            if i == j:
                continue
            elif s[i] == s[j]:
                count += 1
        if count == 0:
            return s[i]

print(nonRepeating(s))