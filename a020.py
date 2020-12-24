def engtonum(x):
    englist = {
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14,
        'F': 15, 'G': 16, 'H': 17, 'I': 34, 'J': 18,
        'K': 19, 'L': 20, 'M': 21, 'N': 22, 'O': 35,
        'P': 23, 'Q': 24, 'R': 25, 'S': 26, 'T': 27,
        'U': 28, 'V': 29, 'W': 32, 'X': 30, 'Y': 31,
        'Z': 33
    }
    return englist[x]

try:
    while True:
        x = input()
        eng = engtonum(x[0])

        s = 8
        sum = 0
        sum += int(eng/10) + int(9 * (eng%10)) + int(x[-1:])
        for i in x[1:-1]:
            sum += int(i) * s
            s -= 1
        if sum % 10 == 0:
            print('real')
        else:
            print('fake')

except EOFError:
    pass