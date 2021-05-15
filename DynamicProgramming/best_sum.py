def bestSum(target,arr,memo={}):
    if target in memo:
        return memo[target]
    if target==0:
        return []
    if target<0:
        return None
        
    ShortestL = None

    for num in arr:
        rem = target-num
        res = bestSum(rem,arr,memo)
        if res!=None:
            comb = res.copy()
            comb.append(num)
            if ShortestL==None or len(ShortestL)>len(comb):
                ShortestL = comb
    
    memo[target]=ShortestL
    return ShortestL 

print(bestSum(100,[1,2,5,25]))