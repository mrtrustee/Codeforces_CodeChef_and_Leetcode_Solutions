answer = "just enter what the test is here"
for i in range(26):
    result  = " "
    for x in answer:
        if x == " ":
            result = result + " "
            continue
        j = ord(x) + i
        if j > 90:
            j = j - 26
        result = result + chr(j)
    print(result)
