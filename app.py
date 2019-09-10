import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Pick variables
tabtitle='dog breeds'
myheading = 'Breeds of Dogs'
myfavoritecolor='#0B5AAE' # More colors are here: https://htmlcolorcodes.com/
x_list=['Australian Cattle Dogs', 'French Bulldogs', 'Corgis', 'Pugs']
y_list=[12, 4, 6, 5]
mytitle='My favorite dog breeds'
githublink='https://github.com/calijason76/zoo-animals-dash'

########### Set up the chart
mydata = [go.Bar(x=x_list,
                y=y_list,
                marker=dict(color=myfavoritecolor))]
mylayout = go.Layout(
    title = mytitle,
    xaxis = dict(title = 'Dog Breed Names'),
    yaxis = dict(title = 'Favorites'))
myfigure = go.Figure(data=mydata, layout=mylayout)

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Display the chart
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(id='figure-1', figure=myfigure),
    html.A('Code on Github', href=githublink)])

########### Execute your code
if __name__ == '__main__':
    app.run_server()
