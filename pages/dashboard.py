import streamlit as st
from database.queries import (
    add_study_session,
    get_study_sessions,
    get_dashboard_stats,
    save_mock_result,
    get_mock_results,
    get_streak
)
from mock_tests.english import questions as english_questions
from mock_tests.reasoning import questions as reasoning_questions
from mock_tests.gk import questions as gk_questions


def dashboard_page():

    # ---------------- Dashboard ----------------

    st.title("🛡️ OfficerPath")
    st.success(f"Welcome {st.session_state.username} 👋")
    st.divider()

    total_sessions, total_minutes = get_dashboard_stats(
        st.session_state.user_id
    )
    streak = get_streak(st.session_state.user_id)
    st.write("Streak =", streak)
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("📚 Sessions", total_sessions)

    with col2:
        st.metric("⏱ Study Time", f"{total_minutes} mins")

    with col3:
        st.metric("🎯 Target", st.session_state.target_exam)
    with col4:
        st.metric("🔥 Streak", f"{streak} Days")
    st.divider()

    # ---------------- Mock Test ----------------
            # ---------------- Mock Test ----------------

    # ---------------- Mock Test ----------------

    if "start_mock" not in st.session_state:
        st.session_state.start_mock = False

    st.subheader("📝 Mock Test")

    mock_subject = st.selectbox(
        "Select Mock Test",
        [
            "English",
            "Reasoning",
            "GK"
        ]
)

    if mock_subject == "English":
        questions = english_questions
    elif mock_subject == "Reasoning":
        questions = reasoning_questions
    else:
        questions = gk_questions

    if st.button("🚀 Start Mock Test"):
        st.session_state.start_mock = True
        st.rerun()

    if st.session_state.start_mock:
        st.subheader(f"📖 {mock_subject} Mock Test")
        answers = []

        for i, q in enumerate(questions):
            selected = st.radio(
                f"Q{i+1}. {q['question']}",
                q["options"],
                key=f"{mock_subject}_{i}"
            )

            answers.append(selected)

    if st.button("Submit Test"):

        score = 0

        for i, q in enumerate(questions):
            if answers[i] == q["answer"]:
                score += 1

        total_questions = len(questions)
        percentage = (score / total_questions) * 100

        st.success(f"🎯 Score: {score}/{total_questions}")

        save_mock_result(
            st.session_state.user_id,
            mock_subject,
            score,
            total_questions,
            percentage
        )

        st.info(f"📊 Percentage: {percentage:.1f}%")

        if percentage >= 80:
            st.success("⭐⭐⭐ Excellent Performance!")
        elif percentage >= 60:
            st.warning("⭐⭐ Good Performance!")
        else:
            st.error("⭐ Needs Improvement!")

        st.session_state.start_mock = False
        st.rerun()
    # ---------------- Study Tracker ----------------

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

    # ---------------- Study History ----------------

    st.subheader("📖 Study History")

    sessions = get_study_sessions(
        st.session_state.user_id
    )

    if sessions:

        for session in sessions:

            with st.container(border=True):

                st.write(f"📚 Subject : {session[0]}")
                st.write(f"📝 Task : {session[1]}")
                st.write(f"⏱ Duration : {session[2]} mins")

    else:
        st.info("No study sessions yet.")
    st.divider()

    st.subheader("📝 Mock Test History")

    results = get_mock_results(st.session_state.user_id)

    if results:
        for result in results:
            with st.container(border=True):
                st.write(f"📚 Subject : {result[0]}")
                st.write(f"🎯 Score : {result[1]}/{result[2]}")
                st.write(f"📊 Percentage : {result[3]}%")
                st.write(f"📅 Date : {result[4]}")
    else:
        st.info("No mock tests attempted yet.")
            