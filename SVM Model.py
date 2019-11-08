#Describing the properties of dataset by using histogram,frequency 
import pandas as pd # panda library

df=pd.read_csv("iris23.csv") 
df

freq_df=df['sepal.length(cm)'].value_counts()#frequency table
freq_df

freq_df=df['sepal.width(cm)'].value_counts()
freq_df

freq_df=df['petal.length(cm)'].value_counts()
freq_df

freq_df=df['petal.width(cm)'].value_counts()
freq_df

df.dtypes

df.columns

df.variety

df.describe()

df[df.Target==1].head(50)
df

df[df.Target==2].head(50)
df

df[df.Target==3].head(50)
df

df['sepal.length(cm)'].plot.hist()

df['sepal.width(cm)'].plot.hist()

df['petal.length(cm)'].plot.hist()

df['petal.length(cm)'].plot.hist()

df['sepal.length(cm)'].plot.box()

df['sepal.width(cm)'].plot.box()

df['petal.length(cm)'].plot.box()

df['petal.width(cm)'].plot.box()
df.isnull()

import matplotlib.pyplot as plt
%matplotlib inline

df0=df[df.Target==1]
df1=df[df.Target==2]
df2=df[df.Target==3]
df0.head()

df1=df[df.Target==2]
df1.head()

df2=df[df.Target==3]
df2.head()

plt.scatter(df0['sepal.length'],df0['sepal.width'],color='green',marker='+')

plt.scatter(df1['sepal.length'],df1['sepal.width'],color='blue',marker='+')

plt.scatter(df2['sepal.length'],df2['sepal.width(cm)'],color='yellow',marker='+')

plt.xlabel('sepal.length')
plt.ylabel('sepal.width')

plt.scatter(df0['petal.length'],df0['petal.width'],color='green',marker='+')

plt.scatter(df1['petal.length'],df1['petal.width'],color='blue',marker='+')

plt.scatter(df2['petal.length'],df2['petal.width'],color='yellow',marker='+')

plt.xlabel('petal.length')
plt.ylabel('petal.width')

import matplotlib.image as mpimg
%matplotlib inline

img=mpimg.imread('IRIS.jpg')

plt.figure(figsize=(20,40))

plt.axis('off')
plt.imshow(img)
X = df.iloc[:,:4].values
X
y = df['variety'].values
y
from sklearn.model_selection import train_test_split
X = df.iloc[:,:4].values
X
y = df['variety'].values
y

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)# here we are taking test size as 20
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
len(X_train)#120
len(X_test)#30

from sklearn.svm import SVC
svcclassifier = SVC(kernel = 'linear', random_state = 90)
svcclassifier.fit(X_train, y_train)
y_pred = svcclassifier.predict(X_test)
print(y_pred)
svcclassifier.score(X_test,y_test)

from sklearn.svm import SVC
svcclassifier = SVC(kernel = 'poly', random_state = 78)
svcclassifier.fit(X_train, y_train)
y_pred = svcclassifier.predict(X_test)
print(y_pred)
svcclassifier.score(X_test,y_test)


from sklearn.svm import SVC
svcclassifier = SVC(kernel = 'rbf', random_state = 40)
svcclassifier.fit(X_train, y_train)
y_pred = svcclassifier.predict(X_test)
print(y_pred)
svcclassifier.score(X_test,y_test)


from sklearn.svm import SVC
svcclassifier = SVC(kernel = 'sigmoid', random_state = 50)
svcclassifier.fit(X_train, y_train)
y_pred = svcclassifier.predict(X_test)
print(y_pred)
svcclassifier.score(X_test,y_test)
