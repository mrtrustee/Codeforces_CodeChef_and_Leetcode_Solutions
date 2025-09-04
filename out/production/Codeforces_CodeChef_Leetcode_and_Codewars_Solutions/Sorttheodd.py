def sort_array(source_array):
    odds= sorted([a for a in source_array if a%2!=0])
    index_f_odd = 0
    for i in range(len(source_array)):
        if source_array[i]%2==1:
            source_array[i] = odds[index_f_odd]
            index_f_odd +=1
    return source_array