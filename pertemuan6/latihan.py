import streamlit as st
if 'username' not in st.session_state:
    st.session_state['username'] = "admin"
if 'password' not in st.session_state:
    st.session_state['password'] = "password"
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
    
    
st.title("Halaman Login")
st.write("Masukan kredensial Anda Untuk masuk")

username_input = st.text_input("Username") 
password_input = st.text_input("Password", type="password")

if st.button("Login"):
    if username_input == st.session_state['username'] and password_input == st.session_state['password']:
        st.session_state['logged_in'] = True
        st.switch_page("pages/home.py")
    else:
        st.error("Login mu gagal login ulang lagi")
        
if st.session_state['logged_in']:
    st.switch_page("pages/home.py")


#home 
import streamlit as st

if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
    st.switch_page("login_page.py")
st.title("Halaman Login")
st.subheader(f"selamat datang, {st.session_state['username']}!")
st.write("anda telah masuk ke aplikasi ini!!")

if st.button("logout"):
    st.session_state.logged_in = False
    st.rerun()

#profile
import streamlit as st

if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
    st.switch_page("login_page.py")

st.subheader(f"selamat datang, {st.session_state['username']}!")
st.write("anda telah masuk ke aplikasi ini!!")

username_input = st.text_input("Masukan username: ", value = st.session_state['username'])
password_input = st.text_input("Masukan password: ", type="password", value = st.session_state['username'])

if st.button("ubah"):
    st.session_state["username"] = username_input
    st.session_state["password"] = password_input
    st.switch_page("pages/home.py")
