def last_digit(a,b):
    if b==0:
        return 1
    lasta = a%10
    if lasta ==0:
        return 0
    if lasta in {0,1,5,6}:
        length = 1
    elif lasta in {4, 9}:
        length =2
    else:
        length =4
    eff = b%length
    if eff ==0:
        eff =length
    result=(lasta **eff) %10
    return result