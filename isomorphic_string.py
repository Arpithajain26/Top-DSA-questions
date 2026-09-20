def isomorphic_string(s,t):
    h={}
    for i in range(len(s)):
        if s[i] in h and h[s[i]] not in t[i]:
            return False
        elif s[i] not in h and t[i] in h.values():
            return False
        else:
            h[s[i]]=t[i]
    return True
print(isomorphic_string("add","egg"))


def isomorphic_string1(s,t):
    h={}
    for i in range(len(s)):
        if s[i] in h and h[s[i]] not in t[i]:
            return False
        elif s[i] not in h and t[i] in h.values():
            return False
        else:
            h[s[i]]=t[i]
    return True
    
print(isomorphic_string1("add","egg"))