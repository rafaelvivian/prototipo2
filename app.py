import streamlit as st
from streamlit_apexjs import st_apexcharts

st.title("Olá, mundo!")
st.write("Estou aqui!")

options = {
    "chart": {
        "toolbar": {
            "show": False
        }
    },

    "labels": [1991, 1992, 1993, 1994, 1995]
    ,
    "legend": {
        "show": True,
        "position": "bottom",
    }
}

series = [44, 55, 41, 17, 15]

st_apexcharts(options, series, 'donut', '600', 'title')
