def in_array(a1, a2):
    r = []
    for i in a2:
        for j in a1:
            if j in i:
                r.append(j)
    return sorted(set(r))
    return []
