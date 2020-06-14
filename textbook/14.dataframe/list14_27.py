import pandas as pd
from pandas import DataFrame

dupli_data = DataFrame({"col1":[1, 1, 2, 3, 4, 4, 6, 6], 
                        "col2":["a", "b", "b", "b", "c", "c", "b", "b"]}) 

print(dupli_data)

print(dupli_data.duplicated())

print(dupli_data.drop_duplicates())