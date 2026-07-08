import streamlit as st

from pages.pyq.nda import questions as nda_questions
from pages.pyq.cds import questions as cds_questions
from pages.pyq.afcat import questions as afcat_questions
from pages.pyq.capf import questions as capf_questions

from database.queries import (
    save_pyq_result,
    get_pyq_results
)


def pyq_page():

    st.title("📚 PYQ Practice")

    # ---------------- Back Button ----------------

    if st.button("⬅ Back to Dashboard"):
        st.session_state.pyq_page = False
        st.rerun()

    st.divider()

    # ---------------- Exam Selection ----------------

    exam = st.selectbox(
        "Select Exam",
        [
            "NDA",
            "CDS",
            "AFCAT",
            "CAPF"
        ]
    )

    if exam == "NDA":
        questions = nda_questions

    elif exam == "CDS":
        questions = cds_questions

    elif exam == "AFCAT":
        questions = afcat_questions

    else:
        questions = capf_questions

    # ---------------- Session State ----------------

    if "start_pyq" not in st.session_state:
        st.session_state.start_pyq = False

    # ---------------- Start Button ----------------

    if not st.session_state.start_pyq:

        if st.button("🚀 Start PYQ Practice", use_container_width=True):
            st.session_state.start_pyq = True
            st.rerun()

    # ---------------- PYQ Questions ----------------

    if st.session_state.start_pyq:

        st.subheader(f"📖 {exam} PYQ Practice")

        answers = []

        for i, q in enumerate(questions):

            selected = st.radio(
                f"Q{i+1}. {q['question']}",
                q["options"],
                key=f"{exam}_{i}"
            )

            answers.append(selected)

        if st.button("Submit PYQ", use_container_width=True):

            score = 0

            for i, q in enumerate(questions):

                if answers[i] == q["answer"]:
                    score += 1

            total_questions = len(questions)
            percentage = (score / total_questions) * 100

            save_pyq_result(
                st.session_state.user_id,
                exam,
                score,
                total_questions,
                percentage
            )

            st.success(f"🎯 Score : {score}/{total_questions}")
            st.info(f"📊 Percentage : {percentage:.1f}%")

            if percentage >= 80:
                st.success("⭐⭐⭐ Excellent Performance!")

            elif percentage >= 60:
                st.warning("⭐⭐ Good Performance!")

            else:
                st.error("⭐ Needs Improvement!")

            st.session_state.start_pyq = False

    # ---------------- PYQ History ----------------

    st.divider()

    st.subheader("📚 PYQ History")

    results = get_pyq_results(
        st.session_state.user_id
    )

    if results:

        for result in results:

            with st.container(border=True):

                st.write(f"🎯 Exam : {result[0]}")
                st.write(f"🏆 Score : {result[1]}/{result[2]}")
                st.write(f"📊 Percentage : {result[3]}%")
                st.write(f"📅 Date : {result[4]}")

    else:

        st.info("No PYQ attempts yet.")
        
        