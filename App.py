import streamlit as st
import requests

if st.button('Joke?'):
    r = requests.get('https://us-central1-dadsofunny.cloudfunctions.net/DadJokes/random/type/general/1')
    st.write(f'''{r.json()[0]['setup']}
    {r.json()[0]['punchline']}
    ''')

