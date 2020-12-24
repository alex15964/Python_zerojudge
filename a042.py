try:
    while True:
        x = int(input())
        print( x * (x-1) + 2)
except EOFError:
    pass