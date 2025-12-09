import pandas as pd
data={
    "Name" : ["John","Peter","Lisa"],
    "Age" : [28,34,29],
    "salary" : [50000,60000,55000]
}
df=pd.DataFrame(data)
print(df)

df.info()   #<class 'pandas.core.frame.DataFrame'>
            # RangeIndex: 3 entries, 0 to 2
            # Data columns (total 3 columns):
            # #   Column  Non-Null Count  Dtype
            # ---  ------  --------------  -----
            # 0   Name    3 non-null      object
            # 1   Age     3 non-null      int64
            # 2   salary  3 non-null      int64
            # dtypes: int64(2), object(1)
            # memory usage: 204.0+ bytes

df.describe()

# read data from excel file.....

# data1=pd.read_excel("C:/Users/muska/OneDrive/Documents/Data Analytics Hotel Booking.xlsx")
# print(data1.head(10))