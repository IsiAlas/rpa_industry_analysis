import numpy as np
import pandas as pd
from PIL import Image
import streamlit as st

st.set_page_config(layout="wide")

#______KEY PLAYERS_____

with st.container():
    st.markdown("<h3 style='text-align: center; font-size:40px; color:#EE103F; \
'>Key Players</h3>", unsafe_allow_html=True)
    st.write("#")

    st.markdown("We will evaluate the providers of RPA software products chosen by Gartner \
in the Magic Quadrant.")
    st.markdown("")

    col1, col2, col3, col4 = st.columns(4, gap='large')
    with col1:
        automation_anywhere_logo = "https://www.globalteksecurity.com/wp-cont\
ent/uploads/2018/03/automation-anywhere-logo-corporate-two-line-lg.png"
        st.image(automation_anywhere_logo, caption='Automation Anywhere', width=150)
    with col2:
        st.markdown("")
        blue_prism_logo= "https://upload.wikimedia.org/wikipedia/commons/thumb/6/\
6e/Blue_Prism_logo.svg/1200px-Blue_Prism_logo.svg.png"
        st.image(blue_prism_logo, caption='Blue Prism', width=150)
    with col3:
        ui_path_logo= "https://logos-download.com/wp-content/uploads/2021/01/Ui\
Path_Logo.png"
        st.image(ui_path_logo, caption='UiPath', width=150)
    with col4:
        st.markdown("")
        nice_logo= "https://upload.wikimedia.org/wikipedia/commons/2/2a/Nice_Logo_2.svg"
        st.image(nice_logo, caption='Nice Systems', width=100)

    col1, col2, col3, col4 = st.columns(4, gap='large')
    with col1:
         microsoft_logo = "https://evergreenleadership.com/wp-content/uploads/2019/05/microsoft-logo-png-transparent-20.png"
         st.image(microsoft_logo, caption='Microsoft', width=150)
    with col2:
        st.markdown("")
        workfusion_logo= "https://upload.wikimedia.org/wikipedia/commons/3/34/Workfusion_2020_Logo.png"
        st.image(workfusion_logo, caption='WorkFusion', width=170)
    with col3:
        cyclone_logo= "data/cyclone_logo.png"
        st.image(cyclone_logo, caption='Cyclone Robotics', width=150)
    with col4:
        st.markdown("")
        samsung_logo = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Samsung_SDS_logo.svg/2560px-Samsung_SDS_logo.svg.png"
        st.image(samsung_logo, caption='Samsung', width=200)


    col1, col2, col3, col4 = st.columns(4, gap='large')
    with col1:
        nintex_logo = "https://www.nintex.com/wp-content/uploads/2018/07/nintex-logo-dark.png"
        st.image(nintex_logo, caption='Nintex', width=170)
    with col2:
        ibm_logo= "https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/IBM_logo.svg/2560px-IBM_logo.svg.png"
        st.image(ibm_logo, caption='IBM', width=100)
    with col3:
        laiye_logo = "https://mediaserver.responsesource.com/press-release/137281/Laiye+Logo.png"
        st.image(laiye_logo, caption='Laiye', width=120)
    with col4:
        pegasystems_logo = "https://companieslogo.com/img/orig/PEGA_BIG-35db3335.png?t=1597250644"
        st.image(pegasystems_logo, caption='Pegasystems', width=150)


    col1, col2, col3, col4 = st.columns(4, gap='large')
    with col1:
        sap_logo= "https://logos-download.com/wp-content/uploads/2016/08/SAP_logo.png"
        st.image(sap_logo, caption='SAP', width=100)
    with col2:
        appian_logo="https://logos-download.com/wp-content/uploads/2022/01/Appian_Logo.png"
        st.image(appian_logo, caption='Appian', width=100)
    with col3:
        salesforce_logo = "https://www.seraphscience.com/wp-content/uploads/2018/06/logo-salesforce-png-454.png"
        st.image(salesforce_logo, caption='Salesforce', width=150)
    with col4:
        st.markdown("")

st.markdown("")
st.markdown("")

#______Magic Quadrant______

st.markdown("<h3 style='text-align: lefts; font-size:28px; color:#EE103F; \
'>Magic Quadrant for Robotic Process Automation</h3>", unsafe_allow_html=True)

st.markdown("")

image_1 = Image.open('data/rpa_quadrant.png')

st.image(image_1, caption='Source: Gartner')

with st.container():
    st.markdown("<h3 style='text-align: lefts; font-size:24px; color:#808080; \
'>Evaluation Criteria</h3>", unsafe_allow_html=True)
    st.markdown("The two axes of the Magic cuadrant are: Ability to Execute and Completeness of Vision.")
    col1, col2 = st.columns(2, gap='large')
    with col1:
        st.markdown("**:blue[Ability to Execute]**")
        st.markdown("Gartner evaluates how well processes, systems, methods and \
procedures enable vendors to be competitive, efficient and effective.")
        st.caption("Criteria: Product or Service, Overall Viability, Sales Execution/Pricing, \
Market Responsiveness/Record, Marketing Execution, Customer Experience, Operations. ")

    with col2:
        st.markdown("**:blue[Completeness of Vision]**")
        st.markdown("Gartner evaluates the level of understanding of the RPA market’s \
present and future outlook and how it aligns with Gartner’s vision.")
        st.caption("Market Understanding, Sales Strategy, Offering (Product) Strategy, \
Business Model, Vertical/Industry Strategy, Innovation, Geographic Strategy")

st.markdown("")

with st.container():
    st.markdown("<h3 style='text-align: lefts; font-size:24px; color:#808080; \
'>Quadrant Descriptions</h3>", unsafe_allow_html=True)

col1, col2 =  st.columns(2, gap="large")
with col1:
    st.markdown("**:green[Leader]**")
    st.markdown("Vendors that have an insightful understanding of a market, a \
reliable track record, the power to influence a market’s direction, and an \
ability to attract and retain customers")
    with col2:
        st.markdown("**:green[Challengers]**")
        st.markdown("Vendors that excel at attracting a large customer base,\
but are often limited to one part of the market.")

col1, col2 =  st.columns(2, gap="large")
with col1:
    st.markdown("**:green[Visionaries]**")
    st.markdown("Vendors that are  market’s innovators. They propel a market \
forward by responding to emerging customer demands and offering \
customers new opportunities to excel.")
with col2:
    st.markdown("**:green[Niche Players]**")
    st.markdown("Vendors that typically specialize in one vertical or functional \
area, or have a strong product that is limited to one part of the market.")

st.markdown("")
#___REVENUE & VALUATION TABLE__

st.markdown("<h3 style='text-align: left; font-size:28px; color:#EE103F; \
'>Revenue & Valuation</h3>", unsafe_allow_html=True)

st.markdown("The following table presents the 2022 revenue and latest valuation of \
the RPA companies present in the Gartner RPA Magic Quadrant. The revenue is not \
necessarily exclusive of the RPA software solution, but could include RPA service solution revenue.")
st.markdown("For non megavendors we also calculated the revenue per employee.")


df_1 = pd.read_csv("data/rpa_revenue_and_valuation.csv")
st.write(df_1)
st.caption("*Employee number source is each company's Linkedin profile in February 2023")

#______STRENGTHS & WEAKNESESS______

st.markdown("")
st.markdown("<h3 style='text-align: left; font-size:28px; color:#EE103F; \
'>Other Company/Product Information</h3>", unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Product Name", "Strengths", "Weaknesses", "Feature Comparison", "Pricing","Customer Base", "Operations"])

with tab1:
   st.header("RPA Product Name")
   df_2 = pd.read_csv("data/rpa_product_name.cvs")
   st.write(df_2)

with tab2:
   st.header("Strengths")
   df_3 = pd.read_csv("data/rpa_strengths.csv")
   st.dataframe(df_3)

with tab3:
   st.header("Weaknesses")
   df_4 = pd.read_csv("data/rpa_weaknesses.csv")
   st.dataframe(df_4)

with tab4:
    st.header("Feature Comparison")
    image_2 = Image.open("data/feature_comparison.png")
    st.image(image_2)

with tab5:
    st.header("Pricing")
    image_4= Image.open('data/pricing.png')
    st.image(image_4)

with tab6:
   st.header("Customer Base")
   image_3 = Image.open('data/customer_base_2.png')
   st.image(image_3)

with tab7:
   st.header("Operations")
   df_4 = pd.read_csv("data/rpa_operations.csv")
   st.dataframe(df_4)














