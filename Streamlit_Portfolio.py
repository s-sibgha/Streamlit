

import streamlit as st

# ---------- Page Configuration ----------
st.set_page_config(page_title="My Portfolio", page_icon="📊", layout="centered")

# ---------- Main Title ----------
st.title("👋 Welcome to My Portfolio")

# ---------- About Me ----------
st.markdown("""
## 🙋‍♀️ Hello, I'm Sibgha
I'm currently pursuing **MSc in Data Science** and exploring the world of data, analytics, and machine learning.  
This portfolio showcases my early learning journey and hands-on projects.
""")

# ---------- Skills ----------
st.markdown("### 🔹 Skills")
st.markdown("""
- 📊 **MS Word, PowerPoint, Excel**  
- 💻 **JupyterLab, Streamlit Basics**  
- 🐍 **Python Basics, Data Entry, Typing**  
""")
st.markdown("###")
# ---------- Projects Section ----
# ---------- FEATURED PROJECT ----------
st.subheader("🚀 Featured Project")

st.markdown("## 📊 Hybrid AI Student Performance Analyzer")

st.write("""
An intelligent AI-powered web application that predicts student performance 
using a hybrid approach combining rule-based logic and machine learning.

✔ Confidence-based decision system  
✔ Accuracy, Precision, Recall, F1-score  
✔ Confusion Matrix & Feature Importance  
✔ Interactive Streamlit dashboard  
""")

st.markdown("""
🔗 [🚀 Live App](https://student-performance-analyzer-ai-kucrjlyb2xdnalf6tpapex.streamlit.app/)  
💻 [📂 GitHub Repo](https://github.com/s-sibgha/student-performance-analyzer)
""")

st.markdown("---")

st.subheader("🏠 PMAY Housing Analysis")

st.image("https://raw.githubusercontent.com/s-sibgha/pmay-housing-insights/main/outputs/completion_rate_barplot.png", caption="State-wise Completion Rate Analysis")

st.write("""
A statistical data analysis project focused on evaluating housing scheme performance 
across states using normalization and visualization techniques.
""")

st.markdown("### 🔹 Key Highlights")
st.markdown("""
- Developed scale-independent performance analysis  
- Identified implementation gaps and inefficiencies  
- Performed comparative state-level analysis  
""")

st.markdown("🔗 [GitHub Repository](https://github.com/s-sibgha/pmay-housing-insights)")
st.markdown("📜 [Certificate](https://drive.google.com/file/d/1Dv_67XVYuSiNdFNGEoU9NUF9fy2cOmOT/view?usp=drivesdk)")



# 📂📙📘
#💼 Portfolio Projects	
col1, col2 = st.columns([1, 10])  # Adjust ratio as needed

with col1:
    st.image("https://img.icons8.com/fluency/96/survey.png", width=50)
     #st.markdown("<span style='font-size:40px;'>💼</span>",
    #unsafe_allow_html=True
with col2:
    st.subheader(" My Projects")

#st.markdown("###")  #Separator line

col1, col2 = st.columns([1, 10]) 

with col1:
    st.image("https://img.icons8.com/color/96/python--v1.png", width=50)

with col2:
    st.subheader("My Python Practice Notebooks")

st.markdown("---")   #Separator line

st.write("""
These notebooks demonstrate essential Python programming concepts through beginner-to-intermediate hands-on projects.  
Explore them to strengthen your core coding logic and real-world application understanding.
""")
# --- Custom CSS for Card and Button Styling ---
st.markdown("""
<style>
.card {
    background-color: #f5f5f5;
    padding: 20px;
    margin-bottom: 20px;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

a.button {
    display: inline-block;
    padding: 8px 18px;
    margin: 6px 0;
    font-size: 15px;
    font-weight: 600;
    color: white;
    text-align: center;
    background-color: #4CAF50;
    text-decoration: none;
    border-radius: 8px;
    transition: background-color 0.3s ease;
}
a.button:hover {
    background-color: #388E3C;
}
</style>
""", unsafe_allow_html=True)

# --- Columns layout for Notebooks ---🔹#388E3C; #007ACC:#4CAF50; #21867a;
col1, gap_col, col2 = st.columns([2, 0.5, 2])

with col1:
    #st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image("https://img.icons8.com/fluency/240/open-book.png",width=50)
    st.markdown("<div style='margin-top:5px;'></div>", unsafe_allow_html=True)
    st.markdown("### Notebook 1: Core Python Basics")
    st.markdown("<div style='margin-top:32px;'></div>", unsafe_allow_html=True)
    st.markdown('<a href="https://nbviewer.org/github/s-sibgha/Streamlit/blob/main/github_practice_notebook_1.html" class="button" target="_blank">📗 Open Notebook</a>', unsafe_allow_html=True)
    st.markdown("<br>",unsafe_allow_html=True)
    st.markdown("<div style='margin-top:0.01px;'></div>", unsafe_allow_html=True)
    st.write("🔍 **What’s inside:** Variable declaration, Expressions using arithmetic operators, Printing results, Simple input/output, Type conversion (int, float, str), Mini - Project Total Cost Calculator.")
    #st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>",unsafe_allow_html=True)

with col2:
    #st.markdown('<div class="card">', unsafe_allow_html=True)
    #st.image("https://img.icons8.com/color/96/flow-chart.png", width=50)
    st.markdown("<span style='font-size:40px;'>🧑‍💻</span>",
    unsafe_allow_html=True)
    st.markdown("### Notebook 2: Python Essentials: From Variables to Debugging")
    st.markdown('<a href="https://nbviewer.org/github/s-sibgha/Streamlit/blob/main/Github_Practice_Notebook_2.html" class="button" target="_blank">📘 Open Notebook</a>', unsafe_allow_html=True)
    #st.markdown("<br>",unsafe_allow_html=True)
    st.markdown("<div style='margin-top:40px;'></div>", unsafe_allow_html=True)
    st.write("🔍 **What’s inside:** Variables and Expressions, Data Types, Input and Output, Type Conversion, Comments, Debugging.")
    #st.markdown('</div>', unsafe_allow_html=True)


st.markdown("###")

col3, gap_col, col4 = st.columns([2, 0.5, 2])

with col3:
    #st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("<span style='font-size:40px;'>🧰</span>",
    unsafe_allow_html=True)
    st.markdown("### Notebook 3: Error Handling & Debugging")
    #st.markdown("<br>",unsafe_allow_html=True)
    st.markdown("<div style='margin-top:52px;'></div>", unsafe_allow_html=True)
    st.markdown('<a href="https://nbviewer.org/github/s-sibgha/Streamlit/blob/main/Github_Practice_Notebook_3.html" class="button" target="_blank">📙 Open Notebook</a>', unsafe_allow_html=True)
    st.markdown("<br>",unsafe_allow_html=True)
    st.write("🔍 **What’s inside:** Try-except blocks, Error messages, Debugging, Mini Project - Simple Tip Calculator.")
    #st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>",unsafe_allow_html=True)

with col4:
    #st.markdown('<div class="card">', unsafe_allow_html=True)
    #st.markdown("<img src='https://cdn-icons-png.flaticon.com/512/4259/4259760.png' width='50'/>", unsafe_allow_html=True)
    #st.markdown("<span style='font-size:40px;'>🌐</span>",
    #unsafe_allow_html=True)
    st.image("https://img.icons8.com/color/96/flow-chart.png", width=50)
    st.markdown("<div style='margin-top:0.5px;'></div>", unsafe_allow_html=True)
    st.markdown("### Notebook 4: Python Control Flow with Real-Life Applications")
    st.markdown("<div style='margin-top:0px;'></div>", unsafe_allow_html=True)
    st.markdown('<a href="https://nbviewer.org/github/s-sibgha/Streamlit/blob/main/Github_Practice_Notebook_4.ipynb" class="button" target="_blank">📓 Open Notebook</a>', unsafe_allow_html=True)
    st.markdown("<br>",unsafe_allow_html=True)
    st.write("🔍 **What’s inside:** if, elif, else, Comparison Operators, Boolean Logic, Nested Conditionals, try/except error handling, Real-life practice examples (age, grading, billing, form validation, etc.), Restauranat Bill Calculator with Discount.")
    #st.markdown('</div>', unsafe_allow_html=True)
st.markdown("###")

st.subheader("📄 My Research Project")
st.write("**Description:** This project explores the mathematical elegance of the Fibonacci sequence and how it connects to the Golden Ratio, with real-world applications in nature, architecture, and computer algorithms. It includes derivations, proofs, graphs, and golden ratio-based design aesthetics.")
st.write("You can request access to my detailed research project PDF using the link below:")
st.markdown(
    "[🔗 Request Access to Research Project (PDF)](https://drive.google.com/file/d/1ll_zBjP7HFD3vSDGpRZG_UQwIXrXX_TK/view?usp=drive_link)",
    unsafe_allow_html=True
)
st.markdown("###")

# ---------- Contact ----------
st.markdown("## 📬 Contact")
st.markdown("""
Feel free to reach out via email: **sibghaislam8@gmail.com**
""")
st.markdown("🔗 LinkedIn: https://linkedin.com/in/sibgha-3665a1377")
st.markdown("🌐 GitHub:   https://github.com/s-sibgha")

# ---------- Footer ----------
st.markdown("---")
st.markdown("© 2025 [Sibgha] | Made with Streamlit")
