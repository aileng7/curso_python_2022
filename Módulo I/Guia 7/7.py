def square(sample: list) -> list:
    list_result = []
    for i in sample:
        list_result.append(i ** 2)
    return list_result


print(square([1, 2, 3, 4, 5]))
print(square([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))