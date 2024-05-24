from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Meeran Muhammad Tabish"
PAGE_ICON = ":wave:"
NAME = "Meeran Muhammad Tabish"
DESCRIPTION = """
Software Developer with 2 years of experience in designing, developing, and maintaining high-quality software applications.
"""
EMAIL = "tabish.muhammad.m@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/mmuhammadtabish/",
    "GitHub": "https://github.com/thetabish",
}
PROJECTS = {
    "🏆 Property prices in the UK Dashboard - Analyzing trends in the purchase of properties across different regions in the UK (the link will take a few minutes to load)": "https://dash-app-portfolio-18p5.onrender.com",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.header("Experience & Qulifications")

# --- SKILLS ---
st.write('\n')
st.subheader("Skills")
st.write(
    """
- 👩‍💻 Programming:   Python, SQL, R, C++, C, Javascript, HTML, CSS,
- 📊 Data Visulization: PowerBI, Streamlit, Plotly Dash
- 📚 Tools and Frameworks: Pandas, NumPy, Tensorflow and Keras, sci-kit, PyVista, VTK, BeautifulSoup, Selenium, Git
- 🗄️ Databases:  Microsoft SQL Server, MySQL, PostgreSQL
- ☁️ Certifications: OVGU Cloud Winter School (Associate Google Cloud Engineer training)
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Wissenschaftliche Hilfskraft | Python - Web scraping and data analytics | DZHW Hannover, Germany**")
st.write("April 2024 - Present")
st.write(
    """
- ► Developing web scraping algorithms to systematically collect and analyze job postings from universities across Germany.
- ► Contributing to the creation of a comprehensive database for analyzing the quality and characteristics of professors in various German universities.
- ► Building a dashboard using Plotly Dash to implement a one-click solution to scrape job postings periodically
- ► Utilizing expertise in Python libraries like Selenium and BeautifulSoup to implement efficient web scraping algorithms and Sci-kit learn and tensorflow to implement machine learning algorithms on the scraped data.
"""
)

st.write("🚧", "**Wissenschaftliche Hilfskraft | Python - Data processing and analytics |  Otto-von-Guericke University Magdeburg, Germany**")
st.write("March 2024 (1 month)")
st.write(
    """
- ► Developed a specialized tool to streamline the processing, manipulation, and conversion of JSON files pertaining to BMW’s manufacturing processes.
- ► The tool converts the JSON file to other formats, enhancing data accessibility and compatibility. Built a dashboard using Streamlit to implement a one-click solution.
- ► Demonstrated proficiency in Python libraries like pandas and streamlit to create efficient and user-friendly solutions.
"""
)

# --- JOB 2
st.write("🚧", "**Wissenschaftliche Hilfskraft | Python - Data analytics and visualization | Otto-von-Guericke University Magdeburg, Germany**")
st.write("July 2023 - November 2023 (5 months)")
st.write(
    """
- ► Engineered a transformative data analytics tool for Volkswagen, resulting in a 20% workflow improvement. Applied advanced data preprocessing techniques for valuable insights.
- ► Developed a dynamic data analytics dashboard with 3D visualization using Plotly Dash, PyVista, Javascript, CSS, VTK, Pandas.
- ► Proactively engaged stakeholders, ensuring seamless collaboration. Known for flexibility in adapting to evolving project requirements and  commitment to delivering high-quality code

"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Application Development Analyst | Software Engineer | Accenture India**")
st.write("February 2021 - September 2022 (1 year and 7 months)")
st.write(
    """
- ► Crafted efficient data queries using SQL, enhancing data workflows.
- ► Utilized Power BI and Excel for KPI tracking reports.
- ► Demonstrated exceptional performance with a significant organizational impact, leading to an early promotion to Analyst at Accenture. Improved ticket resolution of the team with a 20% faster turnaround time.
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
