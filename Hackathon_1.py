import streamlit as st
from datetime import datetime

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="FTE-X | Personal AI Employee Hackathon",
    layout="wide",
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🏆 FTE-X Hackathon")
menu = st.sidebar.radio(
    "Navigate",
    [
        "Hackathon Pitch",
        "Dashboard",
        "Tasks",
        "CEO Briefing",
        "Logs",
        "Settings"
    ]
)

# -----------------------------
# Fake Data (Prototype)
# -----------------------------
tasks = [
    {"task": "Reply to client email", "status": "Pending"},
    {"task": "Post LinkedIn update", "status": "Completed"},
    {"task": "Check bank transactions", "status": "Pending"},
]

logs = [
    "Email drafted for Client A",
    "LinkedIn post scheduled",
    "Bank audit completed",
]

# -----------------------------
# Hackathon Pitch Page
# -----------------------------
if menu == "Hackathon Pitch":
    st.title("🚀 FTE-X: Building a Personal AI Employee (Digital FTE)")

    st.subheader("💡 Problem")
    st.write(
        "Founders and small teams waste hours daily on repetitive tasks like emails, "
        "status reporting, and basic operations."
    )

    st.subheader("🎥 Live Demo (Hackathon Submission)")
    st.video("https://www.youtube.com/watch?v=GTk9fZc26uA")

    st.subheader("🧠 Solution")
    st.success(
        "FTE-X is a **Digital Full-Time Employee** that works 24/7, "
        "handles routine business tasks, and reports directly to leadership."
    )

    st.subheader("⚙ Key Features")
    st.write("""
    • Task management & execution  
    • Automated CEO briefings  
    • Activity & audit logs  
    • Finance & operations monitoring  
    • Cost reduction vs human FTE  
    """)

    st.subheader("🏆 Hackathon Impact")
    st.info(
        "FTE-X reduces operational costs by up to **85%** "
        "while improving speed, consistency, and scalability."
    )

# -----------------------------
# Dashboard
# -----------------------------
elif menu == "Dashboard":
    st.title("📊 FTE-X Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("🕒 Availability", "24/7", "Always On")
    col2.metric("📂 Active Tasks", len(tasks))
    col3.metric("💰 Cost / Month", "$500", "-85% vs Human")

    st.divider()

    st.subheader("🧠 AI Employee Status")
    st.success("FTE-X is running smoothly")

    st.subheader("⚡ Quick Actions")
    if st.button("Run Daily Audit"):
        st.info("FTE-X is auditing emails, tasks, and finances...")

# -----------------------------
# Tasks Page
# -----------------------------
elif menu == "Tasks":
    st.title("✅ Task Manager")

    for t in tasks:
        if t["status"] == "Pending":
            st.warning(f"🕑 {t['task']} - {t['status']}")
        else:
            st.success(f"✔ {t['task']} - {t['status']}")

    st.divider()

    new_task = st.text_input("Add new task")
    if st.button("Add Task"):
        if new_task:
            st.success(f"Task added: {new_task}")
        else:
            st.error("Task cannot be empty")

# -----------------------------
# CEO Briefing
# -----------------------------
elif menu == "CEO Briefing":
    st.title("📑 CEO Briefing (Auto-Generated)")

    st.markdown("""
    ### Executive Summary
    - Operations stable
    - One task delay detected
    - Cost optimization opportunity found
    """)

    st.subheader("📈 Weekly Stats")
    st.write("• Emails processed: 18")
    st.write("• Payments reviewed: 6")
    st.write("• Social posts scheduled: 4")

    st.subheader("🤖 AI Recommendation")
    st.info("Cancel unused SaaS subscription to save $25/month")

# -----------------------------
# Logs
# -----------------------------
elif menu == "Logs":
    st.title("📜 AI Activity Logs")

    for log in logs:
        st.code(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {log}")

# -----------------------------
# Settings
# -----------------------------
elif menu == "Settings":
    st.title("⚙ FTE-X Settings")

    st.checkbox("Enable Human Approval", value=True)
    st.checkbox("Enable Financial Monitoring", value=True)
    st.checkbox("Enable Social Automation", value=False)

    st.slider("AI Autonomy Level", 1, 10, 5)

    if st.button("Save Settings"):
        st.success("Settings saved successfully")
