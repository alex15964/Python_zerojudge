try:
    while True:
        x = input()
        lst = x.split(' ')
        nqrl = []

        for i in range(int(lst[0])):
            x = input()
            nqrl.append(x.split(' '))

        for i in range(int(lst[1])):
            for j in range(int(lst[0])):
                print(nqrl[j][i] + ' ', end = '')
            print('')

except EOFError:
    pass