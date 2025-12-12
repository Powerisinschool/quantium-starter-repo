# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

df = pd.read_csv('pink_morsels_filtered.csv')

fig = px.line(df, x="date", y="sales", title="Sales by date", labels={"date": "Date", "sales": "Sales"})

app.layout = html.Div(children=[
    html.H1(children='Effect of price increase on sales', style={'textAlign': 'center'}),
    dcc.Graph(
        id="wind-speed",
        figure=fig,
    ),
])

if __name__ == '__main__':
    app.run(debug=True)
