
# coding: utf-8

# In[3]:

class Dog:
    def __init__(self , name):
        self.name = name
    def speak(self):
        return "barks"
class Cat:
    def __init__(self , name):
        self.name = name
    def speak(self):
        return "Meoow"
    
    
    
def get_pet(pet = "dog"):
    pets = dict (dog = Dog('harm'), cat = Cat("Peace"))
    return pets[pet]


# In[4]:

d = get_pet()


# In[5]:

d.speak()


# In[6]:

c= get_pet("cat")


# In[7]:

c.speak()


# In[ ]:




# In[ ]:



