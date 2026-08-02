import streamlit as st
import plotly.express as px

def plot_pieChart(df, names, values, title):
    fig = px.pie(
        df, 
        names = names,
        values= values, 
        title = title,
        color_discrete_sequence=[

            "#0047AB",
            "#0066CC",
            "#1E90FF",
            "#5DADE2",
            "#AED6F1",
            "#D6EAF8",
            "#EBF5FB"
        ],
        
    )
    fig.update_layout(

        title={
            "text":title,
            "x":0.5,
            "xanchor":"center",

            "font":{

                "size":22,
                "color":"#354B6F",
                "family":"Arial"

            }
        },

        legend_title="Category"

    )
    st.plotly_chart(fig, use_container_width=True)