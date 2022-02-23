import streamlit as st
import pandas as pd
import csv

#st.set_page_config(layout="wide")

#Intro Goes Here
st.button("Refresh Responses")


st.header("Student Queue")
df = pd.read_csv("assets/queue/queue.csv", names=["ID", "Name", "Email", "Problem", "Admitted"])
#st.table(df)

colms = st.columns((1, 2, 2, 1, 1))
fields = ["ID", 'Name', 'Email', 'Problem', "Status"]
for col, field_name in zip(colms, fields):
    col.write(field_name)

row_num=0
for x, email in enumerate(df['Email']):
    col1, col2, col3, col4, col5 = st.columns((1, 2, 2, 1, 1))
    col1.write(x)  # index
    col2.write(df['Email'][x])  # email
    tmp_id = col3.write(df['ID'][x])  # unique ID
    col4.write(df['Name'][x])   # email status
    admitted = df['Admitted'][x]  # flexible type of button
    button_type = "Admitted" if admitted else "Not Admitted"
    button_phold = col5.empty()  # create a placeholder
    do_action = button_phold.button(button_type, key=x)
    if do_action:
        r = csv.reader(open('assets/queue/queue.csv'))
        lines = list(r)
        state = df.iat[row_num,4]
        st.text(state)
        if state:
            st.text(state)
            lines[row_num][4] = False
        if not state:
            st.text(state)
            lines[row_num][4] = True

        with open('assets/queue/queue.csv', 'w', newline='') as output_file_name:
            writer = csv.writer(output_file_name)
            writer.writerows(lines)

        st.experimental_rerun()
    row_num = row_num + 1
