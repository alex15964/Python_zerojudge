try:
    while True:
        x = int(input())
        nl = []
        for i in range(0, x):
            nl.append(int(input()))

        n0, n1, n2 = 0, 0, 0
        for i in nl:
            if i % 3 == 0:
                n0 += 1
            elif (i-1) % 3 == 0:
                n1 += 1
            else:
                n2 += 1

        print(n0,n1,n2)
except EOFError:
    pass