import streamlit as st
from src.database.db import enroll_student_to_subject
from src.database.config import supabase
import time


from src.database.db import create_attendance


def show_attendance_result(df, logs):
    st.write("Please review attendance before confirming.")
    st.dataframe(df, hide_index=True, width="stretch")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Discard", width="stretch"):
            st.session_state.voice_attendance_results = None
            st.session_state.attendance_images = []
            st.rerun()

    with col2:
        if st.button("Confirm & Save", width="stretch", type="primary"):
            try:
                create_attendance(logs)
                st.toast("Attendance taken")
                st.session_state.attendance_images = []
                st.session_state.voice_attendance_results = None
                st.rerun()
            except Exception as e:
                st.error("Sync failed!" + str(e))


@st.dialog("Attendance Reports")
def attendance_result_dialog(df, logs):
    show_attendance_result(df, logs)


@st.dialog("Attendance Details")
def attendance_details_dialog(
    subject,
    subject_code,
    time,
    present_students,
    absent_students,
):
    total = len(present_students) + len(absent_students)

    percentage = round(len(present_students) / total * 100, 2) if total > 0 else 0

    st.write(f"Subject: {subject}")
    st.write(f"Time: {time}")

    st.metric("Present", len(present_students))
    st.metric("Absent", len(absent_students))
    st.metric("Attendance %", f"{percentage}%")

    st.divider()

    st.subheader("✅ Present Students")

    for student in present_students:
        st.write(student)

    st.divider()

    st.subheader("❌ Absent Students")

    for student in absent_students:
        st.write(student)
