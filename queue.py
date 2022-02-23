import streamlit as st
import pandas as pd
import time
import os

#st.set_page_config(layout="wide")

def intro():
    st.title("AutoQ ⏱️")
    st.subheader("A Queue Management App by Mohab Sameh 💻 ☕")
    col1, col2 = st.columns(2)
    new_title = '<p style="font-size: 22px;">If you have any problems, please scan the following QR Code to take a turn in the queue, then wait for your name to show up on the screen. You will be admitted shortly.</p>'
    col1.markdown(new_title, unsafe_allow_html=True)
    col2.image("assets/images/QR.png")
intro()

mkd = ''
st.markdown(mkd, unsafe_allow_html=True)

df = pd.read_csv("assets/queue/queue.csv", names=["ID", "Name", "Email", "Problem", "Admitted"])
rslt_df = df[df['Admitted'] == True]
st.table(rslt_df)

while True:
    time.sleep(5)
    if os.stat("assets/queue/queue.csv").st_size != 0:
        tmp_df = pd.read_csv('assets/queue/queue.csv')
        if df.equals(tmp_df) is not True:
            st.audio("assets/audio/notification.mp3")
            st.experimental_rerun()
            break
