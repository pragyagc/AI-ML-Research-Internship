import pandas as pd

s = pd.Series([10, 20, 30, 40])
print(s)


#custom indexing
s=pd.Series([10,20,30],index =["a","b","c"])
print(s["b"])


#DATAFRAME
data={
    "name":["pragya","sane","nani"],
    "age":[21,15,25],
    "city":["bkt","ktm","lalitpur"]
}
df=pd.DataFrame(data)
print(df)


#reading from a csv file
df = pd.read_csv("data.csv")
print(df)


#writing to a csv file
df.to_csv("output.csv",index=False)
print(df)
#to a existing file

import pandas as pd

# Example DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob'],
    'Age': [25, 30]
})

# Overwrite the file
df.to_csv('data.csv', index=False, mode='w')
import pandas as pd

#  DataFrame to append
new_data = pd.DataFrame({
    'Name': ['Charlie', 'David'],
    'Age': [35, 40]
})

# Append without header
new_data.to_csv('data.csv', index=False, mode='a', header=False)
