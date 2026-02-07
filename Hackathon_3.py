# hackathon_ii_app.py
import streamlit as st

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Hackathon II – Evolution of Todo",
    page_icon="🚀",
    layout="wide"
)

# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------
st.markdown(
    """
    <div style="text-align:center; padding:50px;
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    border-radius:14px;">
        <h1 style="color:#ffffff;">Hackathon II 🚀</h1>
        <h3 style="color:#fbbf24;">
            The Evolution of Todo – Spec-Driven & Cloud-Native AI
        </h3>
        <p style="color:#e5e7eb; max-width:900px; margin:auto;">
            A multi-phase hackathon where developers evolve a Todo app
            from a simple CLI tool into an AI-powered, Kubernetes-deployed,
            event-driven cloud system.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# --------------------------------------------------
# ABOUT
# --------------------------------------------------
st.subheader("📌 About the Hackathon")

st.markdown(
    """
The future of software development is **AI-native** and **spec-driven**.

In this hackathon, participants master:
- Spec-Driven Development using **Claude Code & Spec-Kit Plus**
- Reusable Intelligence with AI Agents
- Cloud-Native deployment using Kubernetes
- Event-Driven Architecture with Kafka & Dapr

The goal is to think like a **Product Architect**, not just a coder.
"""
)

# --------------------------------------------------
# WHAT YOU WILL LEARN
# --------------------------------------------------
st.subheader("🧠 What You Will Learn")

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        **AI & Spec-Driven Development**
        - Claude Code & Spec-Kit Plus  
        - Reusable Intelligence (Agents & Skills)  
        - OpenAI Agents SDK & MCP  
        """
    )

with col2:
    st.markdown(
        """
        **Cloud-Native Stack**
        - FastAPI, Next.js, SQLModel  
        - Docker & Kubernetes (Minikube)  
        - Kafka, Dapr, Helm Charts  
        """
    )

# --------------------------------------------------
# HACKATHON PHASES
# --------------------------------------------------
st.subheader("🧩 Hackathon Phases")

st.markdown(
    """
| Phase | Description | Tech Stack |
|------|-------------|-----------|
| **Phase I** | In-Memory CLI Todo App | Python, Claude Code |
| **Phase II** | Full-Stack Web App | Next.js, FastAPI, Neon DB |
| **Phase III** | AI Todo Chatbot | OpenAI Agents SDK, MCP |
| **Phase IV** | Local Kubernetes | Docker, Minikube, Helm |
| **Phase V** | Cloud Deployment | Kafka, Dapr, DOKS / AKS |
"""
)

# --------------------------------------------------
# LIVE DEMO VIDEO
# --------------------------------------------------
st.subheader("🎥 Live Demo Video")

st.markdown(
    "Watch the working demo of the **Evolution of Todo** project below:"
)

st.video("https://youtu.be/GTk9fZc26uA")

# --------------------------------------------------
# PROJECT GOALS
# --------------------------------------------------
st.subheader("🎯 Project Goals")

st.markdown(
    """
- Build software **iteratively** using specs, not manual coding  
- Use AI agents to manage tasks via **natural language**  
- Deploy a **stateless, scalable** chatbot on Kubernetes  
- Apply real-world cloud & DevOps practices  
"""
)

# --------------------------------------------------
# FUTURE SCOPE
# --------------------------------------------------
st.subheader("🔮 Future Scope")

st.markdown(
    """
- Multi-language chatbot support (Urdu 🇵🇰)  
- Voice-based todo commands  
- Advanced analytics & audit logs  
- SaaS-ready deployment with CI/CD  
"""
)

# --------------------------------------------------
# PANAVERSITY & CAREER PATH
# --------------------------------------------------
st.subheader("🏫 Panaversity Opportunity")

st.markdown(
    """
High-performing participants may be invited to:
- Interview with **Panaversity Core Team**
- Work with founders **Zia, Rehan, Junaid, and Wania**
- Launch or join an **AI Startup**
- Teach at **Panaversity, PIAIC, or GIAIC**
"""
)

# --------------------------------------------------
# SUBMISSION INFO
# --------------------------------------------------
st.subheader("📤 Submission & Presentation")

st.markdown(
    """
**Submit each phase here:**  
👉 https://forms.gle/KMKEKaFUD6ZX4UtY8

**Required:**
- Public GitHub Repository  
- Deployed App Link  
- Demo Video (≤ 90 seconds)  
- WhatsApp number (for top teams)
"""
)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown("---")
st.markdown(
    """
<div style="text-align:center; color:gray;">
© 2026 Hackathon II – The Evolution of Todo  
Built with ❤️ using Streamlit
</div>
""",
    unsafe_allow_html=True
)
