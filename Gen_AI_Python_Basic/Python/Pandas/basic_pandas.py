import pandas as pd

data = [10, 20, 30, 40, 50]
df = pd.DataFrame(data, columns=['Numbers'])
print(df)

data_dict = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df_dict = pd.DataFrame(data_dict, columns=['Name', 'Age', 'City'])

print(df_dict)

print(df_dict.describe)
print(df_dict.dtypes) #It will print data types
