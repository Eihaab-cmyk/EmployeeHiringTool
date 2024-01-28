import streamlit
from predict_page import show_predict_page
from explore_page import show_explore_page
from skill_assessment_page import show_skill_assessment_page
from chat import show_chatbot_page
from rh import show_resume_highlight_page

page = streamlit.sidebar.selectbox("Select option", ("Predict", "Explore", "Skill Assessment", "HireAssist", "Resume Highlight"))

if page == "Predict":
    show_predict_page()
elif page == "Explore":
    show_explore_page()
elif page == "Skill Assessment":
    show_skill_assessment_page()
elif page == "HireAssist":
    show_chatbot_page()
elif page == "Resume Highlight":
    show_resume_highlight_page()