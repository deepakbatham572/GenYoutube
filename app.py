import streamlit as st
from utils import get_answer

if 'API_KEY' not in st.session_state:
    st.session_state['API_KEY'] = ''

st.sidebar.title('❤ Youtube script generator')
st.session_state['API_KEY'] = st.sidebar.text_input('Enter your api key here:' , type= 'password')
st.sidebar.image('Youtube.jpg' , width=300 , use_column_width= True)

prompt = st.text_input('Enter your topic here' , key='prompt')
video_length = st.slider("Video length 📺" , 0.0 , 10.0 , step=0.1)
creativity = st.slider("Your creativity Range ✨" , 0.0 , 1.0 ,step=0.1)

submit  = st.button('submit')

if submit:
    if st.session_state['API_KEY']:
        search_result,title,script = get_answer(prompt,video_length,creativity,st.session_state['API_KEY'])
        #Generate Script:

        st.success('Hope you like this script 🤩')

        #Generate Title:

        st.subheader('Your Video Title:')
        st.write(title)

        #Video Script

        st.subheader("Your Video Script")
        st.write(script)

        st.subheader("DuckDuckgo Search result: ")
        with st.expander('show me 👀'):
            st.info(search_result)

    else:
        st.error("Oopps someting wrong please try again")