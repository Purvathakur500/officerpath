import streamlit as st

from pages.registration import registration_page
from pages.dashboard import dashboard_page
from database.queries import get_all_users
from pages.practice_pyq import pyq_page
from pages.fitness import fitness_page
from pages.ai_planner import ai_planner_page

st.set_page_config(
    page_title="OfficerPath",
    page_icon="🛡️",
    layout="wide"
)
# ------------------- OfficerPath Military Theme -------------------

st.markdown("""
<style>



/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #556B2F;
}

[data-testid="stSidebar"] * {
    color: white !important;
}

/* Headings */
h1, h2, h3, h4, h5, h6 {
    color: #556B2F !important;
}

/* Paragraphs & Labels */
p, label, span {
    color: #222222 !important;
}

/* Markdown text */
.stMarkdown {
    color: #222222 !important;
}

/* Buttons */
.stButton > button {
    background-color: #6B8E23;
    color: white;
    border-radius: 10px;
    border: none;
    font-weight: 600;
    transition: 0.3s;
}

.stButton > button:hover {
    background-color: #556B2F;
    color: white;
}

/* Selectbox */
.stSelectbox div[data-baseweb="select"] {
    background: white !important;
    color: black !important;
    border-radius: 8px;
}

/* Text Input */
.stTextInput input {
    background: white !important;
    color: black !important;
}

/* Number Input */
.stNumberInput input {
    background: white !important;
    color: black !important;
}

/* Metrics */
[data-testid="stMetric"] {
    background: white;
    padding: 15px;
    border-radius: 12px;
    border: 1px solid #D8D8C8;
}

/* Alerts */
[data-testid="stAlert"] {
    border-radius: 10px;
}

/* Horizontal line */
hr {
    border-top: 2px solid #6B8E23;
}

/* Hide Streamlit Header */
header {
    background: transparent;
}

/* Hide Streamlit Footer */
footer {
    visibility: hidden;
}

/* Hide Main Menu */
#MainMenu {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------
hide_streamlit_style = """
<style>
    [data-testid="stSidebarNav"] {
        display: none;
    }
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

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
if "pyq_page" not in st.session_state:
    st.session_state.pyq_page = False
if "fitness_page" not in st.session_state:
    st.session_state.fitness_page = False
if "ai_page" not in st.session_state:
    st.session_state.ai_page = False
# ================= Sidebar =================

if st.session_state.registered:

    with st.sidebar:

        st.title("🛡️ OfficerPath")

        st.write(f"👤 {st.session_state.username}")
        st.caption(f"🎯 {st.session_state.target_exam}")

        st.divider()

        if st.button("🏠 Dashboard", use_container_width=True):
            st.session_state.pyq_page = False
            st.session_state.fitness_page = False
            st.session_state.ai_page = False
            st.rerun()

        if st.button("📖 PYQ Practice", use_container_width=True):
            st.session_state.pyq_page = True
            st.session_state.fitness_page = False
            st.session_state.ai_page = False
            st.rerun()

        if st.button("💪 Fitness Tracker", use_container_width=True):
            st.session_state.pyq_page = False
            st.session_state.fitness_page = True
            st.session_state.ai_page = False
            st.rerun()

        if st.button("🤖 AI Planner", use_container_width=True):
            st.session_state.pyq_page = False
            st.session_state.fitness_page = False
            st.session_state.ai_page = True
            st.rerun()

        st.divider()

        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.registered = False
            st.session_state.pyq_page = False
            st.session_state.fitness_page = False
            st.session_state.ai_page = False
            st.session_state.show_registration = False
            st.session_state.user_id = None
            st.session_state.username = ""
            st.session_state.target_exam = ""
            st.rerun()

        st.divider()
        st.caption("OfficerPath v1.0")


# =====================================================
# DASHBOARD
# =====================================================
if st.session_state.pyq_page:
    pyq_page()
elif st.session_state.fitness_page:
    fitness_page()
elif st.session_state.ai_page:
    ai_planner_page()
elif st.session_state.registered:

    dashboard_page()

# =====================================================
# REGISTRATION PAGE
# =====================================================

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
    if st.session_state.show_registration:

        registration_page()