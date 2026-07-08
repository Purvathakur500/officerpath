import streamlit as st

from database.queries import (
    save_study_plan,
    get_latest_study_plan
)


def ai_planner_page():

    st.title("🤖 AI Study Planner")

    if st.button("⬅ Back to Dashboard"):
        st.session_state.ai_page = False
        st.rerun()

    st.divider()

    exam = st.selectbox(
        "Target Exam",
        [
            "NDA",
            "CDS",
            "AFCAT",
            "CAPF"
        ]
    )

    months_left = st.slider(
        "Months Left",
        1,
        24,
        6
    )

    study_hours = st.slider(
        "Study Hours Per Day",
        1,
        12,
        4
    )

    weak_subject = st.selectbox(
        "Weak Subject",
        [
            "Maths",
            "English",
            "Reasoning",
            "GK",
            "Science"
        ]
    )

    if st.button("🚀 Generate Study Plan", use_container_width=True):

        plan = f"""
📅 DAILY STUDY PLAN

🎯 Target Exam : {exam}

⏰ Study Time : {study_hours} hrs/day

📚 Weak Subject : {weak_subject}

Morning
• {weak_subject} - 2 hrs

Afternoon
• English - 1 hr
• Reasoning - 1 hr

Evening
• PYQ Practice - 1 hr
• Mock Test - Alternate Days

Fitness
• Run 5 km
• Push-ups 50
• Sit-ups 60
• Plank 180 sec

Weekly
• Sunday Revision
• One Full-Length Mock Test
"""

        save_study_plan(
            st.session_state.user_id,
            exam,
            months_left,
            study_hours,
            weak_subject,
            plan
        )

        st.success("Study Plan Generated Successfully!")

    st.divider()

    st.subheader("📖 Latest Study Plan")

    latest = get_latest_study_plan(
        st.session_state.user_id
    )

    if latest:

        st.text(latest[0])

        st.caption(f"Generated on : {latest[1]}")

    else:

        st.info("No study plan generated yet.")