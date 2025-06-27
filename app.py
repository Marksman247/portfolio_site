# 👑 Built by MAX

# 📦 Import required libraries
import streamlit as st
import json
import os

# ✅ Set Streamlit page configuration
st.set_page_config(
    page_title="MAX's Project Portfolio 🚀",
    page_icon="🚀",
    layout="wide"
)

# ✅ Inject custom CSS to style the entire app — consistent light sky blue gradient including header
st.markdown("""
    <style>
    html, body, .stApp {
        background: linear-gradient(135deg, #d0f0f7, #b2ebf2);
        font-family: 'Poppins', sans-serif;
        color: #000000;
        margin: 0;
        padding: 0;
        overflow-x: hidden;
    }
    header[data-testid="stHeader"] {
        background: linear-gradient(135deg, #d0f0f7, #b2ebf2);
        box-shadow: none;
    }
    section[data-testid="stSidebar"] {
        background-color: #e0f7fa;
    }
    .stButton>button, .stDownloadButton>button {
        background-color: #0288d1;
        color: #ffffff;
        border-radius: 8px;
        border: none;
    }
    a {
        color: #01579b;
        font-weight: 600;
    }
    a:hover {
        color: #0288d1;
    }
    </style>
""", unsafe_allow_html=True)

# ✅ Intro section with profile image and personal intro text
col1, col2 = st.columns([1, 3])

with col1:
    st.image("assets/profile_pic.png", width=180)

with col2:
    st.markdown("""
    # 👋 Hey, I'm **MAX**
    ### Python Developer | Cybersecurity Enthusiast | Data Analytics Explorer  

    Welcome to my personal project portfolio — a curated collection of apps, tools, and projects I've built with passion, purpose, and precision.

    ---

    ### 🔥 What Drives Me  

    I'm deeply driven by a hunger to solve problems, simplify processes, and turn great ideas into clean, functional, and impactful digital solutions. Every project here reflects my constant pursuit of mastery, innovation, and meaningful work.

    ---

    ### 💡 Favorite Quote  

    > *"The best way to predict the future is to build it."*

    ---
    """, unsafe_allow_html=True)

# ✅ Certifications section with clickable external links
st.markdown("""
## 📜 Certifications  

- <a href="https://www.coursera.org/account/accomplishments/verify/OZ9VZXYM2A1F" target="_blank">📊 Foundations: Data, Data, Everywhere — Google</a>  
- <a href="https://www.coursera.org/account/accomplishments/verify/1MXVGDXPBQNN" target="_blank">🤖 Introduction to Artificial Intelligence (AI) — IBM</a>  
- <a href="https://www.coursera.org/account/accomplishments/professional-cert/1CQ4EDES6QA7" target="_blank">🛡️ IBM Cybersecurity Analyst — IBM</a>  
- <a href="https://www.coursera.org/account/accomplishments/verify/K069HSQZ3TUZ" target="_blank">🔐 Cybersecurity for Everyone — University of Maryland, College Park</a>  
- <a href="https://www.coursera.org/account/accomplishments/verify/OFYIZZS5ZZ1A" target="_blank">📊 AI Python for Beginners — Coursera</a>  

---
""", unsafe_allow_html=True)

# ✅ Load projects data securely from JSON file
try:
    with open("projects.json", "r", encoding="utf-8") as f:
        projects = json.load(f)
except FileNotFoundError:
    st.error("❌ projects.json file not found. Please check your directory.")
    st.stop()

# ✅ Projects section with cards displaying details, icons, and working links
st.markdown("## 📂 My Projects")

for project in projects:
    col1, col2 = st.columns([1, 3])

    with col1:
        # Load image if available, fallback to placeholder
        image_path = project.get("image", "assets/placeholder.png")
        if not os.path.exists(image_path):
            image_path = "assets/placeholder.png"
        st.image(image_path, width=100)

    with col2:
        # Dynamically assign emoji based on project title keywords
        emoji = "🚀"
        title = project["title"]
        if "Vulnerability" in title:
            emoji = "🛡️"
        elif "Port Scanner" in title:
            emoji = "📡"
        elif "Data Cleaner" in title:
            emoji = "🧹"
        elif "Profiler" in title:
            emoji = "📊"
        elif "Summary" in title:
            emoji = "📝"
        elif "Password" in title:
            emoji = "🔒"
        elif "Network" in title:
            emoji = "🌐"
        elif "Time Series" in title:
            emoji = "📈"
        elif "Converter" in title:
            emoji = "🔧"
        elif "Task Manager" in title:
            emoji = "📅"
        elif "SEO" in title:
            emoji = "🔍"

        # Display project title and description
        st.markdown(f"### {emoji} {title}")
        st.write(project["description"])
        st.write(f"**Technologies:** {', '.join(project['technologies'])}")

        # Project repository and app links
        col_links = st.columns(2)
        with col_links[0]:
            if project["repo_link"]:
                st.markdown(f"[🔗 View Code]({project['repo_link']})", unsafe_allow_html=True)
        with col_links[1]:
            if project["app_link"]:
                st.markdown(f"[🎨 View App]({project['app_link']})", unsafe_allow_html=True)

    st.markdown("---")

# ✅ Contact footer section
st.markdown("""
---
📧 **Contact me:** [markson.umesi@gmail.com](mailto:markson.umesi@gmail.com)
""")

