import streamlit as st

st.set_page_config(page_title="Course Companion FTE", page_icon="📚", layout="wide")
st.title("📚 Course Companion FTE - Digital Tutor (Phase 1)")

# --- Sample Course Content ---
course_content = {
    "Chapter 1": {
        "title": "Introduction to AI Agents",
        "content": "AI Agents are programs that can perform tasks autonomously...",
        "quiz": {
            "question": "What is an AI Agent?",
            "options": [
                "A human teacher",
                "A program that performs tasks autonomously",
                "A computer hardware",
                "None of the above"
            ],
            "answer": "A program that performs tasks autonomously"
        }
    },
    "Chapter 2": {
        "title": "Cloud-Native Python Basics",
        "content": "Cloud-Native Python involves writing Python apps that run on cloud infrastructure...",
        "quiz": {
            "question": "What does Cloud-Native Python mean?",
            "options": [
                "Python installed locally",
                "Python apps running on cloud infrastructure",
                "Python on desktop apps",
                "None of the above"
            ],
            "answer": "Python apps running on cloud infrastructure"
        }
    },
    "Chapter 3": {
        "title": "Generative AI Fundamentals",
        "content": "Generative AI models can produce new content like text, images, or code...",
        "quiz": {
            "question": "Generative AI models can generate:",
            "options": [
                "Only text",
                "Only images",
                "Text, images, or code",
                "Only numbers"
            ],
            "answer": "Text, images, or code"
        }
    }
}

# --- Initialize Session State ---
if "progress" not in st.session_state:
    st.session_state.progress = {chapter: 0 for chapter in course_content.keys()}

# --- Mastery Function ---
def mastery_level(score):
    if score < 40:
        return "Beginner 🔴"
    elif score < 70:
        return "Learning 🟡"
    elif score < 90:
        return "Proficient 🟢"
    else:
        return "Mastered 🔵"

# --- Sidebar Navigation ---
st.sidebar.header("Course Navigation")
chapter_selected = st.sidebar.selectbox("Select Chapter", list(course_content.keys()))
chapter_data = course_content[chapter_selected]

# --- Display Chapter Content ---
st.header(chapter_data["title"])
st.write(chapter_data["content"])
st.write(f"**Your current mastery:** {mastery_level(st.session_state.progress[chapter_selected])}")

# --- Rule-Based Quiz ---
st.subheader("📋 Quiz")
quiz = chapter_data["quiz"]
st.write(f"**Question:** {quiz['question']}")
user_answer = st.radio("Choose your answer:", quiz["options"])

if st.button("Submit Answer"):
    if user_answer == quiz["answer"]:
        st.success("🎉 Correct!")
        st.session_state.progress[chapter_selected] = min(st.session_state.progress[chapter_selected] + 20, 100)
        st.write(f"Updated mastery: {mastery_level(st.session_state.progress[chapter_selected])}")
    else:
        st.error(f"❌ Incorrect. Try again! The correct answer is: {quiz['answer']}")

# --- Progress Tracker ---
st.sidebar.subheader("📊 Progress Tracker")
for chap, score in st.session_state.progress.items():
    st.sidebar.write(f"{chap}: {mastery_level(score)} ({score}%)")

# --- Freemium Gate Example ---
st.sidebar.subheader("💎 Premium Features")
if st.sidebar.button("Unlock Premium Feature"):
    st.sidebar.info("This is Phase 1 (Zero-Backend-LLM). Premium features will be available in Phase 2.")

# --- User Code Runner (Optional Interactive Section) ---
st.subheader("💻 Try Python Code Here")
user_code = st.text_area("Write Python code (simple, safe):", "print('Hello Digital Tutor!')")

if st.button("Run Your Code"):
    try:
        local_vars = {}
        exec(user_code, {"__builtins__": {}}, local_vars)
        st.success("✅ Code ran successfully!")
        if local_vars:
            st.json(local_vars)
    except Exception as e:
        st.error(f"⚠️ Error: {e}")
