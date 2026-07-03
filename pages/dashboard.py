import streamlit as st
from database.queries import (
    add_study_session,
    get_study_sessions,
    get_dashboard_stats
)


def dashboard_page():

    st.title("🛡️ OfficerPath")

    st.success(f"Welcome {st.session_state.username} 👋")

    st.divider()

    total_sessions, total_minutes = get_dashboard_stats(
    st.session_state.user_id
    )
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("📚 Sessions", total_sessions)

    with col2:
        st.metric("⏱ Study Time", f"{total_minutes} mins")

    with col3:
        st.metric("🎯 Target", st.session_state.target_exam)

    st.divider()

    st.subheader("📚 Study Tracker")

    subject = st.selectbox(
        "Subject",
        [
            "Choose subject",
            "Maths",
            "English",
            "Reasoning",
            "GK",
            "Science"
        ]
    )

    task = st.selectbox(
        "Task",
        [
            "Choose task",
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
        value=60
    )

    if st.button("➕ Add Study Session"):
        if subject == "Choose subject":
            st.error("Please select a subject.")

        elif task == "Choose task":
            st.error("Please select a task.")

        else:
            add_study_session(
                st.session_state.user_id,
                subject,
                task,
                duration
            )

            st.success("Study Session Added! ✅")
        st.divider()

    st.subheader("📖 Study History")

    sessions = get_study_sessions(
    st.session_state.user_id
    )

    for session in sessions:

        with st.container(border=True):

            st.write(f"📚 Subject : {session[0]}")
            st.write(f"📝 Task : {session[1]}")
            st.write(f"⏱ Duration : {session[2]} mins")
            