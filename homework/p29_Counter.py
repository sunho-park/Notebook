from collections import Counter

c = Counter([0, 1, 2, 0])

word_counts = Counter(c) # book 에서는 왜 document 라고 하지?

for word, count in word_counts.most_common(10):
    print(word, count)