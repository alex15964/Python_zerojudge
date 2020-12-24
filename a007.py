try:
    while True:
        x = input()
        for i in x:
            print(chr(int((ord(i)-7))), end = '')
        print('')
except EOFError:
    pass