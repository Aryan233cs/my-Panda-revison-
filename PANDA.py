import pandas as pd
import numpy as np
df = pd.read_csv("titanic.csv").copy()

#IF WE WANT TO SEE ALL(full) THE COLUMS OF OUR RESULT WE CAN USE THIS COMM AND :=pd.set_option('display.max_colwidth', None)


"""
TO PRINT SPECIFIC ROW AND COLUMN

print(df.iloc[:4,])
print(df.iloc[-5:])
"""

"""
print("the total row and column are", df.shape)
print("toltal row", df.shape[0])
print("total colum", df.shape[1])
print("column names", df.columns.tolist())
print("data types", df.dtypes)
"""

"""
print("summary", df.info())
print("statistical summary for numeric data\n", df.describe())
"""

"""
print(df.Name[:5])
TO PRINT A COLUMN USING CONDITIION ON OTHER COLUMN
print(df[df['Age']<30]['Name'] )
OR ALSO WE CAN DO
print(df.loc[df['Age']<30]['Name'])

print(df.loc[df['Sex']=='female']['Name'])
"""

"""
TO FIND THE MISSING VALUES IN COLUN AND THE PERCENTAGE OF MISSING VALUES
#print(df.isnull().sum())    
print((df.isnull().sum() / len(df)) *100)

"""

"""
THIS IS USED TO FILL THE BLANK SPACES OF THE COLUMN
median_age = df['Age'].median()
df['Age'] = df['Age'].fillna(median_age)
#################################################################################
# this is used to update your actual csv:== df.to_csv('titanic.csv', index=False)
#############################################################################
"""

"""
SORTING
dfsorta= df.sort_values(by='Age')
dfsortf= df.sort_values(by='Fare',ascending=False)
print(dfsortf)
"""

"""
GROUPBY

average= df.groupby('Sex')['Age'].mean()
fare= df.groupby('Name',sort=False)['Fare'].mean()
suurvived=df['Survived'].value_counts()
print(suurvived)
print(fare)
"""

"""
DATA ANALYSIS 
survibal_by_class = df.groupby('Pclass')['Survived'].mean()*100
survibal_by_class= survibal_by_class.sort_values(ascending=False)
#print(survibal_by_class)

average_svns= df.groupby('Survived')['Age'].mean()
#print(average_svns)

gendsur= df.groupby('Sex')['Survived'].sum()
gendsurn= df.groupby('Sex')['Survived'].sum().idxmax()
#print(gendsurn)
#print(gendsur)
"""

"""
#TASK 20
TO CREATE NEW COLUMNS WITH CONDITION
df['isChild'] = df['Age'] <18
df['isChild'] = np.where(df['Age'].isna(),np.nan,df['Age']<18)



Fare < 20 → Low
20–50 → Medium

50 → High



# PANDAS.cut() METHOD
#The pd.cut() function is built specifically for splitting numbers into bins or buckets

bins= [-np.inf,20,50,np.inf]
label = ['Low','Medium','High']

df['Fare_category'] = pd.cut(df['Fare'], bins=bins,labels=label,right=False)

# NP.SELECT() METHOD
conditions=[
    df['Fare'] <20,(df['Fare']>= 20) & (df['Fare']<=50), df['Fare']>50
]

choices=['low','medium','high']
df['Fare_category'] = np.select(conditions,choices,default=np.nan)

df.to_csv('titanic.csv', index=False)
"""