# -*- coding: utf-8 -*-
import streamlit as st
import io
import database as db

st.set_page_config(
    page_title="🔥𝕍𝔼𝔼ℝ ℂℍ𝕆𝕌𝔻ℍ𝔸ℝ𝕐 𝔼𝟚𝔼 ℙ𝔸ℕℕ𝕃𝔼🔥",
    page_icon="🔥",
    layout="wide"
)

st.markdown(f"<h1 style='text-align:center;'>🔥𝕍𝔼𝔼ℝ ℂℍ𝕆𝕌𝔻ℍ𝔸ℝ𝕐 𝔼𝟚𝔼 ℙ𝔸ℕℕ𝕃𝔼🔥</h1>", unsafe_allow_html=True)

# ---------- SESSION ----------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_id" not in st.session_state:
    st.session_state.user_id = None
if "username" not in st.session_state:
    st.session_state.username = None

# ---------- LOGIN ----------
def login_page():
    st.subheader("Login Panel")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        uid = db.verify_user(username, password)
        if uid:
            st.session_state.logged_in = True
            st.session_state.user_id = uid
            st.session_state.username = username
            st.success("Login successful")
            st.rerun()
        else:
            st.error("Invalid username or password")

# ---------- MAIN APP ----------
def main_app():
    user_config = db.get_user_config(st.session_state.user_id)

    tab1, tab2 = st.tabs(["E2EE SETUP", "AUTOMATION"])

    # -------- TAB 1 --------
    with tab1:
        col1, col2 = st.columns(2)

        with col1:
            chat_id = st.text_input("CHAT ID", value=user_config["chat_id"])
            name_prefix = st.text_input("NAME PREFIX", value=user_config["name_prefix"])
            delay = st.number_input("DELAY (seconds)", 1, 300, user_config["delay"])

        with col2:
            cookies = st.text_area("FACEBOOK COOKIES", height=150)

            uploaded_file = st.file_uploader(
                "UPLOAD MESSAGE FILE (.txt)",
                type=["txt"]
            )

            messages = user_config["messages"]

            if uploaded_file is not None:
                stringio = io.StringIO(uploaded_file.getvalue().decode("utf-8"))
                messages = "\n".join(
                    [line.strip() for line in stringio.read().splitlines() if line.strip()]
                )
                st.success("Messages loaded from file")

            if st.button("💾 SAVE E2EE", use_container_width=True):
                final_cookies = cookies if cookies.strip() else user_config["cookies"]
                db.update_user_config(
                    st.session_state.user_id,
                    chat_id,
                    name_prefix,
                    delay,
                    final_cookies,
                    messages
                )
                st.success("Saved successfully")

    # -------- TAB 2 --------
    with tab2:
        st.info("Automation disabled on Streamlit Cloud")
        st.write("This panel is UI-only for stability.")

# ---------- ROUTER ----------
if not st.session_state.logged_in:
    login_page()
else:
    main_app()

st.markdown("<hr><center>Made by Veer Choudhary</center>", unsafe_allow_html=True)
