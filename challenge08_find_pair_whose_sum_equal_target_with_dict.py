numbers = [2, 7, 11, 15,5,4]
target = 9
seen = {}

for n in numbers:
    needed = target - n
    if needed in seen:
        pair = (needed,n)
        print(pair)

    seen[n] = True

    