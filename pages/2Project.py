import streamlit as st

st.title("Project")

if "my_input" not in st.session_state:
    st.session_state["my_input"]= ""

my_input = st.text_input("Masukan data text di sini", st.session_state["my_input"])
submit = st.button("Submit")
if submit:
    st.session_state["my_input"] = my_input
    st.write("Data text berhasil memasukan adalah:", my_input)