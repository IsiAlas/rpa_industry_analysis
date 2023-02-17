import streamlit as st

st.set_page_config(layout="wide")
style_1 = "<style>[data-testid=column]:nth-of-type(1) [data-testid=stVerticalBlock]{gap: 0rem;}</style>"
style_2 = "<style>[data-testid=column]:nth-of-type(2) [data-testid=stVerticalBlock]{gap: 0rem;}</style>"

st.markdown("<h3 style='text-align: center; font-size:40px; color:#EE103F; \
'>Customer Needs</h3>", unsafe_allow_html=True)

st.markdown("**:red[Who needs RPA?]**")
st.markdown("RPA is predominantly used in industries that are highly regulated such as \
financial institutions, healthcare and insurance and allow companies to automate repetitive tasks, increase efficiency and \
improve compliance.")

st.markdown("Using the European Commision's business size classification we can expect that RPA vendors \
customers have an annual revenue of at least USD 10 million (small businesses) and most customers have USD 50 \
million or more (large enterprises).")


st.markdown("**:red[What economic benefit can it have?]**")
st.markdown("According to a IDC report sponsored by UiPath, the economic benefit of UiPath RPA \
in 2021 was estimated to be USD 7 billion and is expected to grow to USD 55 billion on 2025 \
with a CAGR of 67%.")




st.markdown("<h3 style='text-align: center; font-size:40px; color:#EE103F; \
'>User Persona</h3>", unsafe_allow_html=True)


st.markdown("People that use RPA Software are:")

col1, col2 = st.columns(2, gap='large')
with col1:
    st.markdown(style_1,unsafe_allow_html=True)

    st.markdown("✅ **Business technologists**")
    st.caption("citizen developers")
    st.markdown("#")

    st.markdown("✅ **Software engineers**")
    st.caption("technical developers")
    st.markdown("#")

    st.markdown("✅ **Business end users of control panels**")
    st.caption("orchestrators")
    st.markdown("#")


    st.markdown("✅ **Business process experts**")
    st.caption("process designers")
    st.markdown("#")


with col2:
    st.markdown(style_2,unsafe_allow_html=True)
    st.markdown("✅ **Bot administrators**")
    st.markdown("#")

    st.markdown("✅ **IT infrastructure support engineers**")
    st.markdown("#")

    st.markdown("✅ **Automation center of excellence (COE) leads**")
    st.markdown("#")
