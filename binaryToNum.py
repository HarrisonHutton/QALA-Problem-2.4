from sympy import isprime

def binaryToNum(bstring):
    sum = 0
    current_power = 0
    for char in range(len(bstring) - 1, -1, -1):
        if int(bstring[char]):
            sum += 2**current_power
        # Final step: adjust power of two
        current_power += 1
    return sum


def makeBStringPerms(length):
    perms = []

    current = ['0']*length
    final = ['1']*length

    perms.append(''.join(current))

    while ''.join(current) != ''.join(final):
        furthest_false = ''.join(current).rfind('0')
        current[furthest_false] = '1'

        for n in range(furthest_false + 1, len(current)):
            current[n] = '0'

        perms.append(''.join(current))

    return perms

if __name__ == "__main__":
    args = makeBStringPerms(20)
    for bstring in args:
        num = binaryToNum(bstring*3)
        div_by_three = True if not (num % 3) else False
        print(num, f"|----| This is prime: {isprime(num)}",\
         f"|----| This is divisible by three: {div_by_three}")
