def factorial(number: int) -> int:
    tmp = 1
    for index in range(number):
        tmp *= index + 1
    return tmp


print(factorial(9))