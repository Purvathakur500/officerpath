import streamlit as st

from database.queries import (
    save_fitness_log,
    get_fitness_history,
    get_fitness_stats
)


def fitness_page():

    st.title("💪 Fitness Tracker")

    # ---------------- Back Button ----------------

    if st.button("⬅ Back to Dashboard"):
        st.session_state.fitness_page = False
        st.rerun()

    st.divider()

    # ---------------- Fitness Stats ----------------

    total_run, total_pushups, total_workouts = get_fitness_stats(
        st.session_state.user_id
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🏃 Total Distance", f"{total_run} km")

    with col2:
        st.metric("💪 Total Push-ups", total_pushups)

    with col3:
        st.metric("🔥 Workouts", total_workouts)

    st.divider()

    # ---------------- Workout Form ----------------

    st.subheader("🏋 Log Today's Workout")

    run_km = st.number_input(
        "🏃 Running (km)",
        min_value=0.0,
        value=0.0,
        step=0.5
    )

    pushups = st.number_input(
        "💪 Push-ups",
        min_value=0,
        value=0
    )

    situps = st.number_input(
        "🔥 Sit-ups",
        min_value=0,
        value=0
    )

    pullups = st.number_input(
        "🏋 Pull-ups",
        min_value=0,
        value=0
    )

    plank_seconds = st.number_input(
        "⏱ Plank (seconds)",
        min_value=0,
        value=0
    )

    if st.button("💾 Save Workout", use_container_width=True):

        save_fitness_log(
            st.session_state.user_id,
            run_km,
            pushups,
            situps,
            pullups,
            plank_seconds
        )

        st.success("Workout Saved Successfully! ✅")
        st.rerun()

    st.divider()

    # ---------------- Workout History ----------------

    st.subheader("📅 Fitness History")

    history = get_fitness_history(
        st.session_state.user_id
    )

    if history:

        for workout in history:

            with st.container(border=True):

                st.write(f"📅 Date : {workout[5]}")
                st.write(f"🏃 Running : {workout[0]} km")
                st.write(f"💪 Push-ups : {workout[1]}")
                st.write(f"🔥 Sit-ups : {workout[2]}")
                st.write(f"🏋 Pull-ups : {workout[3]}")
                st.write(f"⏱ Plank : {workout[4]} sec")

    else:

        st.info("No workout history available.")