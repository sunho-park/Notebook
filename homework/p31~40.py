for x in range(10):
    if x == 3:
        continue
    if x ==5:
        break
    print(x)

#p32. sort
x = [4, 1, 2, 3]
y = sorted(x)
x.sort()
print(x)

x = sorted([-4, 1, -2, 3], key=abs, reverse=True)
print(x)

#p38. enumerate
names = ["Alice", "Bob", "Charlie", "Debbie"]
'''
for i in range(len(names)):
    print(f"name {i} is {names[i]}")

i=0
for i in names:
    print(f"name {i} is {names[i]}")
    i +=1
'''
for i, name in enumerate(names):
   print(f"name {i} is {name}")

#39 난수 생성

import random
random.seed(10)

four_uniform_randoms = [random.random() for _ in range(4)]
print(four_uniform_randoms)

print(random.random())

#random.randrange(10) [0, 1, ..., 9] 에서 난수 생성
#random.randrange(3, 6) 3~5에서 난수 생성

up_to_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(up_to_ten)
print(up_to_ten)

#리스트에서 임의의 항목을 하나 선택
m_best_friend = random.choice(["Alice", "BOb", "Charlie"])
print(m_best_friend)

# 중복이 허용되지 않는 임의의 표본 리스트
lottery_numbers = range(60)
winning_numbers = random.sample(lottery_numbers, 6)
print(winning_numbers)

for_with_replacement = [random.choice(range(10)) for _ in range(4)]
print(for_with_replacement) 

#정규 표현식

import re
re_examples = [ 
    not re.match("a", "cat"),
    re.search("a", "cat"),
    not re.search("c", "dog"),
    3==len(re.split("[ab]", "carbs")),

    "R-D-" == re.sub("[0-9]", "-", "R2D2")
]

assert all(re_examples), "all the regex examples should be True"