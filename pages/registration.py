import streamlit as st
from database.queries import add_user


def registration_page():

    st.title("🛡️ OfficerPath")

    st.caption("AI-Powered Defence Aspirant Companion")

    st.divider()

    st.subheader("👤 Register")

    name = st.text_input("Enter your Name")

    target_exam = st.selectbox(
        "Target Exam",
        [
            "Select Exam",
            "NDA",
            "CDS",
            "AFCAT",
            "CAPF"
        ]
    )

    if st.button("🚀 Start Journey"):

        if name.strip() == "":
            st.error("Please enter your name.")

        elif target_exam == "Select Exam":
            st.error("Please select your target exam.")

        else:
            user_id = add_user(name, target_exam)

            st.session_state.registered = True
            st.session_state.user_id = user_id
            st.session_state.username = name
            st.session_state.target_exam = target_exam
            st.session_state.show_registration=False
            st.rerun()