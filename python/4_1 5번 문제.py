numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output = [[], [], []]

for number in numbers:
    # 1, 2, 3, 4, 5, 6, 7, 8, 9
    output[(number - 1) % 3].append(number)

print(output)