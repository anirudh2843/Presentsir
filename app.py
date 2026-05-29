import streamlit as st

from src.screens.home_screen import home_screen
from src.screens.teacher_screen import teacher_screen
from src.screens.student_screen import student_screen

from src.components.dialog_auto_enroll import auto_enroll_dialog

from src.database.config import supabase


def restore_session():
    role = st.query_params.get("role")

    if role == "teacher" and "teacher_data" not in st.session_state:
        teacher_id = st.query_params.get("teacher_id")

        if teacher_id:
            response = (
                supabase.table("teachers")
                .select("*")
                .eq("teacher_id", int(teacher_id))
                .execute()
            )

            if response.data:
                st.session_state.teacher_data = response.data[0]
                st.session_state.login_type = "teacher"
                st.session_state.user_role = "teacher"
                st.session_state.is_logged_in = True

    elif role == "student" and "student_data" not in st.session_state:
        student_id = st.query_params.get("student_id")

        if student_id:
            response = (
                supabase.table("students")
                .select("*")
                .eq("student_id", int(student_id))
                .execute()
            )

            if response.data:
                st.session_state.student_data = response.data[0]
                st.session_state.login_type = "student"
                st.session_state.user_role = "student"
                st.session_state.is_logged_in = True


def main():
    
    restore_session()
    st.set_page_config(
        page_title="PresentSir - Attendance AI",
        # page_icon="https://i.ibb.co/YTYGn5qV/logo.png",
    )
    if "login_type" not in st.session_state:
        st.session_state["login_type"] = None

    match st.session_state["login_type"]:
        case "teacher":
            teacher_screen()

        case "student":
            student_screen()

        case None:
            home_screen()

    join_code = st.query_params.get("join-code")
    if join_code:
        if st.session_state.login_type != "student":
            st.session_state.login_type = "student"
            st.rerun()
        if (
            st.session_state.get("is_logged_in")
            and st.session_state.get("user_role") == "student"
        ):
            auto_enroll_dialog(join_code)


main()
