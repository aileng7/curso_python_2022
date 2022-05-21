def square(sample: list) -> list:
    list_result = []
    for i in sample:
        list_result.append(i**2)
    return list_result


def statistics(sample: list) -> dict:
    stat = {'media': sum(sample) / len(sample)}
    stat['varianza'] = sum(square(sample))/len(sample)-stat['media']**2
    stat['desviacion tipica'] = stat['varianza']**0.5
    return stat


print(statistics([1, 2, 3, 4, 5]))
print(statistics([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))