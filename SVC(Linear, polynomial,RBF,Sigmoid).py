#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[4]:


x=np.linspace(-5.0,5.0,100)
y=np.sqrt(10**2-x**2)
y=np.hstack([y,-y])
x=np.hstack([x,-x])


# In[5]:


x1=np.linspace(-5.0,5.0,100)
y1=np.sqrt(5**2-x1**2)
y1=np.hstack([y1,-y1])
x1=np.hstack([x1,-x1])


# In[6]:


plt.scatter(y,x)
plt.scatter(y1,x1)


# In[7]:


df1=pd.DataFrame(np.vstack([y,x]).T,columns=['X1','X2'])
df1['Y']=0
df2=pd.DataFrame(np.vstack([y1,x1]).T,columns=['X1','X2'])
df2['Y']=1
df=df1.append(df2)
df.head()
df.tail()


# In[8]:


X=df.iloc[:,:3]
y=df.Y


# In[9]:


y


# In[10]:


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=23)


# In[11]:


from sklearn.svm import SVC
classifier=SVC(kernel="rbf")
classifier.fit(X_train,y_train)


# In[12]:


from sklearn.metrics import accuracy_score
y_pred=classifier.predict(X_test)
y_pred


# In[13]:


y_test


# In[14]:


accuracy_score(y_test,y_pred)


# In[15]:


df['X1_square']=df['X1']**2
df['X2_square']=df['X2']**2
df['X1*X2']=(df['X1']*df['X1'])
df.head()


# In[16]:


X=df[["X1",'X2','X1_square','X2_square','X1*X2']]
Y=df["Y"]


# In[17]:


import plotly.express as px
fig=px.scatter_3d(df,x='X1_square',y='X2_square',z='X1*X2',color="Y")
fig.show()


# In[18]:


import plotly.express as px

fig = px.scatter_3d(df, x='X1', y='X2', z='X1*X2',
              color='Y')
fig.show()


# In[ ]:




