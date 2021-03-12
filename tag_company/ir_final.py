#!/usr/bin/env python
# coding: utf-8

# In[1]:


# -- coding: utf-8 --
import pandas as pd
import pickle as pk


# In[2]:


df_ptt = pd.read_csv('stock2020_Target.csv', encoding = 'utf8')
df_company = pd.read_csv('oncomp.csv', encoding = 'utf8')


# In[3]:


print(df_company)


# In[4]:


company_list = df_company['name']

#替文章標上公司
# In[6]:


l = []


# In[7]:


for t in range(0,len(df_ptt['title'])):
    tmp_list = []
    for i in company_list:
        if i == "正文" or i == "全台":
            continue
        occur_bool = 0
        if str(df_ptt['title'][t]).find(i) != -1:
            occur_bool = 1
        elif str(df_ptt['content'][t]).find(i) != -1:
            occur_bool = 1  
        elif str(df_ptt['title'][t]).find(i[0:2]) != -1:
            if (i[0:2] !="第一" and i[0:2] !="台灣" and i[0:2] !="世界"):
                occur_bool = 1
        elif str(df_ptt['content'][t]).find(i[0:2]) != -1:
            if (i[0:2] !="第一" and i[0:2] !="台灣"and i[0:2] !="世界"):
                occur_bool = 1
        if occur_bool != 0:
            tmp_list.append(i)
    l.append(tmp_list)


# In[11]:


df_ptt['Company']=l


# In[12]:


print(df_ptt['Company'][2])

#替文章標上屬於他的clustring且有出現的tag
# In[17]:


cf_l = []


# In[18]:


#每個class有什麼feature
with open("feature_words.txt", 'r', encoding = 'utf8')as file:
    for l in file:
        d = l.split()
        cf_l.append(d)


# In[20]:


#每個class的文章有誰
with open('class_dict_21.pickle', 'rb') as d:
     class_dict = pk.load(d)


# In[21]:


#print(class_dict)


# In[41]:


feature_article_list = []


# In[42]:


for t in range(0,len(df_ptt['title'])):
    tmp_list = []
    for clas in class_dict.keys(): # clas = 0,1,2,3,4,5
        if t in class_dict[clas]:
            for i in cf_l[clas]: #拿出此class有的字
                occur_bool = 0
                if str(df_ptt['title'][t]).find(i) != -1:
                    occur_bool = 1
                elif str(df_ptt['content'][t]).find(i) != -1:
                    occur_bool = 1
                if occur_bool != 0:
                    tmp_list.append(i)
            break
    feature_article_list.append(tmp_list)
           


# In[43]:


df_ptt['feature_tag'] = feature_article_list


# In[44]:


print(df_ptt['feature_tag'] )


# In[45]:


#print(class_dict)


# In[46]:


df_ptt.to_csv('output.csv') #儲存回去給poi


# In[47]:


print(df_ptt)

