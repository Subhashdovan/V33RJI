
import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Veer Choudhary E2E Panel",
    layout="wide"
)

# ---------------- PREMIUM THEME ----------------
st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at top left, #0f2027, #203a43, #2c5364);
}
.block-container {
    background: rgba(255,255,255,0.06);
    backdrop-filter: blur(18px);
    border-radius: 18px;
    padding: 2rem;
    box-shadow: 0 25px 60px rgba(0,0,0,0.45);
}
h1, h2, h3, label {
    color: #ffffff !important;
}
textarea, input {
    background: rgba(0,0,0,0.55) !important;
    color: #ffffff !important;
    border-radius: 10px !important;
}
button {
    background: linear-gradient(135deg, #ff512f, #dd2476) !important;
    color: white !important;
    border-radius: 12px !important;
    font-weight: 600 !important;
}
.footer {
    text-align:center;
    margin-top:40px;
    opacity:0.7;
    color:white;
}
</style>
""", unsafe_allow_html=True)

st.title("🔥 Veer Choudhary E2E Panel 🔥")

# ---------------- MESSAGE INPUT ----------------
messages = st.text_area(
    "TYPE MESSAGE ONE PER LINE (UNLIMITED)",
    height=200
)

uploaded_file = st.file_uploader(
    "OR CHOOSE MESSAGE FILE (.txt)",
    type=["txt"]
)

if uploaded_file is not None:
    file_text = uploaded_file.getvalue().decode("utf-8")
    messages = "\n".join(
        [line.strip() for line in file_text.splitlines() if line.strip()]
    )

st.button("SAVE E2E")

st.markdown('<div class="footer">MADE BY VEER CHOUDHARY</div>', unsafe_allow_html=True)
