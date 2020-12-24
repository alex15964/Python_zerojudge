try:
    while True:
        x = int(input())
        
        if x > 40:
            sum = 100
        elif x > 20:
            sum = x + 60
        elif x > 10:
            sum = (x-10)*2 + 60
        else:
            sum = x * 6

        print(sum)
except EOFError:
    pass