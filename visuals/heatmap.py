import plotly.express as px
import streamlit as st

def plot_heatmap(results_df, title):
    heatmap_df = results_df.set_index("Model")
    fig = px.imshow(
        heatmap_df,
        text_auto=".3f",
        color_continuous_scale="Blues",
        aspect="auto",
        title=title
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
    )
    st.plotly_chart(fig, use_container_width=True)