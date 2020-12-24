try:
    while True:
        x = input()
        lst = x.split(' ')

        a = int(lst[0])
        b = int(lst[1])
        c = int(lst[2])

        a1 = ((b * -1) + ((b ** 2 - 4 * a * c) ** 0.5)) / (2 * a)
        a2 = ((b * -1) - ((b ** 2 - 4 * a * c) ** 0.5)) / (2 * a)
        #print(a1, a2)
        if b ** 2 - 4 * a * c >= 0:
            if a1 != a2:
                print('Two different roots x1=' + str(int(a1)) + ' , x2=' + str(int(a2)))
                #x.append('Two different roots x1=', int(a1) ,' x2=', int(-5))
            elif a1 == a2:
                print('Two same roots x=' + str(int(a1)))
                #x.append('Two same roots x=', int(a1))
        else:
            print('No real root')
            #x.append('No real root')
except EOFError:
    pass