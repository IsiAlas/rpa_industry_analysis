import streamlit as st
from bs4 import BeautifulSoup
import requests

style_1 = "<style>[data-testid=column]:nth-of-type(1) [data-testid=stVerticalBlock]{gap: 0rem;}</style>"
style_2 = "<style>[data-testid=column]:nth-of-type(2) [data-testid=stVerticalBlock]{gap: 0rem;}</style>"

#______SIDEBAR______
st.sidebar.header('General Info')
st.sidebar.markdown('''
- [Website](https://www.blueprism.com/)
- [LinkedIn](https://www.linkedin.com/company/blue-prism-limited/?trk=tyah)
- [Crunchbase](https://www.crunchbase.com/organization/blue-prism-group-plc)''')

#______HEADER_______
blue_prism_logo= "https://upload.wikimedia.org/wikipedia/commons/thumb/6/\
6e/Blue_Prism_logo.svg/1200px-Blue_Prism_logo.svg.png"
st.image(blue_prism_logo, width=400)

#______ABOUT______
st.markdown("#### About")

st.markdown("Blue Prism invented the term Robotic Process Automation. \
Their software platform enables business operations to be agile and cost \
effective through rapid automation of manual, rules based, back office \
administrative processes, reducing cost and improving accuracy by creating \
a “digital workforce”.")

#______TOP CONTAINER______
with st.container():
    col1, col2 = st.columns(2, gap='large')

    with col1:
        st.markdown("##")
        ceo_pic = "https://global-uploads.webflow.com/5e84a58faf7d5a205d3796b7/6099f0408d5fe93b21471749_William%20Stone_Easy-Resize.com.jpg"
        st.image(ceo_pic, caption='William C. Stone, founder, chairman and chief executive officer of SS&C Technologies', width=250)

    with col2:
        st.write("##")
        st.markdown("🏛️ **Year Founded:** 2001")
        st.write("#")
        st.markdown("👔 **Acquired by:** SS&C")
        st.write("#")
        st.markdown("👫 **Number of Employees:** 1,004")
        st.write("#")
        st.markdown("💰**Total Funding:** $182,9M")
        st.write("#")
        st.markdown("🔠 **Latest Funding Series:** Post-IPO Equity")
        st.write("#")
        st.markdown("**🦄  Latest Known Valuation:** $1.1B before M&A (2021)")

#______MIDDLE CONTAINER______
st.write("##")

with st.container():
    col1, col2 = st.columns(2, gap='large')

    with col1:
        st.markdown("##### 🧑‍💼Investors")
        st.markdown('##')
        st.markdown(" * Clydesdale Bank, Yorkshire Bank, Endeavour Ventures, Enterprise Ventures, and more")

    with col2:
        st.markdown(style_2,unsafe_allow_html=True)
        st.markdown("##### 💸Pricing")
        st.markdown('##')
        st.markdown("* Free Triel & Quote")
        st.markdown("* Pay-as-you go option")
        st.markdown("* Minimum price to get started: USD 1.100 per month")


#______BOTTOM CONTAINER______
# st.write("##")

# with st.container():
#     col1, col2 = st.columns(2, gap='large')
#     st.markdown("""
#     <style>
#     [data-testid=column]:nth-of-type(1) [data-testid=stVerticalBlock]{
#         gap: 0rem;
#     }
#     </style>
#     """,unsafe_allow_html=True)

#     with col1:
#         st.markdown("##### 🌏 Locations")
#         st.markdown('##')
#         st.markdown("")
