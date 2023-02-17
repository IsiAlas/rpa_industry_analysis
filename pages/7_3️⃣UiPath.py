import streamlit as st


style_1 = "<style>[data-testid=column]:nth-of-type(1) [data-testid=stVerticalBlock]{gap: 0rem;}</style>"
style_2 = "<style>[data-testid=column]:nth-of-type(2) [data-testid=stVerticalBlock]{gap: 0rem;}</style>"

#______SIDEBAR______
st.sidebar.header('General Info')
st.sidebar.markdown('''
- [Website](https://www.uipath.com/)
- [LinkedIn](https://www.linkedin.com/company/uipath/)
- [Crunchbase](https://www.crunchbase.com/organization/uipath)''')

#______HEADER_______
ui_path_logo= "https://logos-download.com/wp-content/uploads/2021/01/Ui\
Path_Logo.png"
st.image(ui_path_logo, width=250)

#______ABOUT______
st.markdown("#### About")

st.markdown("UiPath designs and develops robotic process automation software. \
The platform offers foolproof development tools, automation of intricate \
processes, enhanced control, cloud and on-premise deployment, robust \
governance, and multiple robots on a single virtual machine.")

#______TOP CONTAINER______
with st.container():
    col1, col2 = st.columns(2, gap='large')

    with col1:
        st.markdown("##")
        ceo_pic = "https://uipath.com/cdn-cgi/image/format=auto/https:////images.ctfassets.net/5965pury2lcm/5CfWqFGZTNTAa9Qzs1P9Ln/1bf2918337b8d0355b2b4f00b986c084/daniel-dines-uipath-blog.jpeg"
        st.image(ceo_pic, caption='Daniel Dines, Co-founder and CEO', width=250)

    with col2:
        st.write("##")
        st.markdown("🏛️ **Year Founded:** 2005")
        st.write("#")
        st.markdown("👫 **Number of Employees:** 4,320")
        st.write("#")
        st.markdown("💰**Total Funding:** $2 B")
        st.write("#")
        st.markdown("🔠 **Latest Funding Series:** Series F")
        st.write("#")
        st.markdown("**🦄  Latest Known Valuation:** $10+ billion (2021)")

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
        st.markdown(" * Alkeon Capital, Tiger Global Management, Altimeter Capital, Sequoia Capital, Coatue and more")

    with col2:
        st.markdown("##### 💸Pricing")
        st.markdown(style_2,unsafe_allow_html=True)
        st.markdown('##')
        st.markdown("* Free Version & Quote")
        st.markdown("* Subscription Based")
        st.markdown("* Minimum price to get started: USD 420 per month")
