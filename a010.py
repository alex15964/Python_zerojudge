try:
    while True:
        x = int(input())
        t = 0   #判斷同因數出現幾次
        for i in range(2, x + 1):
            while x % i == 0:
                t += 1
                x /= i
            if t > 1:
                if x != 1:
                    print(str(i) + '^' + str(t) + ' * ' , end = '')
                else:
                    print(str(i) + '^' + str(t), end = '')
                    break
            elif t == 1:
                if x != 1:
                    print(str(i) + ' * ', end = '')
                else:
                    print(str(i), end = '')
                    break
            t = 0
        print('')
except EOFError:
    pass