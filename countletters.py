def uni(str):
    for j in set(sorted(str)):
        a = str.count(j)
        if j.isalpha() ==False:
            continue
        if a ==1:
            print(f"{j} exists {a} time")
        else:
            print(f"{j} exists {a} times")


def ask(names , score, /):
    for i in names:
        print(i)

if __name__ == "__main__":
    uni("Thermometer and Rainguage")
    ask("names", "score")
