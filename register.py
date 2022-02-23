from matplotlib.pyplot import title
import streamlit as st
import pandas as pd
from gsheetsdb import connect
import numpy as np

st.title("AutoQ ⏱️")
st.subheader("A Queue Management App by Mohab Sameh 💻 ☕")

st.subheader("Please register your data here:")

ID = st.text_input('ID')
name = st.text_input('Full Name')
email = st.text_input('Email')
problem = st.selectbox('Select your problem', ['Signing Warning/Probation', 'Schedule conflicts/ Missing course/ Schedule issue', 'Other'])
if problem is 'Other':
    tmp_prob = st.text_input('Enter your problem here')
    problem = tmp_prob

dff = pd.read_csv("assets/queue/queue.csv", names=["ID", "Name", "Email", "Problem", "Admitted"])
submit_btn = st.button('Submit')
unique=True
if str(ID) in str(dff.ID.values):
    unique=False

numpy_array = np.array([[ID, name, email, problem, False]])
df = pd.DataFrame(numpy_array)
#st.table(df)
fields=['ID', 'Name', 'Email', 'Problem', 'Admitted']
if submit_btn and unique == False:
    st.error("You have already submitted this form before.")
if submit_btn and unique:
    df.to_csv('assets/queue/queue.csv', mode='a', index=False, header=False)
    st.success('Added in queue, please wait.')
    st.balloons()

