def find_unique_value(numbers: list[int]) -> int:
    for num in numbers:
        if numbers.count(num) == 1:
            return num
    return None  # якщо унікального числа немає

# def find_unique_value(some_list):
#    pass
assert find_unique_value([1, 2, 1, 1]) == 2
# assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2,
# assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5,
print("ОК")
