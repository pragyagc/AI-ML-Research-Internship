import pandas as pd

s = pd.Series([10, 20, 30, 40])
print(s)


#custom indexing
s=pd.Series[10,20,30],index =["a","b","c"]
print(s["b"])


#DATAFRAME
data={
    "name":["pragya","sane","nani"],
    "age":[21,15,25],
    "city":["bkt","ktm","lalitpur"]
}
df=pd.DataFrame(data)
print(df)