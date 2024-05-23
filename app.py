import streamlit as st
from streamlit_apexjs import st_apexcharts

st.set_page_config(layout="wide")

st.title("Hello, world!")
st.write("It's a Bar Chart and a Donut Chart!")

options_bar = {
  "chart": {
    "type": 'bar',
    "toolbar": {"show": False}      
  },
  "plotOptions": {
    "bar": {
      "horizontal": False,
      "columnWidth": '80%',      
      "endingShape": 'rounded',
      "events": {
        "click": False
      }
    },
  },
  "dataLabels": {
    "enabled": False
  },
  "stroke": {
    "show": True,
    "width": 2,
    "colors": ['transparent']
  },
  "xaxis": {
    "categories": [''],
  },
  "yaxis": {
    "title": {
      "text": ''
    }
  },
  "fill": {
    "opacity": 1    
  },
  "tooltip": {
    "enabled": False
  },
  "legend": {
    "show": True,
    "position": "bottom",
    "labels": {
      "colors": "#000000", 
      "useSeriesColors": False
    },
    "onItemClick": {
      "toggleDataSeries": False
    }
  },
  "colors": ['#ffe4e1', '#d9aea9', '#50c878', '#42a864', '#efdd3e', '#cabb30', '#40e0d0', '#34bcaf', '#ffa500', '#d48900'],
  "title": {
    "text": "CSA Estudante X Turma - MÉDIA",        
    "align": "center",
    "style": {
      "fontSize": "14px",
      "color": "#000000",
      "fontWeight": 'normal'
    }
  }     
}


options_donut = {
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

col1, col2 = st.columns([2,1])

with col1:
  with st.container(border=True):
    #series = [{
      #"name": "Porcentagem",
      #"data": [69.1, 80.5, 72.2, 99.8, 23.6]
    #}]
    series = [
      {"name": "Empatia estudante", "data": [69.1, 0, 0, 0, 0]},
      {"name": "Empatia turma", "data": [76.8, 0, 0, 0, 0]},
      {"name": "Resiliência estudante", "data": [0, 80.5, 0, 0, 0]},
      {"name": "Resiliência turma", "data": [0, 72.9, 0, 0, 0]},
      {"name": "Abertura ao Novo estudante", "data": [0, 0, 72.2, 0, 0]},
      {"name": "Abertura ao Novo turma", "data": [0, 0, 81.2, 0, 0]},
      {"name": "Autogestão estudante", "data": [0, 0, 0, 99.8, 0]},
      {"name": "Autogestão turma", "data": [0, 0, 0, 43.4, 0]},
      {"name": "Engajamento estudante", "data": [0, 0, 0, 0, 41.6]},
      {"name": "Engajamento turma", "data": [0, 0, 0, 0, 28.3]}
    ]     
    type = 'bar'
    width = 600
    height = 300
    st_apexcharts(options_bar, series, type, width)    

with col2:
  with st.container(border=True):
    series = [8, 25, 10, 15, 42]
    type = 'donut'
    width = 300
    st_apexcharts(options_donut, series, type, width)
