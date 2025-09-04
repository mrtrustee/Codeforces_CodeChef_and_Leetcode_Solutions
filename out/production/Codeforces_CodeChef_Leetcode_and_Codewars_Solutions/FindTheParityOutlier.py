def find_outlier(integers):
    evens = [n for n in integers if n %2 ==0]
    odds = [n for n in integers if n %2 ==1]
    return evens[0] if len(evens) ==1 else odds[0]