import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import dashtools

# Sample data
df = pd.DataFrame({
    "Year": [2018, 2019, 2020, 2021, 2022, 2023],
    "Sales": [100, 200, 300, 250, 400, 450]
})

# Create figure
fig = px.line(df, x="Year", y="Sales", title="Sales Over Time")

# Initialize Dash app
app = dash.Dash(__name__)
server = app.server

# Layout
app.layout = html.Div(children=[
    html.H1("Simple Dash App"),
    dcc.Graph(id="line-graph", figure=fig)
])

# Run app
if __name__ == "__main__":
    app.run_server(debug=True)