interests = [
    (0, "Hadoop"), (0, "Big data"), (0, "HBASE"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBASE"),
    (1, "Postgres"), (2, "Python"), (2, ""), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"), 
    (4, "machin learning"), (4, "regression"), (4, "decision trees"), 
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"),(5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistis"), 
    (6, "probability"), (6, "mathematics"), (6, "theory"), 
    (7, "machin learning"), (7, "scikit-learn"), (7, "Mahout"), 
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"), 
    (8, "Big data"), (8, "artificial intelligence"), (9, "Hadoop"), 
    (9, "java"), (9, "MapReduce"), (9, "Big Data")
]
from collections import Counter

words_and_counts = Counter(word for user, interest in interests
                                for word in interest.lower().split())
for word, count in words_and_counts.most_common():
    if count > 1:
        print(word, count)
    