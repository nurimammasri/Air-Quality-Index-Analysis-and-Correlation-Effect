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

### DATA EXPLORER ###

# Load Data

# Clean - AIR QUALITY INDEX (by cities).csv
# df_aqicty = pd.read_csv("https://drive.google.com/uc?id=1V086i1eHdM08nk67F4l2D7_bj-ZJk8PY")
df_aqicty = pd.read_csv("../data/Most Polluted Cities and Countries (IQAir Index)/Clean - AIR QUALITY INDEX (by cities).csv")

# Clean - AIR QUALITY INDEX- top countries.csv
# df_aqitpcr = pd.read_csv("http s://drive.google.com/uc?id=11qjUGvAQiqEgfPWW8USMz6rHlARcrL_P")
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

#############################################################
# 01. Most Polluted Cities and Countries (IQAir Index).ipynb
#############################################################

row3_spacer1, row3_1, row3_spacer2 = st.columns((.2, 7.1, .2))
with row3_1:
    st.subheader('Most Polluted Cities and Countries (IQAir Index)')
    st.markdown('')

row4_spacer1, row4_1, row4_spacer2, row4_2, row4_spacer3  = st.columns((.2, 4.4, 0.1, 6.4, .2))
with row4_1:
    ### Top 10 Polluted Country In World ###
    top_10_country = df_aqitpcr.head(20).copy()
    top_10_country['Rank'] = 21-top_10_country['Rank']
    fig1= px.bar(top_10_country, y='Country/Region', 
                x='Rank', color='2021',
                title="Top 10 Polluted Country In World",
                text='2021',
                height=600)
    fig1.layout.plot_bgcolor = "white"
    fig1.update_layout(margin=dict(t=40, b=10))
    fig1.update_xaxes(visible=False, showticklabels=False)
    st.plotly_chart(fig1, use_container_width=True)
with row4_2:
    top_10_country = df_aqitpcr.head(17).copy().iloc[11:18,:]
    top_10_country['Rank'] = 18-top_10_country['Rank']

    # Deleting unnecesary Columns
    top_10_country.drop(['Population'], axis=1, inplace=True)

    # Converting wide to long format
    top_10_country = top_10_country.melt(id_vars=['Rank', 'Country/Region'],
                                var_name="Year", 
                                value_name="AQI")
                                
    top_10_country.sort_values(['Rank','Year'], ascending=[False, True], inplace=True)
    top_10_country['AQI'] = top_10_country['AQI'].astype(float)


    # For Plotting purose filling missing values with the backfill process
    top_10_country.fillna(method="bfill", inplace=True)

    fig2= px.line(top_10_country, y='AQI', 
                x='Year',
                color='Country/Region',
                title="Top 11-17 Yearly Air Quality Index", 
                symbol='Country/Region',
                text="AQI")
    fig2.for_each_trace(lambda t: t.update(textfont_color="black", textposition='top right'))
    fig2.layout.plot_bgcolor = "light grey"
    fig2.update_yaxes(visible=False, showticklabels=False, )
    fig2.update_layout(margin=dict(t=40, b=10))
    st.plotly_chart(fig2, use_container_width=True)
    st.markdown('Investigate a variety of stats for each team. Which team scores the most goals per game? How does your team compare in terms of distance ran per game?')    
   


def human_format(num):
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    # add more suffixes if you need them
    return '%.1f%s' % (num, ['', 'K', 'M', 'B', 'T', 'P'][magnitude])
    
row5_spacer1, row5_1, row5_spacer2, row5_2, row5_spacer3  = st.columns((.2, 6.4, 0.1, 4.4, .2))
with row5_1:
    top_10_country = df_aqitpcr.sort_values(['Population'], ascending=False).head(10).copy()
    top_10_country["text"] = top_10_country["Population"].apply(lambda x: human_format(x))
    fig1= px.bar(top_10_country, 
                x="Country/Region",
                y="Population", 
                color='Country/Region',
                text="text",
                title="Top 10 Population Country In World")
    fig1.layout.plot_bgcolor = "white"
    fig1.update_layout(margin=dict(t=40, b=10))
    st.plotly_chart(fig1, use_container_width=True)
with row5_2:
    st.markdown('Investigate a variety of stats for each team. Which team scores the most goals per game? How does your team compare in terms of distance ran per game?')    


# Get Indonesia Data

# select city in Indonesia
df_aqicty_indo = df_aqicty.loc[df_aqicty['country'] == 'Indonesia'].reset_index(drop=True)

# select country = Indonesia
df_aqitpcr_indo = df_aqitpcr.loc[df_aqitpcr['Country/Region'] == "Indonesia"].reset_index(drop=True)

row6_spacer1, row6_1, row6_spacer2 = st.columns((.2, 7.1, .2))
with row6_1:
    df_aqicty_indo_bar = df_aqicty_indo.copy()
    labels = df_aqicty_indo_bar['city_only']
    fig = go.Figure(data=[
        go.Bar(name="2021", x=labels, y=df_aqicty_indo_bar['2021'], text=df_aqicty_indo_bar['2021']),
        go.Bar(name="2020", x=labels, y=df_aqicty_indo_bar['2020'], text=df_aqicty_indo_bar['2020']),
        go.Bar(name="2019", x=labels, y=df_aqicty_indo_bar['2019'], text=df_aqicty_indo_bar['2019'])
    ])

    # Change the bar mode
    fig.update_layout(title_text='Indonesia Average Air Quality Index by City (3 Years)')
    # fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
    fig.update_layout(barmode='stack')
    fig.update_layout(margin=dict(t=40, b=10))
    fig.for_each_trace(lambda t: t.update(textfont_color="white"))
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("""
        **Keypoints Viz1**

        * Overall, air pollution has gone down in the last 4 years being year 2021 to be the lowest 
        * Jakarta has highest average AQI score with 39.2 
        * Indralaya in South Sumatra has lowest score with 4.2 
        * 4 out of 5 highest polluted cities is in Java 
        * Lowest 5 polluted cities located in Sumatra and Kalimantan Many cities have around 15-25 AQI score
    
    """)  
row7_spacer1, row7_1, row7_spacer2 = st.columns((.2, 7.1, .2))
with row7_1:
    # line plot with plotly express
    df_aqicty_indo_line = df_aqicty_indo.copy()

    # dropping unused columns
    df_aqicty_indo_line.drop(['2021', '2020', '2019', '2018', '2017', 'country', 'city_only'],
                    axis=1, inplace=True)

    # converting wide to long format
    df_aqicty_indo_line = df_aqicty_indo_line.melt(id_vars = ['Rank', 'City'],
                                var_name = "Month", 
                                value_name = "Air Quality Index")

    # filling missing values with the backfill process
    df_aqicty_indo_line.fillna(method="bfill", inplace=True)

    fig= px.line(df_aqicty_indo_line, y = 'Air Quality Index', 
                labels = { 'Air Quality Index': 'AQI'}, 
                x = 'Month', color = 'City',
                title = "Monthly Air Quality Index 2021")
    fig.layout.plot_bgcolor = "light grey"
    
    fig.update_layout(margin=dict(t=40, b=10))
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("""
        **Keypoints Viz2**

        * Jakarta have overall high AQI with highest on July with 57.2
        * Pontianak has staggering rise of 86.2 AQI on November yet followed by inverse effect in cities like Bandung, Jakarta, Serang, and Jambi
        * Indralaya experienced healthy fall of AQI after March by almost 40 points
    """)    


