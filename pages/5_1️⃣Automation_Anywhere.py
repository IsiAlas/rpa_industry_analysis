import streamlit as st
from bs4 import BeautifulSoup
import requests

style_1 = "<style>[data-testid=column]:nth-of-type(1) [data-testid=stVerticalBlock]{gap: 0rem;}</style>"
style_2 = "<style>[data-testid=column]:nth-of-type(2) [data-testid=stVerticalBlock]{gap: 0rem;}</style>"

#______SIDEBAR______
st.sidebar.header('General Info')
st.sidebar.markdown('''
- [Website](https://www.automationanywhere.com/)
- [LinkedIn](https://www.linkedin.com/company/automation-anywhere/)
- [Crunchbase](https://www.crunchbase.com/organization/automation-anywhere)''')

#______HEADER_______
automation_anywhere_logo = "https://www.globalteksecurity.com/wp-cont\
ent/uploads/2018/03/automation-anywhere-logo-corporate-two-line-lg.png"
st.image(automation_anywhere_logo, width=400)

#______ABOUT______
st.markdown("#### About")

st.markdown("Automation Anywhere is a global leader in Robotic Process Automation \
(RPA), empowering customers to automate end-to-end business processes with \
intelligent software bots – AI-powered digital workers that perform repetitive \
and manual tasks, resulting in dramatic productivity gains, optimized customer \
experience and more engaged employees.")

#______TOP CONTAINER______
with st.container():
    col1, col2 = st.columns(2, gap='large')

    with col1:
        st.markdown("##")
        ceo_pic = "https://www.automationanywhere.com/sites/default/files/images/aboutus/team-mihir-shukla_en.jpg"
        st.image(ceo_pic, caption='Mihir Shukla, Co-founder and CEO', width=200)

    with col2:
        st.write("##")
        st.markdown("🏛️ **Year Founded:** 2003")
        st.write("#")
        st.markdown("👫 **Number of Employees:** 2,917")
        st.write("#")
        st.markdown("💰**Total Funding:** $1 B")
        st.write("#")
        st.markdown("🔠 **Latest Funding Series:** Debt Financing")
        st.write("#")
        st.markdown("**🦄  Latest Known Valuation:** $6.8 billion (2022)")


#______MIDDLE CONTAINER______
st.write("##")

with st.container():
    col1, col2 = st.columns(2, gap='small')
    st.markdown("""
    <style>
    [data-testid=column]:nth-of-type(1) [data-testid=stVerticalBlock]{
        gap: 0rem;
    }
    </style>
    """,unsafe_allow_html=True)

    with col1:
        st.markdown("##### 🧑‍💼Investors")
        st.markdown('##')
        st.markdown(" * Hercules Capital, SVB Capital, Silicon Valley Bank, Veligera Capital, and more")

    with col2:
        st.markdown("##### 💸Pricing")
        st.markdown(style_2,unsafe_allow_html=True)
        st.markdown('##')
        st.markdown("* Quote")
        st.markdown("* Subscription Based")
        st.markdown("* Minimum price to get started: USD 750 per month")

#______BOTTOM CONTAINER______
