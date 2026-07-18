from utils.gemini_helper import generate_ai_response
from utils.predictor import predict_emotion
from utils.recommendations import get_recommendation
import streamlit as st
 
 

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Emotion Detection & Learning Support Engine",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- LOAD CSS ----------------
def load_css():
    try:
        with open("static/style.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        pass

load_css()

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.title("🎓 AI Learning Assistant")

    st.markdown("---")

    menu = st.radio(
        "Navigation",
        [
            "🏠 Dashboard",
            "😊 Emotion Detection",
            "🤖 AI Assistant",
            "📊 Analytics",
            "📜 History",
            "⚙ Settings"
        ]
    )

    st.markdown("---")

    st.write("### Developer")
    st.write("MUTTUKURI ASWARDHA CHANDU")

# ---------------- HEADER ----------------
st.title("🎓 Emotion Detection & Learning Support Engine")
st.caption("AI-powered Emotion Detection and Personalized Learning Support")

st.markdown("---")

# ---------------- DASHBOARD ----------------
if menu == "🏠 Dashboard":

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Emotion", "--")

    with col2:
        st.metric("Confidence", "--")

    with col3:
        st.metric("BERT", "Ready")

    with col4:
        st.metric("Gemini", "Ready")

    st.markdown("---")

    st.subheader("📘 About Project")

    st.info("""
This project detects student emotions using BERT,
provides personalized learning recommendations,
and uses Gemini AI to generate supportive responses.
""")

# ---------------- EMOTION PAGE ----------------
elif menu == "😊 Emotion Detection":

    st.subheader("Emotion Detection")

    text = st.text_area(
        "Enter your text",
        placeholder="Example: I feel stressed about tomorrow's exam..."
    )

    if st.button("🔍 Analyze Emotion"):

        if text.strip() == "":
            st.warning("Please enter text.")

        else:

            emotion, confidence = predict_emotion(text)

            st.success(f"😊 Detected Emotion : {emotion.upper()}")

            st.progress(confidence)

            st.metric(
                "Confidence",
                f"{confidence*100:.2f}%"
            )

            st.subheader("📚 Learning Recommendation")
            st.info(get_recommendation(emotion))

            st.subheader("🤖 AI Learning Assistant")

            try:
                ai = generate_ai_response(emotion, text)
                st.write(ai)
            except Exception as e:
                st.error(f"Gemini Error: {e}")

# ---------------- AI PAGE ----------------
elif menu == "🤖 AI Assistant":

    st.subheader("AI Learning Assistant")

    st.info("Gemini AI integration will appear here.")

# ---------------- ANALYTICS ----------------
elif menu == "📊 Analytics":

    st.subheader("Analytics Dashboard")

    col1, col2 = st.columns(2)

    with col1:
        st.info("Emotion Distribution Chart")

    with col2:
        st.info("Confidence Analysis Chart")

# ---------------- HISTORY ----------------
elif menu == "📜 History":

    st.subheader("Prediction History")

    st.write("Prediction history will be shown here.")

# ---------------- SETTINGS ----------------
elif menu == "⚙ Settings":

    st.subheader("Settings")

    st.write("Theme")
    st.toggle("Dark Mode", value=True)

    st.write("Model")

    st.selectbox(
        "Select Model",
        ["BERT", "BiLSTM", "Both"]
    )