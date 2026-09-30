#!/usr/bin/env python
# coding: utf-8

# In[1]:


#python data Structure:
#1.list
#program1:
num=[10,20,30]
num[1]=40
print(num)


# In[2]:


#program2:
num=[1,2,3,1,2]
print(num)


# In[3]:


#program3:
list_name=[1,2,3,'a','number']
print(list_name)


# In[4]:


#program4:
#4.1
empty_list=[]
print(type(empty_list))


# In[5]:


#4.2
empty_list=list()
print(empty_list)


# In[8]:


#4.3
fruit=["apple","banana"]
print(fruit)


# In[10]:


#4.4
mixed_type=[10,12.5,"a",True]
print(mixed_type)


# In[18]:


#1.list
#Functions
#1.len()
#1.1
num=[1,2,3,4,5]
print(len(num))
#1.2
num=[1,2,3,4,5]
num[3]=6
print(num)


# In[13]:


#Functions
#2.Indexing
num=[1,2,3,4,5]
print(num[3])


# In[14]:


#Functions
#3.slicing[:]
#3.1
num=[1,2,3,4,5]
print(num[1:4])


# In[16]:


#3.2
num=[1,2,3,4,5]
print(num[:2])


# In[17]:


#3.3
num=[1,2,3,4,5]
print(num[:])


# In[19]:


#Functions
#4.append()
fruits=["Apple","Banana"]
fruits.append("mango")
print(fruits)


# In[21]:


#Functions
#5.remove()
fruits=["Apple","Banana","mango"]
fruits.remove("Banana")
print(fruits)


# In[22]:


#Function
#6.index()
num=[1,2,3,4,5,1,2]
num.index(2)


# In[23]:


#Function
#7.count()
num=[1,2,3,4,5,1,2,3,1]
print(num.count(1))


# In[30]:


#function
#8.1.extend()
num1=[1,2,3,4]
num2=[5,6,7,8]
num1.extend([5,6,7,8])
print(num1)


# In[31]:


#8.2
num=[1,2,3,4]
num.extend([5,6,7,8])
print(num)


# In[32]:


#function:
#9.insert(index,value)
num=[10,20,40]
num.insert(2,30)
print(num)


# In[33]:


#function
#10.sort()
num=[10,20,40,30]
num.sort()
print(num)


# In[42]:


10.2
fruit=['apple','banana','mango','cherry']
fruit.sort()
print(fruit)


# In[48]:


#fuction
#11.reverse()
num=[10,20,30,40]
print(num.reverse)


# In[ ]:





# In[ ]:




