import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Emad Khaled", layout="wide", page_icon="📈")

# --- PROFESSIONAL CSS ---
st.markdown("""
<style>
    .stApp {
        background-color: #ffffff;
    }
    
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
        max-width: 1200px;
        margin: auto;
    }
    
    header {visibility: hidden;}

    .professional-card {
        background-color: #f5f8fa;
        padding: 25px;
        border-radius: 10px;
        border-left: 5px solid #1E90FF;
        margin: 15px 0;
        line-height: 1.7;
        color: #333333;
    }

    .metric-box {
        background: linear-gradient(135deg, #f5f8fa 0%, #e8f2ff 100%);
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #1E90FF;
        text-align: center;
        margin: 10px 0;
        color: #1a1a1a;
    }

    .metric-box h3 {
        color: #1E90FF;
        margin: 0;
        font-size: 32px;
    }

    .section-header {
        color: #1E90FF;
        border-bottom: 3px solid #1E90FF;
        padding-bottom: 12px;
        margin-top: 30px;
        margin-bottom: 20px;
        font-weight: 700;
    }

    .skill-tag {
        display: inline-block;
        background-color: #e8f2ff;
        color: #1E90FF;
        padding: 8px 16px;
        border-radius: 20px;
        margin: 5px 5px 5px 0;
        font-size: 13px;
        font-weight: 600;
        border: 1px solid #1E90FF;
    }

    .experience-item {
        background-color: #f5f8fa;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #1E90FF;
        margin: 15px 0;
        color: #333333;
    }

    .experience-item h4 {
        margin: 0 0 5px 0;
        color: #1E90FF;
        font-weight: 700;
    }

    .experience-item p {
        margin: 5px 0;
        color: #555555;
        font-size: 14px;
    }

    h1, h2, h3 {
        color: #1a1a1a !important;
    }

    h1 {
        color: #1E90FF !important;
        font-weight: 700;
    }

    hr {
        border-color: #d0d0d0 !important;
    }

    div.stButton > button {
        background-color: #1E90FF !important;
        border: 1px solid #1E90FF !important;
        color: white !important;
        font-weight: 600 !important;
        border-radius: 6px !important;
    }

    div.stButton > button:hover {
        background-color: #0d6fb8 !important;
        border: 1px solid #0d6fb8 !important;
    }
    
    .project-card {
        background-color: #f5f8fa;
        border-radius: 12px;
        padding: 20px;
        margin: 15px 0;
        border: 1px solid #e0e0e0;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    
    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    }
    
    .project-title {
        color: #1E90FF;
        font-size: 20px;
        font-weight: 700;
        margin-bottom: 10px;
    }
    
    .project-description {
        color: #555555;
        font-size: 14px;
        line-height: 1.6;
        margin-bottom: 15px;
    }
    
    .project-link {
        display: inline-block;
        background-color: #1E90FF;
        color: white !important;
        padding: 8px 16px;
        border-radius: 6px;
        text-decoration: none;
        font-size: 13px;
        font-weight: 600;
        margin-right: 10px;
        margin-top: 5px;
    }
    
    .project-link:hover {
        background-color: #0d6fb8;
    }
    
    .project-link-secondary {
        display: inline-block;
        background-color: white;
        color: #1E90FF !important;
        padding: 8px 16px;
        border-radius: 6px;
        text-decoration: none;
        font-size: 13px;
        font-weight: 600;
        border: 1px solid #1E90FF;
        margin-top: 5px;
    }
    
    .project-link-secondary:hover {
        background-color: #e8f2ff;
    }
</style>
""", unsafe_allow_html=True)

# --- PROJECTS DATA ---
PROJECTS = [
    {
        "title": "Crypto Market Analysis",
        "subtitle": "Extreme Event Detection & Statistics",
        "description": "Analyzed Bitcoin, Ethereum, and Dogecoin trading data (2013-2021) to identify extreme market events using z-score analysis. Detected 53 anomalous trading days and found that Ethereum outperformed Bitcoin with a Sharpe ratio of 0.090 vs 0.055.",
        "image": "CRYPTO MARKET ANALYSIS.png",
        "tags": ["Python", "SQL", "Pandas", "Matplotlib", "Statistics"],
        "github": "https://github.com/emad-khaled-dev/crypto-market-analysis",
        "demo": "https://emad-khaled-dev.github.io/crypto-market-analysis/notebooks/analysis.html"
    },
    {
        "title": "Israeli Tech M&A Screener",
        "subtitle": "Quantitative Valuation & Monte Carlo DCF",
        "description": "Built a screening tool to identify undervalued Israeli tech companies using regression analysis on EV/Revenue multiples vs growth rates. Includes Monte Carlo DCF simulation with 1,000 iterations to estimate intrinsic value ranges.",
        "image": "ISRAELI TECH M&A SCREENER.png",
        "tags": ["Python", "yfinance", "Scikit-learn", "Monte Carlo", "Finance"],
        "github": "https://github.com/emad-khaled-dev/Quant-MA-Screener-Israel",
        "demo": "https://emad-khaled-dev.github.io/Quant-MA-Screener-Israel/"
    }
]

# --- Navigation state ---
if 'page' not in st.session_state:
    st.session_state.page = "Home"

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("Home", use_container_width=True):
        st.session_state.page = "Home"
with col2:
    if st.button("About", use_container_width=True):
        st.session_state.page = "About"
with col3:
    if st.button("Projects", use_container_width=True):
        st.session_state.page = "Projects"
with col4:
    if st.button("Education", use_container_width=True):
        st.session_state.page = "Education"
with col5:
    if st.button("Contact", use_container_width=True):
        st.session_state.page = "Contact"

st.divider()
# --- PAGE: HOME ---
if st.session_state.page == "Home":

    st.title("Emad Khaled")
    st.subheader("Computer Science & Statistics Student")

    st.markdown("""
    <div class="professional-card">
        <p>
        Third-year student at Tel Aviv University pursuing a dual degree in Computer Science and Statistics. 
        Experienced in data analysis, statistical modeling, and software development.
        </p>
        <p>
        <b>Looking for:</b> Student position or internship in Business Intelligence, Data Analysis, Software Development or other tech roles.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col_a, col_b, col_c = st.columns(3)

    with col_a:
        st.markdown(f"""
        <div class="metric-box">
            <h3>{"3+"}</h3>
            <p>Projects</p>
        </div>
        """, unsafe_allow_html=True)

    with col_b:
        st.markdown("""
        <div class="metric-box">
            <h3>85.6</h3>
            <p>CS GPA</p>
        </div>
        """, unsafe_allow_html=True)

    with col_c:
        st.markdown("""
        <div class="metric-box">
            <h3>2027</h3>
            <p>Graduation</p>
        </div>
        """, unsafe_allow_html=True)


# --- PAGE: ABOUT ---
elif st.session_state.page == "About":
    st.title("About Me")
    
    st.markdown("""
    <div class="professional-card">
    <h3>Overview</h3>
    <p>I'm a Computer Science and Statistics student at Tel Aviv University with hands-on experience in data collection, 
    analysis, and software development. I enjoy working with data - whether it's analyzing market trends, 
    building clustering algorithms, or creating visualizations that tell a story.</p>
    <p>I'm looking for a student position or internship where I can apply my skills in Business Intelligence, Data Analysis, 
    Software Development or any tech-related role.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<h3 class="section-header">Technical Skills</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Programming**")
        skills_prog = ["Python", "C", "Java", "R", "SQL"]
        for skill in skills_prog:
            st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Tools & Environment**")
        skills_tools = ["Git", "Linux", "Docker", "SSH", "Excel"]
        for skill in skills_tools:
            st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("**Data & Analysis**")
        skills_data = ["Pandas", "NumPy", "Matplotlib", "Scikit-learn", "Statistical Modeling"]
        for skill in skills_data:
            st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Other**")
        skills_other = ["Python C API", "Data Visualization", "Machine Learning"]
        for skill in skills_other:
            st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)
    
    st.markdown('<h3 class="section-header">Languages</h3>', unsafe_allow_html=True)
    
    languages = ["Hebrew", "English", "Arabic", "Russian"]
    for lang in languages:
        st.markdown(f'<span class="skill-tag">{lang}</span>', unsafe_allow_html=True)

# --- PAGE: PROJECTS ---
elif st.session_state.page == "Projects":
    st.title("Projects")
    
    st.markdown("""
    <p style="color: #555; font-size: 16px; margin-bottom: 30px;">
    Here are some of my data analysis and programming projects. Click on the links to view the code or live demos.
    </p>
    """, unsafe_allow_html=True)
    
    for project in PROJECTS:
        st.markdown("---")
        
        col1, col2 = st.columns([1.7, 1.3], gap="large")
        
        with col1:
            try:
                st.image(project["image"], use_container_width=True)
            except:
                st.info(f"Image: {project['image']}")
        
        with col2:
            st.markdown(f'<div class="project-title">{project["title"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<p style="color: #1E90FF; font-size: 14px; margin-top: -10px;">{project["subtitle"]}</p>', unsafe_allow_html=True)
            st.markdown(f'<p class="project-description">{project["description"]}</p>', unsafe_allow_html=True)
            
            tags_html = ""
            for tag in project["tags"]:
                tags_html += f'<span class="skill-tag">{tag}</span>'
            st.markdown(tags_html, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            links_html = f'''
            <a href="{project["github"]}" target="_blank" class="project-link">📁 GitHub</a>
            <a href="{project["demo"]}" target="_blank" class="project-link-secondary">🔗 Live Demo</a>
            '''
            st.markdown(links_html, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("""
    <p style="color: #888; font-size: 14px; text-align: center; margin-top: 30px;">
    More projects coming soon...
    </p>
    """, unsafe_allow_html=True)

# --- PAGE: EDUCATION ---
elif st.session_state.page == "Education":
    st.title("Education")
    
    st.markdown("""
    <div class="experience-item">
    <h4>Tel Aviv University</h4>
    <p><b>B.Sc. Computer Science & Statistics (Dual Degree)</b></p>
    <p>Oct 2022 - July 2027 (Expected)</p>
    <p><b>GPA:</b> Computer Science: 86.4 | Statistics: 81.1</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<h3 class="section-header">Relevant Coursework</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Computer Science**
        - Extended Intro to Computer Science
        - Data Structures
        - Algorithms
        - Software Project (C + Python API)
        - Discrete Mathematics
        """)
    
    with col2:
        st.markdown("""
        **Statistics**
        - Probability Theory
        - Statistical Theory
        - Statistical Models
        - Statistical Computing (R)
        - Introduction to Statistical Learning
        - Operations Research
        """)
    
    st.markdown('<h3 class="section-header">Experience</h3>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="experience-item">
    <h4>Campus Tree Surveyor</h4>
    <p><b>Tel Aviv University</b> | March 2025 - August 2025</p>
    <p>Conducted field surveys of campus trees, collecting data on species, locations, and conditions. 
    Entered data into the university's digital databases for documentation and ongoing management. 
    Part of a project to develop a digital app for mapping trees on campus.</p>
    </div>
    """, unsafe_allow_html=True)

# --- PAGE: CONTACT ---
elif st.session_state.page == "Contact":
    st.title("Contact")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="professional-card">
        <b>📧 Email</b><br>
        <a href="mailto:emad.kha3@gmail.com">emad.kha3@gmail.com</a>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="professional-card">
        <b>💼 LinkedIn</b><br>
        <a href="https://www.linkedin.com/in/emad-khaled-6b6528257/" target="_blank">linkedin.com/in/emad-khaled</a>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="professional-card">
        <b>🐙 GitHub</b><br>
        <a href="https://github.com/emad-khaled-dev" target="_blank">github.com/emad-khaled-dev</a>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    st.markdown("""
    <div class="professional-card">
    <p>Open to student positions, internships, and project collaborations. Feel free to reach out!</p>
    </div>

    """, unsafe_allow_html=True)




