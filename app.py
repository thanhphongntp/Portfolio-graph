import dash
from dash import html

# Create Dash app
app = dash.Dash(__name__)

# App Layout
app.layout = html.Div(style={"fontFamily": "Arial", "padding": "0", "margin": "0"}, children=[
    html.Div(style={
        "padding": "10px 10px",
        "background": "linear-gradient(90deg, #007BFF, #00C6FF)",
        "color": "white",
        "textAlign": "left",
        "borderRadius": "0",  # Remove rounded corners
        "width": "100%",      # Full-width
        "boxShadow": "0 4px 12px rgba(0, 0, 0, 0.3)",  # Optional shadow for depth
        "animation": "fadeIn 2s ease-in-out"
    }, children=[
        html.H1("📊 Portfolio Plot", style={
            "fontSize": "2em",
            "marginBottom": "10px",
            "textShadow": "2px 2px 4px rgba(0, 0, 0, 0.5)"
        }),
        html.P("A showcase of data visualizations and process monitoring insights.", style={
            "fontSize": "1.em",
            "letterSpacing": "1px",
            "fontWeight": "300"
        })
    ]),

    html.Div([
        html.Div([
            html.H3("1. Monitor Failure Rate Trend Period", style={"textAlign": "left"}),
            html.Div([
                html.Img(src="/assets/trend1.png", style={
                    "width": "50%", "borderRadius": "10px",
                    "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.1)",
                    "marginBottom": "10px", "paddingLeft": "20px"
                }),
                html.Img(src="/assets/trend2.png", style={
                    "width": "50%", "borderRadius": "10px",
                    "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.1)",
                    "marginBottom": "10px", "paddingLeft": "20px"
                }),
                html.Img(src="/assets/trend3.png", style={
                    "width": "50%", "borderRadius": "10px",
                    "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.1)",
                    "paddingLeft": "20px"
                }),
            ], style={"display": "flex", "flexDirection": "column", "gap": "10px"})
        ]),

        html.Div([
            html.H3("2. Monitor Failure Categories", style={"textAlign": "left"}),
            html.Img(src="/assets/fail_trend1.png", style={
                "width": "40%", "borderRadius": "10px",
                "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.1)",
                "paddingLeft": "20px"
            }),
            html.Img(src="/assets/fail_trend2.jpg", style={
                "width": "50%", "borderRadius": "10px",
                "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.1)",
                "paddingLeft": "20px"
            }),
        ]),
        html.Div([
            html.H3("3. Overall System Performance", style={"textAlign": "left"}),
            html.Img(src="/assets/machine1.png", style={"width": "50%", "borderRadius": "10px", "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.1)", "paddingLeft": "20px"})
        ]),

        html.Div([
            html.H3("4. Commonality check", style={"textAlign": "left"}),
            html.Img(src="/assets/defect1.jpg", style={"width": "50%", "borderRadius": "10px", "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.1)", "marginBottom": "10px", "paddingLeft": "20px"}),
            html.Img(src="/assets/scatter1.jpg", style={"width": "50%", "borderRadius": "10px", "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.1)", "marginBottom": "10px", "paddingLeft": "20px"}),
            html.Img(src="/assets/distribition1.png", style={"width": "50%", "borderRadius": "10px", "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.1)", "marginBottom": "10px", "paddingLeft": "20px"}),
            html.Img(src="/assets/corr.png", style={"width": "50%", "borderRadius": "10px", "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.1)", "marginBottom": "10px", "paddingLeft": "20px"}),
        ]),

        html.Div([
            html.H3("5. Heatmap check", style={"textAlign": "left"}),
            html.Img(src="/assets/heatmap1.png", style={"width": "50%", "borderRadius": "10px", "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.1)", "marginBottom": "10px", "paddingLeft": "20px"}),
        ]),

        html.Div([
            html.H3("6. Variation check", style={"textAlign": "left"}),
            html.Img(src="/assets/variation1.png", style={"width": "50%", "borderRadius": "10px", "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.1)", "marginBottom": "10px", "paddingLeft": "20px"}),
        ])
    ], style={"display": "flex", "flexDirection": "column", "gap": "20px"})
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8080)
