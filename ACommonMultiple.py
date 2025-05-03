from collections import defaultdict
def max_beautiful_sub(t, tests):
    output = []
    for test in tests:
        n, a = test
        count = defaultdict(set)

        for i in range(n):
            for j in range(n):
                if a[j] ==0:
                    continue
                    product = a[i] * a[j]
                    for k in range(n):
                        if product % a[k] ==0:
                            quotient = product//a[k]
                            count[(product)].add(quotient)

        output.append(max(len(d) for d in count.values()) if count else 1)
    return output