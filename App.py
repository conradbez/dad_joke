import streamlit as st
import Library
import warnings

sidebarselect = st.sidebar.selectbox("Select your notebook",['Library'])

if sidebarselect=='Library':
    exec(open("./Library.py").read())