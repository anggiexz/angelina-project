import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


path_dataset = "day.csv"

df = pd.read_csv(path_dataset)

df.describe(include="all")

def run():
    st.set_page_config(
        page_title="Bike Dataset",
        page_icon="👋",
    )

st.image('https://cdn.pixabay.com/photo/2017/08/07/09/50/bike-2602080_1280.jpg', 
          use_column_width=True)

st.title(" Bike Sharing Information 🚲 ")

# Menjumlahkan nilai dalam kolom 'cnt'
total_cnt = df['cnt'].sum()


# Menampilkan teks
st.write("Total users who rent bike (2011 - 2012): ")

st.write(f"<h1 style='color: purple'>{total_cnt}</h1>", unsafe_allow_html=True)


st.title (" During weekdays in 2011 & 2012, which month has the highest and the lowest bike rental users for each year?")

#Data 1#
wd1 = df[(df['workingday'] == 1) & (df['mnth'] == 1)& (df['yr'] == 0)]['cnt'].sum()
wd2 = df[(df['workingday'] == 1) & (df['mnth'] == 2)& (df['yr'] == 0)]['cnt'].sum()
wd3 = df[(df['workingday'] == 1) & (df['mnth'] == 3)& (df['yr'] == 0)]['cnt'].sum()
wd4 = df[(df['workingday'] == 1) & (df['mnth'] == 4)& (df['yr'] == 0)]['cnt'].sum()
wd5 = df[(df['workingday'] == 1) & (df['mnth'] == 5)& (df['yr'] == 0)]['cnt'].sum()
wd6 = df[(df['workingday'] == 1) & (df['mnth'] == 6)& (df['yr'] == 0)]['cnt'].sum()
wd7 = df[(df['workingday'] == 1) & (df['mnth'] == 7)& (df['yr'] == 0)]['cnt'].sum()
wd8 = df[(df['workingday'] == 1) & (df['mnth'] == 8)& (df['yr'] == 0)]['cnt'].sum()
wd9 = df[(df['workingday'] == 1) & (df['mnth'] == 9)& (df['yr'] == 0)]['cnt'].sum()
wd10 = df[(df['workingday'] == 1) & (df['mnth'] == 10)& (df['yr'] == 0)]['cnt'].sum()
wd11 = df[(df['workingday'] == 1) & (df['mnth'] == 11)& (df['yr'] == 0)]['cnt'].sum()
wd12 = df[(df['workingday'] == 1) & (df['mnth'] == 12)& (df['yr'] == 0)]['cnt'].sum()

#Data 2#
wdd1 = df[(df['workingday'] == 1) & (df['mnth'] == 1)& (df['yr'] == 1)]['cnt'].sum()
wdd2 = df[(df['workingday'] == 1) & (df['mnth'] == 2)& (df['yr'] == 1)]['cnt'].sum()
wdd3 = df[(df['workingday'] == 1) & (df['mnth'] == 3)& (df['yr'] == 1)]['cnt'].sum()
wdd4 = df[(df['workingday'] == 1) & (df['mnth'] == 4)& (df['yr'] == 1)]['cnt'].sum()
wdd5 = df[(df['workingday'] == 1) & (df['mnth'] == 5)& (df['yr'] == 1)]['cnt'].sum()
wdd6 = df[(df['workingday'] == 1) & (df['mnth'] == 6)& (df['yr'] == 1)]['cnt'].sum()
wdd7 = df[(df['workingday'] == 1) & (df['mnth'] == 7)& (df['yr'] == 1)]['cnt'].sum()
wdd8 = df[(df['workingday'] == 1) & (df['mnth'] == 8)& (df['yr'] == 1)]['cnt'].sum()
wdd9 = df[(df['workingday'] == 1) & (df['mnth'] == 9)& (df['yr'] == 1)]['cnt'].sum()
wdd10 = df[(df['workingday'] == 1) & (df['mnth'] == 10)& (df['yr'] == 1)]['cnt'].sum()
wdd11 = df[(df['workingday'] == 1) & (df['mnth'] == 11)& (df['yr'] == 1)]['cnt'].sum()
wdd12 = df[(df['workingday'] == 1) & (df['mnth'] == 12)& (df['yr'] == 1)]['cnt'].sum()


# Data untuk grafik 1 (tahun 2011)
year_2011 = ['1', '2', '3', '4','5','6','7','8','9','10','11','12']
users_2011 = [wd1, wd2, wd3, wd4, wd5, wd6, wd7, wd8, wd9, wd10, wd11, wd12]
bar_labels_2011 = ['1', '2', '3', '4','5','6','7','8','9','10','11','12']
bar_colors_2011 = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange', 'tab:purple', 'tab:brown',
              'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan', 'tab:orange', 'tab:green']

# Data untuk grafik 2 (tahun 2012)
year_2012 = ['1', '2', '3', '4','5','6','7','8','9','10','11','12']
users_2012 = [wdd1, wdd2, wdd3, wdd4, wdd5, wdd6, wdd7, wdd8, wdd9, wdd10, wdd11, wdd12]
bar_labels_2012 = ['1', '2', '3', '4','5','6','7','8','9','10','11','12']
bar_colors_2012 = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange', 'tab:purple', 'tab:brown',
              'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan', 'tab:orange', 'tab:green']

# Membuat dua subplot dalam satu baris
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Plot grafik 1
ax1.bar(year_2011, users_2011, tick_label=bar_labels_2011, color=bar_colors_2011)
ax1.set_ylabel('users')
ax1.set_xlabel('month')
ax1.set_title('2011')

# Plot grafik 2
ax2.bar(year_2012, users_2012, tick_label=bar_labels_2012, color=bar_colors_2012)
ax2.set_ylabel('users')
ax2.set_xlabel('month')
ax2.set_title('2012')

# Menampilkan plot dalam Streamlit
st.pyplot(fig)

with st.expander("Conclusion"):
    st.write(
        """
        It can be concluded that for the years 2011 and 2012, 
        the highest number of bike rentals users occurred in August, 
        while the lowest occurred in January.
        """
    )

# Membuat tab #

st.write('select a year for more information')
year1, year2 = st.tabs(["2011", "2012"])

with year1:
  
    st.header("Bike Sharing in 2011")
    ("- The number of bikes rented during weekdays in January :", wd1 ,'bikes')
    ("- The number of bikes rented during weekdays in February :", wd2 ,'sepeda')
    ("- The number of bikes rented during weekdays in March :", wd3 ,'sepeda')
    ("- The number of bikes rented during weekdays in April :", wd4 ,'bikes')
    ("- The number of bikes rented during weekdays in May :", wd5 ,'bikes')
    ("- The number of bikes rented during weekdays in June :", wd6 ,'bikes')
    ("- The number of bikes rented during weekdays in July :", wd7 ,'bikes')
    ("- The number of bikes rented during weekdays in August :", wd8 ,'bikes')
    ("- The number of bikes rented during weekdays in September :", wd9 ,'bikes')
    ("- The number of bikes rented during weekdays in October :", wd10 ,'bikes')
    ("- The number of bikes rented during weekdays in November :", wd11 ,'bikes')
    ("- The number of bikes rented during weekdays in December :", wd12 ,'bikes')

    
with year2:

    st.header("Bike Sharing in 2012")
    ("- The number of bikes rented during weekdays in January :", wdd1 ,'bikes')
    ("- The number of bikes rented during weekdays in February :", wdd2 ,'sepeda')
    ("- The number of bikes rented during weekdays in March :", wdd3 ,'sepeda')
    ("- The number of bikes rented during weekdays in April :", wdd4 ,'bikes')
    ("- The number of bikes rented during weekdays in May :", wdd5 ,'bikes')
    ("- The number of bikes rented during weekdays in June :", wdd6 ,'bikes')
    ("- The number of bikes rented during weekdays in July :", wdd7 ,'bikes')
    ("- The number of bikes rented during weekdays in August :", wdd8 ,'bikes')
    ("- The number of bikes rented during weekdays in September :", wdd9 ,'bikes')
    ("- The number of bikes rented during weekdays in October :", wdd10 ,'bikes')
    ("- The number of bikes rented during weekdays in November :", wdd11 ,'bikes')
    ("- The number of bikes rented during weekdays in December :", wdd12 ,'bikes')

st.title (" In which season did the most and the least for casual users, registered users, and total users rent bikes in 2011-2012?")


# Data for casual users
casual_user = ['1', '2', '3', '4']
countss = [60622, 203522, 226091, 129782]
bar_labels = ['1', '2', '3', '4']
bar_colorss = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange']

# Data for registered users
registered_user = ['1', '2', '3', '4']
countsss = [410726, 715067, 835038, 711831]
bar_labels = ['1', '2', '3', '4']
bar_colorss = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange']

# Data for total users
total_user = ['1', '2', '3', '4']
countssss = [471348, 918589, 1061129, 841613]
bar_labels = ['1', '2', '3', '4']
bar_colorss = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange']

# Create a single subplot with three bars for each season
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20, 5))

# Plot for casual users
ax1.bar(casual_user, countss, color=bar_colorss)
ax1.set_ylabel('Users')
ax1.set_xlabel('Season')
ax1.set_title('Casual Users for Every Season')

# Plot for registered users
ax2.bar(registered_user, countsss, color=bar_colorss)
ax2.set_ylabel('Users')
ax2.set_xlabel('Season')
ax2.set_title('Registered Users for Every Season')

# Plot for total users
ax3.bar(total_user, countssss, color=bar_colorss)
ax3.yaxis.set_major_formatter(FuncFormatter(lambda x, _: '{:,.0f}'.format(x)))
ax3.set_ylabel('Users')
ax3.set_xlabel('Season')
ax3.set_title('Total Users for Every Season')

# Adjust layout and display the plot
plt.tight_layout()
plt.show()


st.pyplot(fig)

with st.expander("Conclusion"):
    st.write(
        """
        From the three aspects (Casual, Registered, and Total User), 
        it can be concluded that bikes are most frequently rented during season 3, which includes Light Snow, 
        Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds,
        and least frequently during season 1, which includes Clear, Few clouds, 
        Partly cloudy, Partly cloudy.
        """
    )
    
# Membuat tab #

st.write('select users for more information')
Casual, Registered, Total = st.tabs(["Casual", "Registered","Total"])

with Casual:
  
    st.header("Casual users for every season")
    casual_season_1 = df.loc[df['season'] == 1, 'casual'].sum()
    casual_season_2 = df.loc[df['season'] == 2, 'casual'].sum()
    casual_season_3 = df.loc[df['season'] == 3, 'casual'].sum()
    casual_season_4 = df.loc[df['season'] == 4, 'casual'].sum()

    ("- Total casual rent bikes when Clear, Few clouds, Partly cloudy, Partly cloudy (season 1) : ", casual_season_1,'users')
    ("- Total casual rent bikes when Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist (season 2) : ", casual_season_2,'users')
    ("- Total casual rent bikes when Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds (season 3) : ", casual_season_3,'users')
    ("- Total casual rent bikes when Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog (season 4): ", casual_season_4,'users')

with Registered:
  
    st.header("Registered users for every season")
    registered_season_1 = df.loc[df['season'] == 1, 'registered'].sum()
    registered_season_2 = df.loc[df['season'] == 2, 'registered'].sum()
    registered_season_3 = df.loc[df['season'] == 3, 'registered'].sum()
    registered_season_4 = df.loc[df['season'] == 4, 'registered'].sum()

    ("- Total registered rent bikes when Clear, Few clouds, Partly cloudy, Partly cloudy (season 1): ", registered_season_1,'users')
    ("- Total registered rent bikes when Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist (season 2): ", registered_season_2,'users')
    ("- Total registered rent bikes when Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds (season 3): ", registered_season_3,'users')
    ("- Total registered rent bikes when Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog (season 4): ",registered_season_4,'users')

with Total:
  
    st.header("Total users for every season")
    cnt_season_1 = df.loc[df['season'] == 1, 'cnt'].sum()
    cnt_season_2 = df.loc[df['season'] == 2, 'cnt'].sum()
    cnt_season_3 = df.loc[df['season'] == 3, 'cnt'].sum()
    cnt_season_4 = df.loc[df['season'] == 4, 'cnt'].sum()

    ("- Total rent bikes when Clear, Few clouds, Partly cloudy, Partly cloudy (season 1) : ", cnt_season_1,'users')
    ("- Total rent bikes when Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist (season 2) : ", cnt_season_2,'users')
    ("- Total rent bikes when Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds (season 3) : ", cnt_season_3,'users')
    ("- Total rent bikes when Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog (season 4): ", cnt_season_4,'users')