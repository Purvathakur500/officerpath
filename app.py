import streamlit as st
from database.queries import (
    add_user,
    add_study_session,
    get_study_sessions
)

st.set_page_config(
    page_title="OfficerPath",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ OfficerPath")
st.caption("AI-Powered Defence Aspirant Companion")
st.divider()

# =========================
# Registration + Dashboard
# =========================

left_col, right_col = st.columns([2, 1])

with left_col:

    st.subheader("👤 Register")

    name = st.text_input("Enter your Name")

    target_exam = st.selectbox(
        "Target Exam",
        [
            "Select Exam",
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
            add_user(name, target_exam)
            st.success(f"Welcome {name}! 🎉")

with right_col:

    st.subheader("📊 Dashboard")

    st.info("Start your preparation journey today!")

    st.metric("📚 Study Sessions", len(get_study_sessions()))

st.divider()

# =========================
# Study Tracker
# =========================

st.subheader("📚 Study Tracker")

subject = st.selectbox(
    "Subject",
    [
        "Select Subject",
        "Maths",
        "English",
        "Reasoning",
        "GK",
        "Science"
        "Other"
    ]
)

task_type = st.selectbox(
    "Task Type",
    [
        "Select Task",
        "Lecture",
        "Revision",
        "PYQ Practice",
        "Mock Test",
        "Current Affairs",
        "Notes"
    ]
)

duration = st.number_input(
    "Duration (minutes)",
    min_value=1,
    max_value=600,
    value=60
)

if st.button("➕ Add Study Session"):

    if subject == "Select Subject":
        st.error("Please select a subject.")

    elif task_type == "Select Task":
        st.error("Please select a task.")

    else:

        # Assuming user_id = 1 for MVP
        add_study_session(
            1,
            subject,
            task_type,
            duration
        )

        st.success("Study session added successfully! ✅")

st.divider()

# =========================
# Study History
# =========================

st.subheader("📖 Recent Study Sessions")

sessions = get_study_sessions()

if sessions:

    for session in sessions:

        st.container(border=True)

        st.write(f"📚 **Subject:** {session[0]}")
        st.write(f"📝 **Task:** {session[1]}")
        st.write(f"⏱ **Duration:** {session[2]} minutes")
        st.write("---")

else:

    st.info("No study sessions found.")