import plotly.express as px
import streamlit as st

def plot_donut(df, names, values, title):
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
                "#EBF5FB",
                "#F7F7F7"
            ],
            hole=0.4, 
            
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