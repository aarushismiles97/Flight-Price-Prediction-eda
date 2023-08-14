#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[23]:


train_df=pd.read_excel('Data_Trai.xlsx')


# In[24]:


train_df.head()


# In[25]:


test_df=pd.read_excel('Test_s.xlsx')
test_df


# In[26]:


final_df=train_df.append(test_df)
final_df.head()


# In[27]:


final_df.tail()


# In[28]:


##FEATURE ENGINEERING 


# In[ ]:





# In[ ]:





# In[36]:


final_df['Date_of_Journey'].str.split('/').str[0]


# In[37]:


final_df['Date']=final_df['Date_of_Journey'].str.split('/').str[0]
final_df['Month']=final_df['Date_of_Journey'].str.split('/').str[1]
final_df['Year']=final_df['Date_of_Journey'].str.split('/').str[2]


# In[38]:


final_df.head(2)


# In[39]:


final_df['Date']=final_df['Date'].astype(int)


# In[40]:


final_df['Month']=final_df['Month'].astype(int)


# In[41]:


final_df['Year']=final_df['Year'].astype(int)


# In[42]:


final_df.info()


# In[44]:


final_df.drop('Date_of_Journey',axis=1,inplace=True)


# In[45]:


final_df.head(2)


# In[48]:


final_df['Arrival_Time'].str.split(' ')


# In[50]:


final_df['Arrival_Time']=final_df['Arrival_Time'].str.split(' ').str[0]


# In[ ]:


#so we still have to cut the arrival hour and arrival minute 


# In[60]:


final_df['Arrival_Hour']=final_df['Arrival_Time'].str.split(':').str[0]
final_df['Arrival_Min']=final_df['Arrival_Time'].str.split(':').str[1]


# In[61]:


final_df.head(2)


# In[ ]:





# In[65]:


final_df.info()


# In[51]:


final_df.isnull().sum()


# In[67]:


final_df.drop('Arrival_Time',axis=1,inplace=True)


# In[68]:


final_df.head(1)


# In[70]:


final_df['Dep_Time'].str.split(':').str[0]


# In[72]:


final_df['Dep_Hour']=final_df['Dep_Time'].str.split(':').str[0]
final_df['Dep_Mins']=final_df['Dep_Time'].str.split(':').str[1]


# In[73]:


final_df.head(2)


# In[74]:


final_df['Dep_Hour']=final_df['Dep_Hour'].astype(int)
final_df['Dep_Mins']=final_df['Dep_Mins'].astype(int)


# In[75]:


final_df.info()


# In[76]:


final_df.drop('Dep_Time',axis=1,inplace=True)


# In[77]:


final_df['Total_Stops'].unique()


# In[82]:


final_df['Total_Stops']=final_df['Total_Stops'].map({'non-stop':0,'1 stop':1,'2 stops':2,'3 stops':3,'4 stops':4,'nan':1})


# In[79]:


final_df.head()


# In[83]:


final_df.drop('Route',axis=1,inplace=True)


# In[84]:


final_df.head()


# In[85]:


final_df['Additional_Info'].unique()


# In[86]:


final_df['Duration'].str.split(' ').str[0 ]


# In[89]:


final_df['Duration'].str.split(' ').str[0].str.split('h')


# In[117]:


final_df['Duration_hourr']=final_df['Duration'].str.split(' ').str[0].str.split('h').str[0]


# In[118]:


final_df[final_df['Duration']=='5m']


# In[ ]:





# In[ ]:





# In[100]:


final_df[final_df['Duration']=='5m']


# In[121]:


final_df.head()


# In[ ]:





# In[113]:


final_df['Duration_hour']=final_df['Duration_hour']*60


# In[114]:


final_df.head(2)


# In[122]:


final_df['Airline'].unique()


# In[123]:


from sklearn.preprocessing import LabelEncoder
labelencoder=LabelEncoder()


# In[124]:


final_df['Airline']=labelencoder.fit_transform(final_df['Airline'])
final_df['Source']=labelencoder.fit_transform(final_df['Source'])
final_df['Destination']=labelencoder.fit_transform(final_df['Destination'])
final_df['Additional_Info']=labelencoder.fit_transform(final_df['Additional_Info'])


# In[125]:


final_df.head()


# In[126]:


final_df['Duration_hourr']= final_df['Duration_hourr'].astype(int)


# In[127]:


final_df.info()


# In[128]:


final_df['Duration_hourr']=final_df['Duration_hourr']*60


# In[129]:


final_df.head()


# In[130]:


final_df.drop('Duration_hour',axis=1,inplace=True)


# In[131]:


final_df.drop('Duration',axis=1,inplace=True)


# In[132]:


final_df.head()


# In[134]:


final_df.shape


# In[141]:


df1=pd.get_dummies(final_df['Airline'])
df2=pd.get_dummies(final_df['Source'])


# In[143]:


pd.get_dummies(final_df,columns=["Airline","Source","Destination","Additional_Info"],drop_first=True)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




