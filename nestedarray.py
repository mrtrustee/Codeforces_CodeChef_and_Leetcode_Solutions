def nestedarray(arr):
    result = 0 
    for i in range(0, len(arr)):
        if type(arr[i]) is not int:
            result+= nestedarray(arr[i])
        else:
            result+=nestedarray(arr[i])
    return result