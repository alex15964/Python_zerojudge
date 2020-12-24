try:
    while True:
        x = int(input())
        if x == 1: 
            ans = '1'
        elif x == 0:
            ans = '0'
        else:
            ans = ''
            
        while x > 1:
            ans += str(x % 2)
            x = int(x / 2)
            if x == 1 or x == 0:
                ans += str(x)
        print(ans[::-1])

except EOFError:
    pass