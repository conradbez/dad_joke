
# In[8]:


import streamlit as st
try:
    from IPython.display import display
    st.write = display
    st.write('is running on notebook')
except:
    st.write('is running on streamlit')


# In[3]:


import requests
r = requests.get('https://us-central1-dadsofunny.cloudfunctions.net/DadJokes/random/jokes')


# In[5]:


f'''{r.json()['setup']}
r.json()['punchline']
'''


# In[ ]:




