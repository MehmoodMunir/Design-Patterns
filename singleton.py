
# coding: utf-8

# In[118]:

counter = 1
class TestSingleton:
    
    __instance = None
    __var = 0
    def __init__(self):
        global counter
        self.__var = counter
        counter += 1

    def get_var(self):
        return self.__var
    @staticmethod
    def get_instance():
        if TestSingleton.__instance == None :
            TestSingleton.__instance = TestSingleton()
        return TestSingleton.__instance


# In[119]:


t1 = TestSingleton().get_instance()


# In[120]:

t1.get_var()


# In[ ]:




# In[121]:

t2 = TestSingleton.get_instance()


# In[122]:

t2.get_var()


# In[ ]:




# In[ ]:




# In[ ]:


    


# In[ ]:



