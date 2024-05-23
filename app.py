import streamlit as st
from streamlit_apexjs import st_apexcharts

st.set_page_config(layout="wide")

st.title("Hello, world!")
st.write("It's a Donut Chart!")

options = {
  "chart": {
    "toolbar": {"show": False},
  },
  "legend": {
    "show": True,    
    "position": "bottom",    
    "labels": {
      "colors": "#000000",
      "useSeriesColors": False
    },
  },
  "plotOptions": {
    "pie": {
      "expandOnClick": True,
      "donut": {
        "size": '50%',
        "labels": {
          "show": False,
          "name": {
            "show": True,
            "fontSize": '14px',
            "color": '#000000'
          },
          "value": {
            "show": False,
            "fontSize": '14px',
            "color": '#000000'                        
          },
          "total": {
            "show": False,
            "label": 'Total',
            "color": '#000000'
          }
        }
      }
    }
  },
  "colors": ['#ffe4e1', '#50c878', '#efdd3e', '#40e0d0', '#ffa500'],
  "labels": ['Empatia', 'Resiliência', 'Abertura ao Novo', 'Autogestão', 'Engajamento'],
  "dataLabels": {
    "enabled": True,
    "style": {
      "colors": ['#000000'],
      "fontWeight": 'normal'
    }
  },
  "tooltip": {
    "enabled": False
  },
  "title": {
    "text": "CSA Estudante - TOTAL",        
    "align": "center",
    "style": {
      "fontSize": "14px",
      "color": "#000000",
      "fontWeight": 'normal'
    }
  }
}

series = [8, 25, 10, 15, 42]
type = 'donut'
width = 300
#st_apexcharts(options, series, type, width)

col1, col2 = st.columns([2,1])

with col1:
  with st.container(border=True):
    st.write("Estou aqui")

with col2:
  with st.container(border=True):
    st_apexcharts(options, series, type, width)
