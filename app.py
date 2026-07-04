import streamlit as st

from pages.registration import registration_page
from pages.dashboard import dashboard_page
from database.queries import get_all_users

st.set_page_config(
    page_title="OfficerPath",
    page_icon="🛡️",
    layout="wide"
)

# ---------------- Session State ----------------

if "registered" not in st.session_state:
    st.session_state.registered = False

if "show_registration" not in st.session_state:
    st.session_state.show_registration = False

if "user_id" not in st.session_state:
    st.session_state.user_id = None

if "username" not in st.session_state:
    st.session_state.username = ""

if "target_exam" not in st.session_state:
    st.session_state.target_exam = ""


# =====================================================
# DASHBOARD
# =====================================================

if st.session_state.registered:

    dashboard_page()

# =====================================================
# REGISTRATION PAGE
# =====================================================

elif st.session_state.show_registration:

    registration_page()

# =====================================================
# HOME PAGE
# =====================================================

else:

    st.title("🛡️ OfficerPath")

    st.subheader("Welcome")

    users = get_all_users()

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
                user
                for user in users
                if f"{user[1]} ({user[2]})" == selected_user
            )

            st.session_state.user_id = selected[0]
            st.session_state.username = selected[1]
            st.session_state.target_exam = selected[2]
            st.session_state.registered = True

            st.rerun()

    st.divider()

    if st.button("➕ Register New User"):

        st.session_state.show_registration = True

        st.rerun()