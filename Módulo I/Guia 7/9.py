def mcd(number: int, maximum: int) -> int:
    while maximum > 0:
        rest = maximum
        maximum = number % maximum
        number = rest
    return number


def mcm(number: int, maximum: int) -> int:
    if number > maximum:
        greater = number
    else:
        greater = maximum
    while (greater % number != 0) or (greater % maximum != 0):
        greater += 1
    return greater


print(mcd(24, 36))
print(mcm(24, 36))