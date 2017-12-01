
# coding: utf-8

# In[1]:

class Korean:

    def __init__(self):
        self.name = "Korean"

    def speak_korean(self):
        return "An-neyong?"

class British:
    
    def __init__(self):
        self.name = "British"


    def speak_english(self):
        return "Hello!"

class Adapter:
    

    def __init__(self, obj, **adapted_method):
        
        self._object = obj

        
        self.__dict__.update(adapted_method)

    def __getattr__(self, attr):
        
        return getattr(self._object, attr)


objects = []


korean = Korean()


british =British()


objects.append(Adapter(korean, speak=korean.speak_korean))
objects.append(Adapter(british, speak=british.speak_english))


# In[7]:

for obj in objects:
    print("{} says '{}'\n".format(obj.name, obj.speak()))


# In[ ]:




# In[ ]:



