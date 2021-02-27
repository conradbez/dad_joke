import streamlit as st
import requests

if st.button('Joke?'):
    r = requests.get('https://us-central1-dadsofunny.cloudfunctions.net/DadJokes/random/jokes')
    st.write(f'''{r.json()['setup']}
    {r.json()['punchline']}
    ''')

