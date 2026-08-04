import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt

def plot_group_barChart(df, xaxis, yaxis, title):
    fig = px.bar(
        df,
        x=xaxis,
        y=yaxis,
        title=title,
        barmode="group",
        color_discrete_sequence=[
            "#032F6C",
            "#1272D1",
            "#5DA3E9",
            "#9BBDD4",
        ]
    )

    fig.update_layout(

        # Title
        title={
            "text": title,
            "x": 0.5,
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
        yaxis_title="Score",

        xaxis_title_font=dict(
            size=16,
            color="#3B82F6"
        ),

        yaxis_title_font=dict(
            size=16,
            color="#3B82F6"
        ),

        # Grid
        xaxis=dict(
            showgrid=False
        ),

        yaxis=dict(
            showgrid=True,
            gridcolor="#E5E7EB"
        ),

        # Legend
        legend_title="Metrics"
    )

    st.plotly_chart(fig, use_container_width=True)