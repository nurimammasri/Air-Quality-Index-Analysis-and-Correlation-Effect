import streamlit as st
import base64
import os

st.set_page_config(
    layout="wide"
)


st.title("Projects")

# def show_pdf(file_path):
#     with open(file_path,"rb") as f:
#         base64_pdf = base64.b64encode(f.read()).decode('utf-8')
#     pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
#     st.text(pdf_display)
#     st.markdown(pdf_display, unsafe_allow_html=True)

# if os.path.dirname(os.getcwd()) == "/app":
#     d = "/app/air-quality-index-analysis-and-correlation-effect/Dashboard"
# else:
#     d=os.getcwd()

# show_pdf(d+'/docs/portfolio.pdf')

pdf = os.getcwd()+'/docs/portfolio.pdf'
st.markdown(f"""
<iframe src="https://drive.google.com/uc?id=1UdXtGNRX1KC-qqIakEDLgxnm7V6heHa7/" width="1300" height="650"></iframe>
""", unsafe_allow_html=True)

