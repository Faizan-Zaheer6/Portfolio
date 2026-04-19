import streamlit as st
from pathlib import Path
import random

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Faizan Zaheer | Backend Engineer",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. ADVANCED PURPLE NEON CSS ---
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
<style>
    html { scroll-behavior: smooth; }
    .stApp {
        background: radial-gradient(circle at center, #1a0b2e 0%, #09050f 100%);
        background-attachment: fixed;
        color: #ffffff;
    }
    .stApp::before {
        content: ""; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        background: repeating-linear-gradient(0deg, transparent, transparent 1px, rgba(157, 0, 255, 0.05) 1px, rgba(157, 0, 255, 0.05) 2px);
        pointer-events: none; z-index: 0;
        animation: moveLines 25s linear infinite;
    }
    @keyframes moveLines { from { background-position: 0 0; } to { background-position: 0 1000px; } }
    .tech-element {
        position: fixed; color: rgba(157, 0, 255, 0.08); font-size: 2.5rem;
        pointer-events: none; z-index: -1; filter: blur(1px); opacity: 0.5;
    }
    .nav-container {
        display: flex; justify-content: center; background: rgba(20, 10, 40, 0.95);
        padding: 20px; border-radius: 60px; margin-bottom: 40px;
        backdrop-filter: blur(25px); border: 1px solid #9d00ff;
        position: sticky; top: 10px; z-index: 999;
        box-shadow: 0 0 25px rgba(157, 0, 255, 0.4);
    }
    .nav-item {
        color: #bc6ff1 !important; text-decoration: none; margin: 0 30px;
        font-weight: 800; font-size: 1.2rem; transition: 0.4s ease;
    }
    .nav-item:hover { 
        text-shadow: 0 0 20px #9d00ff; transform: scale(1.15); color: #ffffff !important; 
    }
    .main-header {
        text-align: center; padding: 6rem 0; background: linear-gradient(135deg, #2d033b 0%, #000000 100%);
        border: 2px solid #9d00ff; border-radius: 35px; margin-bottom: 5rem;
        box-shadow: 0 0 60px rgba(157, 0, 255, 0.3);
    }
    .main-header h1 { font-size: 4.5rem; margin-bottom: 15px; }
    .section-header {
        color: #bc6ff1; border-bottom: 2.5px solid rgba(157, 0, 255, 0.5);
        padding-bottom: 1.5rem; margin-top: 5rem; margin-bottom: 3rem; 
        font-weight: 800; font-size: 2.8rem; text-transform: uppercase;
        letter-spacing: 2px;
    }
    .custom-card {
        background: rgba(255, 255, 255, 0.05); padding: 2.5rem; border-radius: 25px;
        border-left: 8px solid #9d00ff; margin-bottom: 2.5rem; transition: 0.5s ease-in-out;
        border-top: 1px solid rgba(157, 0, 255, 0.2); border-right: 1px solid rgba(157, 0, 255, 0.2);
    }
    .custom-card:hover {
        background: rgba(157, 0, 255, 0.12); transform: translateY(-10px);
        box-shadow: 0 10px 30px rgba(157, 0, 255, 0.2);
    }
    .skill-badge {
        display: inline-block; background: rgba(157, 0, 255, 0.2); color: #bc6ff1;
        padding: 0.7rem 1.6rem; border-radius: 40px; border: 1px solid #9d00ff; 
        margin: 0.6rem; font-size: 1rem; font-weight: 700; transition: 0.3s;
    }
    .skill-badge:hover { background: #9d00ff; color: #fff; box-shadow: 0 0 15px #9d00ff; }
    .contact-wrapper { display: flex; justify-content: space-around; padding: 3rem 0; flex-wrap: wrap; }
    .contact-box { text-align: center; text-decoration: none !important; color: white !important; transition: 0.4s; width: 220px; }
    .contact-box i { font-size: 4.5rem; color: #bc6ff1; margin-bottom: 15px; display: block; transition: 0.4s; filter: drop-shadow(0 0 10px rgba(157, 0, 255, 0.4)); }
    .contact-box:hover { transform: scale(1.2); }
    .contact-box:hover i { color: #ffffff; filter: drop-shadow(0 0 20px #9d00ff); }
    .contact-box span { font-size: 1.3rem; font-weight: bold; color: #bbbbbb; }
    .ticker-wrapper { width: 100%; overflow: hidden; background: rgba(157, 0, 255, 0.15); border-top: 2px solid #9d00ff; padding: 18px 0; position: fixed; bottom: 45px; left: 0; z-index: 1000; backdrop-filter: blur(12px); }
    .ticker { display: inline-block; white-space: nowrap; padding-left: 100%; animation: ticker 45s linear infinite; font-weight: 800; color: #bc6ff1; font-size: 1.1rem; }
    @keyframes ticker { 0% { transform: translate(0, 0); } 100% { transform: translate(-200%, 0); } }
    .footer-handle { position: fixed; bottom: 0; left: 0; width: 100%; background: #09050f; color: #9d00ff; text-align: center; padding: 12px 0; font-family: 'Courier New', monospace; font-size: 1rem; letter-spacing: 3px; border-top: 1px solid rgba(157, 0, 255, 0.2); z-index: 1001; font-weight: bold; }
</style>

<div class="nav-container">
    <a class="nav-item" href="#about">📖 About</a>
    <a class="nav-item" href="#skills">🛠️ Skills</a>
    <a class="nav-item" href="#projects">🚀 Projects</a>
    <a class="nav-item" href="#resume">📄 Resume</a>
    <a class="nav-item" href="#contact">📬 Contact</a>
</div>
""", unsafe_allow_html=True)

# --- 3. BACKGROUND FLOATING ANIMATION LOGIC ---
tech_symbols = ["💻", "🤖", "FastAPI", "Python", "SQL", "JWT", "Docker", "PostgreSQL", "🧠", "⚡", "JSON", "Git"]
floating_html = ""
for _ in range(25):
    symbol = random.choice(tech_symbols)
    left, top = random.randint(0, 100), random.randint(0, 100)
    dur = random.uniform(20, 45)
    floating_html += f'<div class="tech-element" style="left:{left}%; top:{top}%; animation: floatAround {dur}s infinite;">{symbol}</div>'

st.markdown(f"""
<style>
    @keyframes floatAround {{
        0%, 100% {{ transform: translate(0,0) rotate(0deg); }}
        33% {{ transform: translate(65px, -65px) rotate(5deg); }}
        66% {{ transform: translate(-65px, 45px) rotate(-5deg); }}
    }}
</style>
{floating_html}
""", unsafe_allow_html=True)

# --- 4. HEADER SECTION ---
st.markdown("""
<div class="main-header">
    <h1 style='color: #bc6ff1;'>👨‍💻 Muhammad Faizan Zaheer</h1>
    <h3 style='color: #ffffff;'>Backend Engineer | FastAPI Specialist | AI Enthusiast </h3>
    <p style='color: #bbbbbb; font-size: 1.4rem; max-width: 850px; margin: 0 auto; line-height: 1.6;'>
        Building High-Performance API Architectures, Secure Authentication Systems, 
        and Modern Backend Solutions with a focus on Type-Safety and Scalability.
    </p>
</div>
""", unsafe_allow_html=True)

# --- 5. ABOUT SECTION ---
st.markdown('<div id="about"></div>', unsafe_allow_html=True)
st.markdown('<h2 class="section-header">📖 About Me</h2>', unsafe_allow_html=True)
st.markdown("""
<div style="font-size: 1.25rem; line-height: 2.1; background: rgba(255,255,255,0.03); padding: 40px; border-radius: 25px; border: 1px solid rgba(157, 0, 255, 0.15);">
🚀 <b>Professional Vision:</b> I am a backend developer who thrives on solving complex structural problems through clean, optimized code.<br><br>
⚙️ <b>Technical Core:</b> Specialist in <b>FastAPI</b>, leveraging <b>Pydantic v2</b> for speed and <b>SQLAlchemy 2.0</b> for robust database interactions.<br><br>
🔐 <b>Security Standards:</b> Experienced in implementing <b>JWT</b> workflows, Bcrypt password hashing, and <b>AES-256</b> data protection layers.<br><br>
🤖 <b>AI Interests:</b> Integrating Large Language Models (LLMs) like the <b>Gemini API</b> into backend services to create intelligent user experiences.<br><br>
🎓 <b>Current Milestone:</b> Finalizing my 8th Semester BSCS at <b>NUML Faisalabad</b>, eager to contribute to global tech ecosystems.
</div>
""", unsafe_allow_html=True)

# --- 6. TECHNICAL SKILLS SECTION ---
st.markdown('<div id="skills"></div>', unsafe_allow_html=True)
st.markdown('<h2 class="section-header">🛠️ Technical Skills</h2>', unsafe_allow_html=True)

col_a, col_b = st.columns(2)
with col_a:
    st.markdown("### ⚡ Backend Ecosystem")
    s1 = ["Python (Async)", "FastAPI", "Pydantic v2", "SQLAlchemy 2.0", "Alembic Migrations", "Uvicorn", "RESTful APIs", "FastAPI Middleware"]
    st.markdown("".join([f'<span class="skill-badge">{s}</span>' for s in s1]), unsafe_allow_html=True)
    
    st.markdown("### 🗄️ Database Engineering")
    s2 = ["PostgreSQL", "Neon DB", "Redis Caching", "SQLite", "Vector Databases", "Schema Optimization"]
    st.markdown("".join([f'<span class="skill-badge">{s}</span>' for s in s2]), unsafe_allow_html=True)

with col_b:
    st.markdown("### 🔐 Security & Logic")
    s3 = ["JWT Tokens", "AES-256 Encryption", "Bcrypt Hashing", "OAuth2 Flow", "RBAC", "Data Integrity"]
    st.markdown("".join([f'<span class="skill-badge">{s}</span>' for s in s3]), unsafe_allow_html=True)
    
    st.markdown("### 🏗️ Workflow & DevOps")
    s4 = ["Repository Pattern", "Docker Containers", "Git/GitHub", "CI/CD Basics", "Railway/Render", "Linux Environment"]
    st.markdown("".join([f'<span class="skill-badge">{s}</span>' for s in s4]), unsafe_allow_html=True)

# --- 7. PROJECTS SECTION ---
st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
st.markdown('<h2 class="section-header">🚀 Featured Projects</h2>', unsafe_allow_html=True)

all_projects = [
    (
        "🔐 NeonSecureVault", 
        "Enterprise-grade security vault using <b>AES-256</b> encryption for data safety and <b>JWT</b> for authentication. Uses <b>Alembic</b> for robust migrations.", 
        "FastAPI, Neon PostgreSQL, SQLAlchemy"
    ),
    (
        "⚡ LinkZap-Pro", 
        "Fast URL shortener built for scale. Includes high-performance schema validation via <b>Pydantic v2</b> and persistent storage on Neon DB.", 
        "FastAPI, PostgreSQL, Pydantic, Streamlit"
    ),
    # Commented as requested:
    # (
    #     "🤖 AI-Based Ecommerce Engine", 
    #     "Engineered a RAG-powered Chatbot using Vector Databases for context-aware product recommendations.", 
    #     "FastAPI, Pinecone, Redis, OpenAI"
    # ),
    (
        "📊 Pulse Era Monitor", 
        "A futuristic, real-time website monitoring dashboard built with FastAPI and Streamlit. Features automated system health tracking.", 
        "FastAPI, Discord Hooks, Neon DB"
    ),
    (
        "🌤️ SKY-Pulse-API-Project", 
        "Futuristic, real-time weather and air quality monitoring dashboard. Fetches live data via <b>OpenWeatherMap APIs</b> with advanced atmospheric data visualization.", 
        "FastAPI, Streamlit, OpenWeatherMap API, Python Requests"
    ),
    (
       "🎓 EduManage Pro – Student & Course Management System",
       "FastAPI-driven management platform featuring dashboard for real-time educational analytics. Developed a secure Admin Panel with full CRUD functionality.",
       "FastAPI, PostgreSQL, SQLAlchemy, Jinja2"
    )
]

for title, desc, tech in all_projects:
    st.markdown(f"""
    <div class="custom-card">
        <h3>{title}</h3>
        <p style='font-size: 1.15rem; line-height: 1.6;'>{desc}</p>
        <div style="margin-top: 20px;">
            <span style="color:#bc6ff1; font-weight:bold;">Primary Stack:</span> 
            <code style="background:rgba(157,0,255,0.1); padding:8px 12px; border-radius:10px; color:#ffffff;">{tech}</code>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- 8. EDUCATION SECTION ---
st.markdown('<h2 class="section-header">🎓 Education</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="custom-card">
    <h3 style="color:#bc6ff1;">Bachelor of Science in Computer Science (BSCS)</h3>
    <p style="font-size:1.2rem;"><b>National University of Modern Languages (NUML), FSD</b> <span style='float:right;'>2022 – 2026</span></p>
</div>
<div class="custom-card">
    <h3 style="color:#bc6ff1;">Intermediate in Computer Science (ICS)</h3>
    <p style="font-size:1.2rem;"><b>Punjab Group of Colleges</b> | Grade: A <span style='float:right;'>2020 – 2022</span></p>
</div>
<div class="custom-card">
    <h3 style="color:#bc6ff1;">Matriculation</h3>
    <p style="font-size:1.2rem;"><b>The Educators</b> | Grade: A+ <span style='float:right;'>2020</span></p>
</div>
""", unsafe_allow_html=True)

# --- 9. CERTIFICATIONS SECTION ---
st.markdown('<h2 class="section-header">📜 Certifications</h2>', unsafe_allow_html=True)
certs = [
    ("Python Essentials 1", "Cisco Networking Academy – Foundational Python programming and logic."),
    ("Modern AI Certificate", "Cisco Networking Academy – Exploration of artificial intelligence and machine learning models."),
    ("Full-Stack Development (Backend & AI Chatbot)", "Saylani Mass IT Training (SMIT) – [In Progress] Advanced Backend & AI integration."),
    ("Microsoft Education Partner (Associate)", "Recognition of technical collaboration and educational platform expertise.")
]

for c_title, c_desc in certs:
    st.markdown(f"""
    <div class="custom-card" style="border-left-color: #00ffcc;">
        <h3 style="color: #00ffcc;">{c_title}</h3>
        <p style="font-size: 1.1rem;">{c_desc}</p>
    </div>
    """, unsafe_allow_html=True)

# --- 10. PROFESSIONAL EXPERIENCE SECTION ---
st.markdown('<h2 class="section-header">💼 Professional Experience</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="custom-card">
    <h3 style="color: #bc6ff1;">🌐 Open Source Contributor & Freelance Backend Developer</h3>
    <p style="color: #bbbbbb; font-weight: bold;">Remote Collaboration | 2024 - Present</p>
    <ul style="font-size: 1.15rem; line-height: 1.8;">
        <li>Architecting modular API structures using FastAPI for diverse enterprise requirements.</li>
        <li>Deploying AES-256 encryption protocols for high-security fintech prototypes.</li>
        <li>Automating database lifecycle management using Alembic for seamless production migrations.</li>
        <li>Optimizing legacy validation layers by transitioning to Pydantic v2.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# --- 11. RESUME SECTION ---
st.markdown('<div id="resume"></div>', unsafe_allow_html=True)
st.markdown('<h2 class="section-header">📄 Resume</h2>', unsafe_allow_html=True)
try:
    with open("Faizan_Resume.pdf", "rb") as f:
        st.download_button(
            label="📥 DOWNLOAD MY FULL TECHNICAL RESUME (PDF)",
            data=f,
            file_name="Faizan_Zaheer_Resume.pdf",
            mime="application/pdf",
            use_container_width=True
        )
except Exception:
    st.error("⚠️ Resume file 'Faizan_Resume.pdf' not found in the root directory.")

# --- 12. CONTACT SECTION WITH LOGOS ---
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
st.markdown('<h2 class="section-header">📬 Get In Touch</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="contact-wrapper">
    <a href="mailto:faizanfz@gmail.com" class="contact-box">
        <i class="fas fa-envelope"></i><span>Email Me</span>
    </a>
    <a href="https://www.linkedin.com/in/faizan-zaheer-b81746274/" target="_blank" class="contact-box">
        <i class="fab fa-linkedin"></i><span>LinkedIn</span>
    </a>
    <a href="https://github.com/Faizan-Zaheer6" target="_blank" class="contact-box">
        <i class="fab fa-github"></i><span>GitHub</span>
    </a>
</div>
""", unsafe_allow_html=True)

# --- 13. FOOTER TICKER & HANDLE ---
st.markdown("""
<div class="ticker-wrapper">
    <div class="ticker">
        • FastAPI Specialist • Pydantic v2 • Alembic Migrations • Neon PostgreSQL • JWT & AES-256 Security • Clean Code • 8th Semester BSCS • Open for Roles •
    </div>
</div>
<div class="footer-handle">
    @Faizan-Zaheer6 | Developer Portfolio
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br><br><br><br><br>", unsafe_allow_html=True)