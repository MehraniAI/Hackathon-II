import streamlit as st

st.set_page_config(page_title="LearnFlow Simple", page_icon="📚")
st.title("📚 LearnFlow - Python Tutor")

# --- Progress Tracking ---
if "progress" not in st.session_state:
    st.session_state.progress = {"Variables": 0, "Loops": 0, "Lists": 0}

def mastery_level(score):
    if score < 40:
        return "Beginner 🔴"
    elif score < 70:
        return "Learning 🟡"
    elif score < 90:
        return "Proficient 🟢"
    else:
        return "Mastered 🔵"

# --- Python Concepts ---
st.header("Learn Python Concepts")
topic = st.selectbox("Select a topic:", ["Variables", "Loops", "Lists"])

examples = {
    "Variables": "x = 10\ny = 5\nprint(x + y)",
    "Loops": "for i in range(5):\n    print(i)",
    "Lists": "my_list = [1, 2, 3]\nfor item in my_list:\n    print(item)"
}

hints = {
    "Variables": "Variables store data. Example: x = 5",
    "Loops": "Loops repeat actions. Example: for i in range(5):",
    "Lists": "Lists store multiple items. Example: my_list = [1,2,3]"
}

st.write(f"**Your current mastery for {topic}:** {mastery_level(st.session_state.progress[topic])}")

if st.button("Show Example"):
    st.subheader(f"Example for {topic}")
    st.code(examples[topic], language="python")
    st.info(hints[topic])

# --- Python Code Runner ---
st.header("Try Your Own Code")
user_code = st.text_area("Write Python code here:", "print('Hello LearnFlow!')")

if st.button("Run Code"):
    try:
        local_vars = {}
        exec(user_code, {"__builtins__": {}}, local_vars)
        st.success("✅ Code executed successfully!")
        if local_vars:
            st.subheader("Output Variables:")
            st.json(local_vars)
        # Increase progress slightly
        st.session_state.progress[topic] = min(st.session_state.progress[topic]+20, 100)
        st.write(f"Updated mastery for {topic}: {mastery_level(st.session_state.progress[topic])}")
    except Exception as e:
        st.error(f"⚠️ Error: {e}")

# --- Mini Quiz ---
st.header("Mini Quiz")
quiz = {
    "Variables": {
        "question": "What is the correct way to assign 10 to a variable x?",
        "options": ["x == 10", "x = 10", "10 -> x", "let x = 10"],
        "answer": "x = 10"
    },
    "Loops": {
        "question": "Which loop runs a fixed number of times?",
        "options": ["while loop", "for loop", "infinite loop", "do-while loop"],
        "answer": "for loop"
    },
    "Lists": {
        "question": "How do you access the first element of a list `my_list`?",
        "options": ["my_list[0]", "my_list[1]", "my_list.first()", "my_list.get(0)"],
        "answer": "my_list[0]"
    }
}

q = quiz[topic]
st.write(f"**Question:** {q['question']}")
user_answer = st.radio("Choose an answer:", q['options'])

if st.button("Check Answer"):
    if user_answer == q['answer']:
        st.success("🎉 Correct!")
        # Increase progress for correct answer
        st.session_state.progress[topic] = min(st.session_state.progress[topic]+20, 100)
        st.write(f"Updated mastery for {topic}: {mastery_level(st.session_state.progress[topic])}")
    else:
        st.error("❌ Incorrect! Try again.")
