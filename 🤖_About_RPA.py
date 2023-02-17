import altair as alt
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from PIL import Image
import requests
import streamlit as st

# Tab Configuration
st.set_page_config(page_title="Robotic Process Automation", page_icon="🤖", layout="wide")

style_1 = "<style>[data-testid=column]:nth-of-type(1) [data-testid=stVerticalBlock]{gap: 0rem;}</style>"
style_2 = "<style>[data-testid=column]:nth-of-type(2) [data-testid=stVerticalBlock]{gap: 0rem;}</style>"

# Header
st.markdown("<h3 style='text-align: center; font-size:40px; color:#EE103F; \
'>🤖 Robotic Process Automation</h3>", unsafe_allow_html=True)
st.markdown("")

#____HISTORY OF RPA____
st.markdown("##### **:blue[History of RPA]**")
st.markdown("It dates to the early 2000's, and depended on technology \
developed on the 50's and 60's such as Artificial Intelligence, \
Screen Scraping and Workflow Automation.")
st.markdown("")

#____WHAT IS RPA?____
st.markdown("##### **:blue[What is RPA?]**")
st.markdown("According Digital Workforce, RPA is \
a 'technology that utilizes pre-defined business logic, established rules \
and structured data to automate business processes. Software robots built \
on RPA are able to capture and interpret applications for processing a \
transaction, manipulating data, triggering responses and communicating \
with other digital systems. RPA is the ideal \
technology for many labour-intensive knowledge work. It handles repetitive, \
and rule-based, large volume tasks particularly well.'")
st.markdown("")

#____RPA BUSINESS BENEFITS____
st.markdown("##### **:blue[RPA Business Benefits]**")
with st.container():
    col1, col2 = st.columns(2, gap='large')
    st.markdown(style_1,unsafe_allow_html=True)
    with col1:
        st.markdown("* Ends repetitive digital tasks")
        st.markdown("* Reduces manual errors")
        st.markdown("* Identifies process and tasks improvement opportunities")
        st.markdown("* Leverages a company’s existing infrastructure without causing disruption to underlying systems")
    st.markdown(style_2,unsafe_allow_html=True)
    with col2:
        st.markdown("* Allows fast and cost-efficient digital transformation (rapid return on investment)")
        st.markdown("* Boosts employee satisfaction and productivity")
        st.markdown("* Scalable")
        st.markdown("* Improves compliance")
st.markdown("")

#____RPA TECHNOLOGY____
st.markdown("##### **:blue[Technology that RPA uses]**")
with st.container():
    col1, col2, col3 = st.columns(3, gap='large')
    st.markdown(style_1, unsafe_allow_html=True)
    with col1:
        st.markdown("**1. User Interface Automation**")
        st.write("##")
        st.markdown("*Provides programmatic access to most user interface (UI)\
        elements on the desktop, enabling assistive technology products such\
        a screen readers to provide information about the UI to end users and\
        to manipulate the UI by means other than standard input.*")

    with col2:
        st.markdown("**2. Optical character recognition (OCR)**")
        st.write("##")
        st.markdown("*OCR systems use a combination of hardware and software \
        to convert physical, printed documents into machine-readable text.*")

    with col3:
        st.markdown("**3. Natural Language Processing (NLP)**")
        st.markdown("*Gives computers the ability to understand text and \
        spoken words in much the same way human beings can.*")










# st.write("")
# with st.container():
#     st.markdown("#### **Information Tracked:**")
#     col1, col2, col3 = st.columns(3, gap='small')


#     with col1:
#         st.markdown("🏢 General Company Overview ")
#         st.markdown("👫 N° Employees")
#         st.markdown("🌏 Locations")

#     with col2:
#         st.markdown("💰 Total Funding")
#         st.markdown("🧑‍💼 Investors")
#         st.markdown("🔠 Latest Funding Series")

#     with col3:
#         st.markdown("💸 Pricing")
#         st.markdown("💻 Features")
#         st.markdown("📰 Latest News")





#col1, col2, col3 = st.columns(3, gap='medium')


#st.sidebar.write("""## Top Competitors""")
#st.sidebar.selectbox("Pick a competitor", ['ClickUp', 'Airtable', 'Wrike'])


#st.sidebar.write("""## Pick Information to visualize""")
#st.sidebar.checkbox('General')
#st.sidebar.checkbox('Pricing')
#st.sidebar.checkbox('Total Funding')
#st.sidebar.checkbox('Investors')
#st.sidebar.checkbox('Latest News')
#st.sidebar.checkbox('N° Employees')
#st.sidebar.checkbox('Latest Funding Series')
#st.sidebar.checkbox('Features')
#st.sidebar.checkbox('')




#def app():
    # title of the app
 #   st.sidebar.markdown("Quantitative Stats")
    # Add a sidebar
  #  st.sidebar.subheader("Graph Settings")
