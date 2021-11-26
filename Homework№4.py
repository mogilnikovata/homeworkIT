#!/usr/bin/env python
# coding: utf-8

# In[41]:


from random import randrange


# In[42]:


m=10000


# In[43]:


def throw():
        x = randrange(1,7) + randrange (1,7)
        return x
    


# In[44]:


k=0
n=1
x =throw()
if x == 7 or x == 11:
    print ('You win', '100%')
elif x == 2 or x == 3 or x == 12:
    print ('You lose', '0%')
else:
    for i in range (2,m):
        new_x = throw()
        while new_x!=7 or new_x!=4 or new_x!=5 or new_x!=6 or new_x!=8 or new_x!=9 or new_x!=12:
            n+=1
            if new_x == 7:
                k+=1
                break
            elif new_x!=4 or new_x!=5 or new_x!=6 or new_x!=8 or new_x!=9 or new_x!=12:
                break
            


# In[45]:


print('Вероятность выигрыша=',k/n*100,'%')


# In[ ]:




