
def isprimes(n):
    flag = True
    for i in range(2,n):
        if (n % i) == 0:
            flag = False
            break
    return flag
        
    
    
    
