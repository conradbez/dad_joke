
# In[8]:


import streamlit as st
try:
    from IPython.display import display
    st.write = display
    st.write('is running on notebook')
except:
    st.write('is running on streamlit')


# In[ ]:




