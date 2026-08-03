
def generate_cube_numbers(limit):

    num = 2
    while True:
        cube = num ** 3
        if cube >= limit:
            return   # вихід із генератора
        yield cube
        num += 1
print(list(generate_cube_numbers(10)))
print(list(generate_cube_numbers(1000)))
print(list(generate_cube_numbers(100)))

