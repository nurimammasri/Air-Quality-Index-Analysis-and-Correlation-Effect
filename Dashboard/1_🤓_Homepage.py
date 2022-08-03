import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import plotly.express as px
import plotly.graph_objs as go
import plotly.offline as pyoff
import warnings # Ignores any warning
warnings.filterwarnings("ignore")
plt.style.use('seaborn')
sns.set(rc={'figure.figsize':(15, 8)})
pd.set_option('display.max_columns', None)


st.set_page_config(
    page_title="Multipage App",
    page_icon="👋",
    layout="wide"
)

# ------------------------------------

####################
### INTRODUCTION ###
####################

row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((.1, 2.3, .1, 1.3, .1))
with row0_1:
    st.title('Air Quality Index Analysis and Correlation Effect')
with row0_2:
    st.text("")
    st.subheader('Streamlit App by [Nur Imam Masri](https://www.linkedin.com/in/nurimammasri/)')
row1_spacer1, row1_1, row1_spacer2 = st.columns((.1, 3.2, .1))
with row1_1:
    st.markdown("You can find the source code in:")
    st.markdown("[Air Quality Index Analysis and Correlation Effect GitHub Repository](https://github.com/nurimammasri/Air-Quality-Index-Analysis-and-Correlation-Effect)")
    
    st.markdown("**Air pollution** is the contamination of air due to the presence of substances in the atmosphere that are harmful to the health of humans and other living beings, or cause damage to the climate or to materials.")
        
    st.markdown("""
            There are many different types of air pollutants, such as :

            * *Gases* (including ammonia, carbon monoxide, sulfur dioxide, nitrous oxides, methane, carbon dioxide and chlorofluorocarbons),
            ```
            PM10 - Particulate Matter
            SO2 - Sulfur Dioxide
            CO - Carbon Monoxide
            O3 - Ozone
            NO2 - Natrium Dioxide
            CFC - Chlorofluorocarbon
            HC - Hidrokarbon
            Pb - Timah
            CO2 - Carbon Diaoksida
            ```
            * *Particulates* (both organic and inorganic), and
            * *Biological Molecules*
            
            Air pollution can cause diseases, allergies, and even death to humans;

            It can also cause harm to other living organisms such as animals and food crops, and may damage the natural environment (for example, climate change, ozone depletion or habitat degradation) or built environment (for example, acid rain).

            Both human activity and natural processes can generate air pollution.
    """)
    st.markdown("*`PLEASE WAIT A MOMENT FOR THE DATA TO LOAD`*")



################
### ANALYSIS ###
################

#############################################################
# 01. Most Polluted Cities and Countries (IQAir Index).ipynb
#############################################################

### DATA EXPLORER ###

# Load Data

# Clean - AIR QUALITY INDEX (by cities).csv
# df_aqicty = pd.read_csv("https://drive.google.com/uc?id=1V086i1eHdM08nk67F4l2D7_bj-ZJk8PY")
df_aqicty = pd.read_csv("../data/Most Polluted Cities and Countries (IQAir Index)/Clean - AIR QUALITY INDEX (by cities).csv")

# Clean - AIR QUALITY INDEX- top countries.csv
# df_aqitpcr = pd.read_csv("https://drive.google.com/uc?id=11qjUGvAQiqEgfPWW8USMz6rHlARcrL_P")
df_aqitpcr = pd.read_csv("../data/Most Polluted Cities and Countries (IQAir Index)/Clean - AIR QUALITY INDEX- top countries.csv")

# Clean - pollutant-standards-index-jogja-2020.csv
# df = pd.read_csv("https://drive.google.com/uc?id=1BpMqLEYmGRuOAIyzEsx_-XXdxF5b_1vR")
df = pd.read_csv("../data/Air Quality in Yogyakarta, Indonesia/Clean - pollutant-standards-index-jogja-2020.csv")

# GDPPerCapita.csv
# gdp = pd.read_csv("https://drive.google.com/uc?id=1rBgi4F_R9EhYerayeFvaRaRCPQV6N_IY")
gdp = pd.read_csv("../data/Co2 Emissions and Economic/GDPPerCapita.csv")

# CO2EmissionsPerCapita.csv
# co2pc = pd.read_csv("https://drive.google.com/uc?id=136cdpMhIX_WKyg5A_FKAjdDspog_Rc7p")
co2pc = pd.read_csv("../data/Co2 Emissions and Economic/CO2EmissionsPerCapita.csv")

# ElectricityGeneratedYear.csv
# elecdt = pd.read_csv("https://drive.google.com/uc?id=1f3LClVnVBSjExxdvsl5wSQBv3jwxF1G-")
elecdt = pd.read_csv("../data/Co2 Emissions and Economic/ElectricityGeneratedYear.csv")

# AnnualCOEmissionsbyRegion.csv
# co2ann = pd.read_csv("https://drive.google.com/uc?id=1LDi87mDkdnCkl6DN_CqZw9NZprYQGUch")
co2ann = pd.read_csv("../data/Co2 Emissions and Economic/AnnualCOEmissionsbyRegion.csv")

# jumlah_kendaraan_bermotor.csv
# df_kendaraan = pd.read_csv("https://drive.google.com/uc?id=1kSguqLIcFnTgqs2r67W0qLUVi0QWyHvh", sep=";")
df_kendaraan = pd.read_csv("../data/Additinal Data/jumlah_kendaraan_bermotor.csv", sep=";")

# jumlah_kendaraan_bermotor_provinsi_jenis.csv
# df_kendaraan_prov = pd.read_csv("https://drive.google.com/uc?id=1qFTbI3xHlvNMxdYDQMs34KG50n7Xrl5Y", sep=";")
df_kendaraan_prov = pd.read_csv("../data/Additinal Data/jumlah_kendaraan_bermotor_provinsi_jenis.csv", sep=";")

# jumlah_penduduk_provinsi_jk_all.csv
# df_penduduk_all = pd.read_csv("https://drive.google.com/uc?id=1NZZlMpsApa_VSO75TQfpe4qbQs0CXQeu", sep=";")
df_penduduk_all = pd.read_csv("../data/Additinal Data/jumlah_penduduk_provinsi_jk_all.csv", sep=";")

row2_spacer1, row2_1, row2_spacer2 = st.columns((.2, 7.1, .2))
with row2_1:

    st.markdown("You can click here to see the raw data first 👇")

    see_data = st.expander('AIR QUALITY INDEX (by cities)')
    with see_data:
        st.dataframe(data=df_aqicty.reset_index(drop=True))
    
    see_data2 = st.expander('AIR QUALITY INDEX (top countries)')
    with see_data2:
        st.dataframe(data=df_aqitpcr.reset_index(drop=True))

    see_data3 = st.expander('Pollutant Standards Index Jogja 2020')
    with see_data3:
        st.dataframe(data=df.reset_index(drop=True))

    see_data4 = st.expander('GDP Per Capita')
    with see_data4:
        st.dataframe(data=gdp.reset_index(drop=True))

    see_data5 = st.expander('CO2 Emissions Per Capita')
    with see_data5:
        st.dataframe(data=co2pc.reset_index(drop=True))

    see_data5 = st.expander('Electricity Generated Year')
    with see_data5:
        st.dataframe(data=elecdt.reset_index(drop=True))

    see_data6 = st.expander('Annual CO Emissions by Region')
    with see_data6:
        st.dataframe(data=co2ann.reset_index(drop=True))

    see_data7 = st.expander('Perkembangan Jumlah Kendaraan Bermotor Menurut Jenis (Unit), 2018-2020')
    with see_data7:
        st.dataframe(data=df_kendaraan.reset_index(drop=True))
    
    see_data8 = st.expander('Jumlah Kendaraan Bermotor Menurut Provinsi dan Jenis Kendaraan (unit)')
    with see_data8:
        st.dataframe(data=df_kendaraan_prov.reset_index(drop=True))
    
    see_data9 = st.expander('Jumlah Penduduk Hasil Proyeksi Menurut Provinsi dan Jenis Kelamin (Ribu Jiwa), 2018-2020')
    with see_data9:
        st.dataframe(data=df_penduduk_all.reset_index(drop=True))
st.text('')

row3_spacer1, row3_1, row3_spacer2 = st.columns((.2, 7.1, .2))
with row3_1:
    st.subheader('Most Polluted Cities and Countries (IQAir Index)')
    st.markdown('Show the (or a) match with the...')  
    