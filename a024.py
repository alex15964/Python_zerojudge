try:
    while True:
        x = input()
        nl = x.split(' ')

        n1, n2 = int(nl[0]), int(nl[1])
        while n1 != 0 and n2 != 0:
            if n1 >= n2:
                n1 = int(n1 % n2)
                mn = n2
            elif n2 >= n1:
                n2 = int(n2 % n1)
                mn = n1
        if mn > 0:
            print(mn)

except EOFError:
    pass