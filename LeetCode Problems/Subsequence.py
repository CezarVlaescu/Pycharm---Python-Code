# s = 'abc'
# t = 'adbcesd

def isSubsequence(s, t):
    if len(s) > len(t):
        return False
    if len(s) == 0:
        return True
    sub = 0
    for i in range(0, len(t)):
        if sub <= len(s) - 1:
            print(s[sub])
            if s[sub] == t[i]:
                sub += 1
    return sub == len(s)

print(isSubsequence("abc", "adasbc"))
