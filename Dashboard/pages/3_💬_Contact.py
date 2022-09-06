import streamlit as st

st.title("Contact")

st.markdown('***')
## Find me and let's connect 
html_string = """## Find me
<p>
  <a href="https://www.linkedin.com/in/nurimammasri/" target="_blank"><img alt="LinkedIn" src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" /></a>  
  <a href="https://www.instagram.com/nurimammasri" target="_blank"><img alt="Instagram" src="https://img.shields.io/badge/instagram-%23E4405F.svg?&style=for-the-badge&logo=instagram&logoColor=white" /></a> 
  <a href="mailto:nurimammasri.01@gmail.com" target="_blank"><img alt="Gmail" src="https://img.shields.io/badge/gmail-D14836?&style=for-the-badge&logo=gmail&logoColor=white"/></a> 
  <a href="https://medium.com/@nurimammasri" target="_blank"><img alt="Medium" src="https://img.shields.io/badge/medium-%2312100E.svg?&style=for-the-badge&logo=medium&logoColor=white" /></a>  
  <a href="https://github.com/nurimammasri" target="_blank"><img alt="Github" src="https://img.shields.io/github/followers/nurimammasri?style=social" /></a>  
  
</p>
"""
st.markdown(html_string, unsafe_allow_html=True)