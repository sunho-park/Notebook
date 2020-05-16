numbers = [273, 103, 5, 32 ,65, 9, 72, 800, 99]

# for number in numbers:
#     if number >= 100:
#         print(" - 100 이상의 수 : ", number)

# 리스트 안 짝수, 홀수 구하기 

# for number in numbers:
#     if number % 2 == 0:
#         print("{} 는 짝수입니다. ".format(number))
#     else:
#         print("{} 는 홀수입니다. ".format(number))

for number in numbers:
    print("{} 는 {} 자릿수입니다. ".format(number, len(str(number))))