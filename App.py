
# In[8]:


import streamlit as st
# try:
#     from IPython.display import display
#     st.write = display
#     st.write('is running on notebook')
# except:
#     st.write('is running on streamlit')


# In[9]:


import requests
r = requests.get('https://us-central1-dadsofunny.cloudfunctions.net/DadJokes/random/jokes')
print('new')

# In[10]:


st.write(f'''{r.json()['setup']}
{r.json()['punchline']}
''')


# In[ ]:




