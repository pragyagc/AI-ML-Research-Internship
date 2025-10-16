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



data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["Kathmandu", "Pokhara", "Lalitpur"]
}

df = pd.DataFrame(data)

 
print(df.head() )       # First 5 rows
print(df.tail(2)  )     # Last 2 rows
# df.shape         # (rows, columns)
# df.columns       # Column names
# df.info()        # Column types and non-null count
# df.describe()    # Statistics summary


#filtering data
filtered_df=df[df["Age"] > 25] 
print(filtered_df)             # Filter rows
df[df["City"] == "Pokhara"]


#adding and removing columns
df["Country"] = "Nepal"           # Add column
df["Age+10"] = df["Age"] + 10 #add a another column
#df.drop("Age+10", axis=1, inplace=True)  # Remove column
print(df)