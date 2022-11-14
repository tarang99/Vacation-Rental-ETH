import streamlit as st
import requests


st.set_page_config(page_title = 'Welcome to Vacation Finder!', layout='wide')
  
  
 
st.title('Welcome To ETHER-BNB:house:')
st.subheader('Find the best vacation homes in Toronto or Vancouver!')  

st.write('Rent amazing home for your next holidays using Ethereum') 

st.image("Images/6.png", width=700)

 # Contact       
with st.container():
    st.write("___")
    st.header("We are here to help!")
    st.write('##')

    # Contact Form
    contact_form = """
    <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
        
        # Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")
