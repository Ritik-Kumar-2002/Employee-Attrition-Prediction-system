import plotly.express as px

def plotbar_chart(result):
    fig = px.bar(
        result,
    )
    fig.show()