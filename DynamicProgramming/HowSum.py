def howSum(target,arr,memo={}):
    if target in memo:
        return memo[target]
    if target==0:
        return []
    if target<0:
        return None
    for num in arr:
        rem = target-num
        res = howSum(rem,arr,memo)
        if res!=None:
            res.append(num)
            memo[target] = res
            return memo[target]
    memo[target]=None
    return None
    
print(howSum(5,[2,3]))