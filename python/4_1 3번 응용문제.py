numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

holzzak = ["짝수", "홀수"]
for number in numbers:
    print("{}는 {}입니다.".format(number, holzzak[number % 2]))