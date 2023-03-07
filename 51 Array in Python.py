matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for row in range(3):
    for column in range(3):
        matrix[row][column] = int(input(f'Enter a value for [{row}, {column}]: '))
print('-=' * 15)
for row in range(3):
    for column in range(3):
        print(f'[{matrix[row][column]:^5}]', end='')
    print()