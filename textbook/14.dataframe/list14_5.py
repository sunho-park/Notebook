import pandas as pd

data = {"city": ["Nagano", "Sydney", "Salt Lake City", "Athens", "Torino", "Beijing", "Vancouver", "London", "Sochi", "Rio de Janeiro"],
        "year": [1998, 2000, 2002, 2004, 2006, 2008, 2010, 2012, 2014, 2016],
        "season": ["winter", "summer", "winter", "summer", "winter", "summer", "winter", "summer", "winter", "summer"]}

df = pd.DataFrame(data)

df.to_csv("csv1.csv")