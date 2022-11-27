def isAnagram(s,t):
    
    if len(s) != len(t): return False
    
    #method 1 with T = O(n logn)
    return sorted(s) == sorted(t)
    
    
    #method 2 using Counter data type in pyhon
    return Counter(s) == Counter(t)
        
    
    #method 3 using hashmap T = O(n + m)
    mapS, mapT = {} ,{}
    
    for i in range(len(s)):
        mapS[s[i]] = 1 + mapS.get(s[i], 0)
        mapT[t[i]] = 1 + mapT.get(t[i], 0)
    
    for c in mapS:
        if mapS[c] != mapT.get(c,0):
            return False
    return True
    
    
    
print(isAnagram("aa","a"))
