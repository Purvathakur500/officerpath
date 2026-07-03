import streamlit as st
from pages.registration import registration_page
from pages.dashboard import dashboard_page

st.set_page_config(
    page_title="OfficerPath",
    page_icon="🛡️",
    layout="wide"
)

# --------------------------
# Session State
# --------------------------

if "registered" not in st.session_state:
    st.session_state.registered = False

if "username" not in st.session_state:
    st.session_state.username = ""

if "target_exam" not in st.session_state:
    st.session_state.target_exam = ""

# --------------------------
# Routing
# --------------------------

from database.queries import get_all_users

users = get_all_users()

if not st.session_state.registered:

    st.title("🛡️ OfficerPath")

    if users:

        user_names = [
            f"{user[1]} ({user[2]})"
            for user in users
            ]

        selected_user = st.selectbox(
            "Select Existing User",
            user_names
        )

        if st.button("Continue"):

            selected = next(
                user for user in users
                if f"{user[1]} ({user[2]})" == selected_user
                )
            

            st.session_state.user_id = selected[0]
            st.session_state.username = selected[1]
            st.session_state.registered = True

            st.rerun()

    st.divider()

    if st.button("➕ Register New User"):
        registration_page()

else:
    dashboard_page()