#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd


# In[2]:


dataset=pd.read_csv('C:/Users/LENOVO/Desktop/Brain Tumour Detection/lung_cancer_examples.csv')


# In[3]:


dataset.head()


# In[4]:


del dataset["Name"]
del dataset["Surname"]
dataset.tail()


# In[5]:


x=dataset.iloc[:,0:4]
y=dataset.iloc[:,4:]


# In[7]:


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20 ,random_state=0)


# In[6]:


from sklearn import tree
cls=tree.DecisionTreeClassifier(criterion="entropy")
cls.fit(x_train,y_train)
ypred=cls.predict(x_test)
import sklearn.metrics as metrik
accuracy = print(metrik.accuracy_score(y_true=y_test,y_pred=ypred))
accuracy


# In[ ]:


model.save('lungCancer_new_model2.h5')


# In[ ]:


file1=open("result.txt","w")


# In[ ]:


file1.write(str(accuracy))


# In[ ]:


file1.close()

