import streamlit as st
import pandas as pd
import numpy as np

#Homework 11 : 11 places with Location in map

st.title("11 Interesting Places In India to visit")
st.subheader("Want to go then first scroll throgh this site...")
st.info("These places are accornding to my choices there are still many places in india that are beautiful, mesmerizing and adventurous!!")

st.sidebar.title("11 Interesting Places ")
st.sidebar.subheader("It's my personal Choices")
place = st.sidebar.radio("Choose a place: ",["0","1","2","3","4","5","6","7","8","9","10","11"])




# Place 2
if place == "2":
    st.header("Adiyogi Shiva")
    st.image(r"C:/Users/TANU/Downloads/gettyimages-1066143570-612x612.jpg")
    st.subheader("About")
    st.info("About the place : The Adiyogi Shiva bust is a 34-metre-tall (112 ft), 45-metre-long (147 ft) and 25-metre-wide (82 ft) steel bust of Shiva with Thirunamam at Coimbatore, Tamil Nadu. It is recognized by the Guinness World Records as the Largest Bust Sculpture” in the world.[1][2] Designed by Sadhguru, the founder and head of the Isha Foundation, the statue weighs around 500 tonnes (490 long tons; 550 short tons).Adiyogi refers to Shiva as the first yogi.[4] It was established to inspire people towards inner well-being through yoga.")
    st.subheader("Location in map")
    md1 = pd.DataFrame(np.random.randn(1,2)/[50,50]+[10.972270147042348, 76.7407714296481],columns=["lat","lon"])

    st.map(md1, size = 744, color = "#183FDA")

#Place 3
elif place == "3":

   st.header("Chittorgarh")
   st.image(r"C:\Users\TANU\Downloads\india-rajasthan-chittorgarh-fort.webp")
   st.subheader("About")
   st.info("About the place : Chittorgarh Fort is India's largest fort, sprawling over 700 acres atop a 180-meter-high hill in Rajasthan.  It stands as a powerful symbol of Rajput valor, sacrifice, and resistance, having witnessed three legendary sieges and acts of jauhar (mass self-immolation) by Rajput women to protect their honor.")
   st.subheader("Location in map")

   md2 = pd.DataFrame(np.random.randn(1,2)/[50,50]+[25.024210067839196, 74.69943033359412],columns=["lat","lon"])

   st.map(md2, size = 744, color = "#BC1611")


#Place 4
elif place == "4":

   st.header("Dwarka")
   st.image(r"C:\Users\TANU\Downloads\5714340.webp")
   st.subheader("About")
   st.info("About the place : Dwarka, located on the western tip of the Kathiawar Peninsula in Gujarat, is one of India's holiest cities and a key part of the Char Dham pilgrimage circuit.  Known as the Gateway to Heaven (Dwar means gate, Ka refers to Brahma), it is believed to be the ancient kingdom of Lord Krishna, established over 2,500 years ago. ")
   st.subheader("Location in map")
   md3 = pd.DataFrame(np.random.randn(1,2)/[50,50]+[22.2444592181988, 68.97023016180516],columns=["lat","lon"])

   st.map(md3, size = 744, color = "#B742B3")


#Place 5

elif place == "5":

   st.header("Ladakh")
   st.image(r"C:\Users\TANU\Downloads\wp9815254.webp")
   st.subheader("About")
   st.info("About the place : Ladakh, often called Little Tibet or the Land of High Passes, is a high-altitude cold desert in the northernmost part of India.  Since 2019, it has been a separate Union Territory, distinct from Jammu & Kashmir.  It is renowned for its stark, dramatic landscapes, ancient Tibetan Buddhist culture, and extreme adventure opportunities.")
   st.subheader("Location in map")
   md4 = pd.DataFrame(np.random.randn(1,2)/[50,50]+[34.638778141698204, 77.24245492340275],columns=["lat","lon"])

   st.map(md4, size = 744, color = "#183FDA")


#Place 6

elif place == "6":

   st.header("Jaipur")
   st.image(r"C:\Users\TANU\Downloads\5000515.webp")
   st.subheader("About")
   st.info("About the place: Jaipur, the capital of Rajasthan, is famously known as the Pink City due to the distinctive terracotta-pink color of its historic buildings.  Founded in 1727 by the Kachchwaha Rajput ruler Maharaja Sawai Jai Singh II, it was India's first planned city, designed using a grid system based on the principles of Vastu Shastra and Shilpa Shastra by the architect Vidyadhar Bhattacharya.")
   st.subheader("Location in map")
   md5 = pd.DataFrame(np.random.randn(1,2)/[50,50]+[26.918181525241014, 75.78916726398127],columns=["lat","lon"])

   st.map(md5, size = 744, color = "#BC1611")


#Place 7

elif place == "7":

   st.header("Nainital")
   st.image(r"C:\Users\TANU\Downloads\9071138.webp")
   st.subheader("About")
   st.info("About the place : Nainital, often called the Lake District of India, is a picturesque hill station in the Kumaon region of Uttarakhand.  Nestled at an altitude of approximately 2,084 meters (6,840 ft), it is famous for its emerald-shaped Naini Lake, colonial heritage, and lush forests.")
   st.subheader("Location in map")
   md6 = pd.DataFrame(np.random.randn(1,2)/[50,50]+[29.392993430290886, 79.45312471979828],columns=["lat","lon"])

   st.map(md6, size = 744, color = "#B742B3")


#Place 8

elif place == "8":

   st.header("Himanchal Pradesh")
   st.image(r"C:\Users\TANU\Downloads\wp13852573.webp")
   st.subheader("About")
   st.info("About the place : Himachal Pradesh, known as Dev Bhoomi (Land of the Gods), is a mountainous state in northern India nestled in the Western Himalayas.  It is renowned for its diverse landscapes, ranging from lush green valleys and dense pine forests to stark, high-altitude cold deserts. Since becoming a full-fledged state in 1971, it has evolved into a premier destination for adventure tourism, spiritual retreats, and eco-tourism. ")
   st.subheader("Location in map")
   md7 =pd.DataFrame(np.random.randn(1,2)/[50,50]+[31.99520909049508, 76.90582815800526],columns=["lat","lon"])

   st.map(md7, size = 744, color = "#183FDA")

# page 0
elif place == "0":
    username = st.text_input("Username: ", max_chars=15 )
    st.write(" your entered username is :",username)
    password = st.text_input("Password: ", max_chars=15, type="password")
    st.write("password length is :",len(password))


#Place 9

elif place == "9":

   st.header("Gulmarg")
   st.image(r"C:\Users\TANU\Downloads\9470510.webp")
   st.subheader("About")
   st.info("About the place : Gulmarg, translating to Meadow of Flowers, is a world-renowned hill station and ski resort located in the Pir Panjal range of the Himalayas in Jammu and Kashmir.  Originally named Gaurimarg ( Path of Goddess Gauri ) by local shepherds, it was renamed by the 16th-century Kashmiri Sultan Yousuf Shah Chak, who frequented the meadow with his queen, Habba Khatoon. ")
   st.subheader("Location in map")
   md8 = pd.DataFrame(np.random.randn(1,2)/[50,50]+[34.04614948986164, 74.46245198073697],columns=["lat","lon"])

   st.map(md8, size = 744, color = "#BC1611")


#Place 10

elif place == "10":

   st.header("Kerla")
   st.image(r"C:\Users\TANU\Downloads\851772-2000x1333-desktop-hd-kerala-wallpaper-photo.webp")
   st.subheader("About")
   st.info("About the place : Kerala, famously known as God's Own Country, is a tropical paradise on India's southwestern Malabar Coast.  Renowned for its unique geography, it features a network of serene backwaters, lush hill stations, pristine beaches, and dense wildlife sanctuaries.  Unlike many Indian states, Kerala boasts a literacy rate of nearly 100% and a distinct culture shaped by centuries of spice trade and religious harmony. ")
   st.subheader("Location in map")
   md9 = pd.DataFrame(np.random.randn(1,2)/[50,50]+[19.47351729273764, 82.54052439367075],columns=["lat","lon"])

   st.map(md9, size = 744, color = "#183FDA")


#Place 11

elif place == "1" :
  st.header("Meghalaya")
  st.image(r"C:\Users\TANU\Downloads\03y8iuhdyqpwl1wy7r0nmxo86c9w_Krang_Suri_Waterfall_(6).webp")
  st.subheader("About")
  st.info("About the place : Meghalaya, meaning Abode of Clouds in Sanskrit, is a mountainous state in Northeast India known for its extreme rainfall, lush subtropical forests, and unique indigenous culture.  It is home to the Khasi, Jaintia, and Garo tribes, who maintain a matrilineal society where lineage and inheritance are traced through women.")
  md10 = pd.DataFrame(np.random.randn(1,2)/[50,50]+[25.615206274480887, 91.08290501577207],columns=["lat","lon"])

  st.map(md10, size = 744, color = "#B742B3")

#Place 12
else:

  st.header("Darjeeling")
  st.image(r"C:\Users\TANU\Downloads\wp10912265.webp")
  st.subheader("About")
  st.info("About the place : Darjeeling, known as the Queen of the Hills, is a historic hill station in the Eastern Himalayas of West Bengal.  Situated at an elevation of 2,045 meters (6,709 ft), it is globally renowned for its Darjeeling tea, the UNESCO-listed Darjeeling Himalayan Railway (Toy Train), and panoramic views of Mount Kanchenjunga (the world's third-highest peak).")
  st.subheader("Location in map")
  md11 = pd.DataFrame(np.random.randn(1,2)/[50,50]+[27.12024966102156, 88.64532666572138],columns=["lat","lon"])

  st.map(md11, size = 744, color = "#183FDA")

#st.header("Assam")
#st.image("")
#st.subheader("About")
#st.info("About the place :")
#st.subheader("Location in map")
#md12 = pd.DataFrame(np.random.randn(44,2)/[50,50]+[26.538421996698762, 92.52710857472634],columns=["lat","lon"])

#st.map(md12, size = 744, color = "#B742B3")

#st.header("Dhanushkodi")
#st.image("")
#st.subheader("About")
#st.info("About the place :")
#st.subheader("Location in map")
#md13 = pd.DataFrame(np.random.randn(44,2)/[50,50]+[9.180898536747778, 79.42230360494108],columns=["lat","lon"])

#st.map(md13, size = 744, color = "#183FDA")

#st.header("Lakshadweep")
#st.image("")
#st.subheader("About")
#st.info("About the place :")
#st.subheader("Location in map")
#md14 = pd.DataFrame(np.random.randn(44,2)/[50,50]+[10.135394033396052, 73.74058465644066],columns=["lat","lon"])

#st.map(md14, size = 744, color = "#B742B3")

#st.header("Puri ")
#st.image("")
#st.subheader("About")
#st.info("About the place :")
#st.subheader("Location in map")
#md15 = pd.DataFrame(np.random.randn(44,2)/[50,50]+[19.802659960721776, 85.84987405100605],columns=["lat","lon"])

#st.map(md15, size = 744, color = "#183FDA")
