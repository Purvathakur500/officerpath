import streamlit as st
from database.queries import add_user, get_users

st.set_page_config(page_title="OfficerPath", page_icon="🛡️")

st.title("🛡️ OfficerPath")
st.subheader("Defence Aspirant Registration")

name = st.text_input("Enter your Name")

target_exam = st.selectbox(
    "Select Target Exam",
    ["NDA","CDS", "AFCAT", "CAPF"]
)

if st.button("Register"):

    if name.strip() == "":
        st.error("Please enter your name.")

    else:
        add_user(name, target_exam)
        st.success("Registration Successful!")

st.divider()

st.subheader("Registered Users")

users = get_users()

for user in users:
    st.write(
        f"👤 {user[1]} | 🎯 {user[2]}"
    )