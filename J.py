s = input()
t = input()

def isAnagram(s, t):
    cnt = {}
    if len(s) != len(t):
        return "No"

    for c in s:
        cnt[c] = cnt.get(c, 0) + 1
    for c in t:
        if c not in cnt:
            return "No"
      
        cnt[c] -= 1
        if cnt[c] < 0:
            return "No"
    return "Yes"
print(isAnagram(s, t))


