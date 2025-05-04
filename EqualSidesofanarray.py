def find_even_index(arr):
    for i in range(len(arr)):
        sum1 = sum(arr[:i])
        sum2 = sum(arr[i+1:])
        if sum1 ==sum2:
            return i
    return -1
