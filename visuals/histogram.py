import streamlit as st
import plotly.express as px

def plot_histogram(df, xaxis, yaxis, title):
    fig = px.bar(
            df,
            x = xaxis,
            y = yaxis,
            title=title,
            orientation='h',
            color_discrete_sequence=["#2061c3"],  
        )
    fig.update_layout(

        # Title
        title={
            "text": title,
            "x": 0.5,                     # Center
            "xanchor": "center",
            "font": {
                "size": 22,
                "color": "#354B6F",
                "family": "Arial"
            }
        },

        # Background
        plot_bgcolor="#FFFFFF",
        paper_bgcolor="#FFFFFF",

        # Axis Titles
        xaxis_title=xaxis,
        yaxis_title=yaxis,

        xaxis_title_font=dict(
            size=16,
            color='#3B82F6'
        ),

        yaxis_title_font=dict(
            size=16,
            color="#3B82F6"
        ),

        # Grid Color
        xaxis=dict(
            showgrid=False
        ),

        yaxis=dict(
            showgrid=True,
            gridcolor="#E5E7EB"
        )
    )  
    st.plotly_chart(fig, use_container_width=True)