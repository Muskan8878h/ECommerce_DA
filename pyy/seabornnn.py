import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
data={
    "days" : ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
    "NOP" : [150,200,250,300,400,500,600]    
}

df=pd.DataFrame(data)
print(df)
sns.lineplot(data=data, x="days",y="NOP")

# sns.barplot(x="days",y="NOP",data=data)
# sns.scatterplot(x="days",y="NOP",data=data)
# sns.boxplot(x="month",y="passengers",data=df)
# sns.violinplot(x="month",y="passengers",data=df)
# sns.histplot(df["passengers"],bins=10)
# sns.heatmap(df.corr(),annot=True)
# sns.pairplot(df)

plt.show()