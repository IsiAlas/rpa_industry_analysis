import altair as alt
import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")


style_1 = "<style>[data-testid=column]:nth-of-type(1) [data-testid=stVerticalBlock]{gap: 0rem;}</style>"
style_2 = "<style>[data-testid=column]:nth-of-type(2) [data-testid=stVerticalBlock]{gap: 0rem;}</style>"


###_____MARKET SIZE___###

st.markdown("<h3 style='text-align: left; font-size:40px; color:#EE103F; \
'>I. Market Size</h3>", unsafe_allow_html=True)

source = pd.DataFrame({
"Market Size (in billions USD)": [10.01, 12.35, 15.24, 18.81, 23.21, 28.64, 35.34, 43.61],
"Year": ['2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029']
})

bar_chart = alt.Chart(source).mark_bar(line={'color':'darkgreen'}).encode(
    x="Year",
    y="Market Size (in billions USD)"
).interactive()

st.markdown("<h3 style='text-align: center; color:white;'>Expected Global \
Robotic Process Automation Market Size</h3>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: white;'>2022-2029 \
period</h5>", unsafe_allow_html=True)

st.altair_chart(bar_chart, use_container_width=True)

st.markdown("By 2029 the market is projected to **:blue[grow to USD 43.52 billion]** at a CAGR of 23.4% in forecast period.")


###_____MARKET SEGMENTATION___###

st.markdown("<h3 style='text-align: left; font-size:40px; color:#EE103F; \
'>II. Market Segmentation</h3>", unsafe_allow_html=True)

with st.container():
    col1, col2 = st.columns(2, gap='large')
    st.markdown(style_1,unsafe_allow_html=True)
    with col1:
        st.markdown("**Deployment**")
        st.markdown("* On Premise")
        st.markdown("* Cloud ")
        st.caption("Adoption of Advanced Technologies such as AI, Cloud is increasing to boost RPA capabilities")

    st.markdown(style_2,unsafe_allow_html=True)
    with col2:
        st.markdown("**Solution**")
        st.markdown("* Software")
        st.markdown("* Service")
        st.caption("This segment is expected to have the largest share as the adoption of RPA-as-a-Services \
    surges worldwide")


with st.container():
    col1, col2 = st.columns(2, gap='large')
    st.markdown(style_1,unsafe_allow_html=True)
    with col1:
        st.markdown("**End User Industry**")
        st.markdown("* IT and Telecom")
        st.markdown("* Healthcare")
        st.markdown("* BFSI")
        st.markdown("* Retail")
        st.markdown("* Manufacturing")
        st.markdown("* Other")

    st.markdown(style_2,unsafe_allow_html=True)
    with col2:
        st.markdown("**Geography**")
        st.markdown("* North America")
        st.caption("Largest market share during the forcast period")
        st.markdown("* Europe")
        st.markdown("* Asia Pacific")
        st.caption("Fastest growing region of the forcast period")
        st.markdown("* Latin America")
        st.markdown("* Middle East and Africa")

###_____MARKET TRENDS___###

st.markdown("<h3 style='text-align: left; font-size:40px; color:#EE103F; \
'>III. Market Trends</h3>", unsafe_allow_html=True)

st.markdown("**:blue[🌱Drivers for Market Growth]**")
#**:blue[

st.markdown("*Rising adoption of RPA in Healthcare industry over COVID-19 Pandemic*")
st.caption("* The pandemic boosted the demand for healthcare providers contact center tasks")
st.caption("* RPA technology is used to speed up the development of pharmaceuticals \
and has a relevant role in pharmacovigilance")

st.markdown("*Increasing adoption advanced technology such as AI, ML and Cloud*")
st.caption("* There is a higher adoption of Intelligent bots (RPA + AI) and their capabilities is expanding")
st.caption("* Higher adoption of Infrastructure-as-a-Service (IaaS),\
Plataform-as-a-Service (PaaS) and Software-as-a-Service (SaaS) for cloud computing that boost the market")

st.markdown("**:blue[🔻Factor that Blocks Market Growth]**")
st.markdown("*Infrastructure and Customization of RPA implementation*")
st.caption("* RPA implementtion is complex and expensive (infrastructure, \
hire personnel, educate current employees, deployment)")


###_____MARKET OUTLOOK___###

# st.markdown("<h3 style='text-align: left; font-size:40px; color:#EE103F; \
# '>IV. Market Outlook</h3>", unsafe_allow_html=True)
