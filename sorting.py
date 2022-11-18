import pandas as pd
# calling data frame constructor
df = pd.DataFrame()
print(df)

list = [
    {'name': 'Rachel', 'year': '1969'},
    {'name': 'Ross', 'year': '1966'},
    {'name': 'joey', 'year': '1967'},
    {'name': 'Monica', 'year': '1964'}]


df = pd.DataFrame(list)
#merges ort
print(df.sort_values(by="year", kind="mergesort"))
#quiksort
print(df.sort_values(by="year", kind="quicksort"))
#heapsort
print(df.sort_values(by="year", kind="heapsort"))

















