import streamlit as st
import pandas as pd
import numpy as np

# Homework 11 : 11 places with Location in map
st.title("11 Interesting Places In India to visit")
st.subheader("Want to go then first scroll through this site...")
st.info("These places are according to my choices, there are still many places in India that are beautiful, mesmerizing and adventurous!!")

st.sidebar.title("11 Interesting Places")
st.sidebar.subheader("It's my personal Choices")
place = st.sidebar.radio("Choose a place: ", ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"])

# Place 2
if place == "2":
    st.header("Adiyogi Shiva")
    # CHANGED: Local absolute path changed to relative path
    st.image("images/gettyimages-1066143570-612x612.jpg")
    st.subheader("About")
    st.info("About the place : The Adiyogi Shiva bust is a 34-metre-tall (112 ft)...")
    st.subheader("Location in map")
    md1 = pd.DataFrame(np.random.randn(1, 2) / [50, 50] + [10.972270147042348, 76.7407714296481], columns=["lat", "lon"])
    st.map(md1, size=744, color="#183FDA")

# Place 3
elif place == "3":
    st.header("Chittorgarh")
    # CHANGED: Local absolute path changed to relative path
    st.image("images/india-rajasthan-chittorgarh-fort.webp")
    st.subheader("About")
    st.info("About the place : Chittorgarh Fort is India's largest fort...")
    st.subheader("Location in map")
    md2 = pd.DataFrame(np.random.randn(1, 2) / [50, 50] + [25.024210067839196, 74.69943033359412], columns=["lat", "lon"])
    st.map(md2, size=744, color="#BC1611")

# Place 4
elif place == "4":
    st.header("Dwarka")
    st.image("images/5714340.webp")
    st.subheader("About")
    st.info("About the place : Dwarka, located on the western tip...")
    st.subheader("Location in map")
    md3 = pd.DataFrame(np.random.randn(1, 2) / [50, 50] + [22.2444592181988, 68.97023016180516], columns=["lat", "lon"])
    st.map(md3, size=744, color="#B742B3")

# Place 5
elif place == "5":
    st.header("Ladakh")
    st.image("images/wp9815254.webp")
    st.subheader("About")
    st.info("About the place : Ladakh, often called Little Tibet...")
    st.subheader("Location in map")
    md4 = pd.DataFrame(np.random.randn(1, 2) / [50, 50] + [34.638778141698204, 77.24245492340275], columns=["lat", "lon"])
    st.map(md4, size=744, color="#183FDA")

# Place 6
elif place == "6":
    st.header("Jaipur")
    st.image("images/5000515.webp")
    st.subheader("About")
    st.info("About the place: Jaipur, the capital of Rajasthan...")
    st.subheader("Location in map")
    md5 = pd.DataFrame(np.random.randn(1, 2) / [50, 50] + [26.918181525241014, 75.78916726398127], columns=["lat", "lon"])
    st.map(md5, size=744, color="#BC1611")

# Place 7
elif place == "7":
    st.header("Nainital")
    st.image("images/9071138.webp")
    st.subheader("About")
    st.info("About the place : Nainital, often called the Lake District...")
    st.subheader("Location in map")
    md6 = pd.DataFrame(np.random.randn(1, 2) / [50, 50] + [29.392993430290886, 79.45312471979828], columns=["lat", "lon"])
    st.map(md6, size=744, color="#B742B3")

# Place 8
elif place == "8":
    st.header("Himanchal Pradesh")
    st.image("images/wp13852573.webp")
    st.subheader("About")
    st.info("About the place : Himachal Pradesh, known as Dev Bhoomi...")
    st.subheader("Location in map")
    md7 = pd.DataFrame(np.random.randn(1, 2) / [50, 50] + [31.99520909049508, 76.90582815800526], columns=["lat", "lon"])
    st.map(md7, size=744, color="#183FDA")

# page 0
elif place == "0":
    username = st.text_input("Username: ", max_chars=15)
    st.write(" your entered username is :", username)
    password = st.text_input("Password: ", max_chars=15, type="password")
    st.write("password length is :", len(password))

# Place 9
elif place == "9":
    st.header("Gulmarg")
    st.image("images/9470510.webp")
    st.subheader("About")
    st.info("About the place : Gulmarg, translating to Meadow of Flowers...")
    st.subheader("Location in map")
    md8 = pd.DataFrame(np.random.randn(1, 2) / [50, 50] + [34.04614948986164, 74.46245198073697], columns=["lat", "lon"])
    st.map(md8, size=744, color="#BC1611")

# Place 10
elif place == "10":
    st.header("Kerla")
    st.image("images/851772-2000x1333-desktop-hd-kerala-wallpaper-photo.webp")
    st.subheader("About")
    st.info("About the place : Kerala, famously known as God's Own Country...")
    st.subheader("Location in map")
    md9 = pd.DataFrame(np.random.randn(1, 2) / [50, 50] + [19.47351729273764, 82.54052439367075], columns=["lat", "lon"])
    st.map(md9, size=744, color="#183FDA")

# Place 1
elif place == "1":
    st.header("Meghalaya")
    st.image("images/03y8iuhdyqpwl1wy7r0nmxo86c9w_Krang_Suri_Waterfall_(6).webp")
    st.subheader("About")
    st.info("About the place : Meghalaya, meaning Abode of Clouds...")
    md10 = pd.DataFrame(np.random.randn(1, 2) / [50, 50] + [25.615206274480887, 91.08290501577207], columns=["lat", "lon"])
    st.map(md10, size=744)
