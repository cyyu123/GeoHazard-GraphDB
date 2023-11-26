import pandas as pd
import json
import plotly.graph_objs as go
import plotly.express as px
import os
from plotly.io import to_html
from shiny import App, ui, reactive, render, Inputs, Outputs, Session

summary_stats_2022 = pd.read_csv("./Neo4JOutputs/count_level_summary.csv")
joining_sites = pd.read_csv("./july2023_hsi.csv")
joining_table = joining_sites[["Site Name", "County"]]

# Exectue data collection
# Define function that can basically obtain counts 

# Establish function to dynamically return available nodes in the db
water_data = {}
soil_data = {}

# Soil
for file in os.listdir("./soil/"):
    if ".csv" in file:
        file_name = file.replace(".csv", "")
        soil_data.update({file_name:pd.read_csv("./soil/"+file)})

for file in os.listdir("./water/"):
    if ".csv" in file:
        file_name = file.replace(".csv", "")
        water_data.update({file_name:pd.read_csv("./water/"+file)})

with open('./Neo4JOutputs/geojson-counties-fips.json') as file:
    counties_geojson = json.load(file)

# Plot features

def plot_feature(pulldata, site_var, county_var, location):
    georgia_features = [feature for feature in counties_geojson['features'] if feature['properties']['STATE'] == '13']

    georgia_geojson = {
        "type": "FeatureCollection",
        "features": georgia_features
    }

    chemical_colorscale = [
        [0, 'rgb(0, 50, 50)'],
        [0.5, 'rgb(0, 100, 50)'],
        [1, 'rgb(0, 0, 200)']
    ]

    # Create a scatter plot for the sites
    scatter = go.Scattergeo(
        lon = pulldata['longitude'],
        lat = pulldata['latitude'],
        text = pulldata['Site Name'],
        mode = 'markers',
        marker = dict(
            color = pulldata['counts'],
            colorscale = chemical_colorscale,
            colorbar = dict(
                title = 'Number of Chemicals',
                x = 0.1
            ),
            opacity = 0.5,
            reversescale = False,
            symbol = 'circle',
            showscale = True
        )
    )

    # Create a map with both the scatter plot and the county boundaries
    fig = go.Figure(scatter)
    fig.update_geos(
        fitbounds="locations",
        visible=False
    )
    fig.add_trace(
        go.Choropleth(
            geojson=georgia_geojson,
            featureidkey="properties.NAME",
            locations=summary_stats_2022['Geography'],
            z=summary_stats_2022[county_var],
            colorscale="Reds",
            colorbar = dict(
                title = county_var,
                x = 0.9
            ),
            marker_line_width=0
        )
    )
    fig.update_layout(
        title_text = county_var + ' & ' + site_var + " - " + location,
        geo_scope='usa',
    )

    # Show the figure
    return fig

# App
# Assuming soil_data and water_data are defined somewhere in your script

app_ui = ui.page_fluid(
    ui.navset_tab(
        #Intro
        ui.nav("Intro", "Intro", ui.page_fluid(
            ui.h1("MVP_GEOHAZARD-GRAPHDB for Georgia 2023"),
            ui.p("This application provides a brief overview of soil and water contaminant sites data across various counties in Georgia. It allows users to view data, perform aggregate analysis, visualize data on maps, and explore county trends."),
            ui.h2("How to Use This App"),
            ui.p("Navigate the tabs through the top. Please note that some datasets are not currently finished which may result in an error being thrown. Please ignore and try another variable if this occurs."),
            ui.h2("Data Sources and Methodology"),
            ui.p("Data is sourced from a graph database that was previously constructed, focusing on soil and water quality in Georgia. Methods include data aggregation and geospatial mapping. More advanced capabilites may be added in the future. This represents the first working version of the dataset."),
            ui.h2("Interactive Elements"),
            ui.p("The app includes interactive maps, dynamic charts, and filters for customized analysis."),
            ui.h2("Contact and Feedback"),
            ui.p("For more information or to provide feedback, feel free to reach out at knakats@emory.edu.")
        )),

        
        # Tab 1: View Data
        ui.nav("View Data", "View Data", ui.page_fluid(
            ui.input_select("select_type", "Select Type:", ["Soil", "Water"]),
            ui.input_select("select_key", "Select Key:", list(water_data.keys())),
            ui.output_ui("data_display"),
        )),
        # Tab 2: View Agg Data
        ui.nav("View County Stats", "View County Stats", ui.page_fluid(
            ui.input_select("select_type_county", "Select Type:", ["Soil", "Water"]),
            ui.input_select("select_key_county", "Select Key:", list(water_data.keys())),
            ui.input_select("filter_bool", "Filter?", ["Yes", "No"]),
            ui.input_select("filterby", "Filter By:", ["population_category", "black_percentile_category", "poor_percentile_category", "age_18_24_percentile_category", "educational_score_25_over_percentile_category"]),
            ui.input_select("filterbylevel", "Filter Level:", ["very low", "low", "medium", "high", "very high"]),
            ui.output_ui("data_display_agg"),
        )),
        # Tab 3: Map View
        ui.nav("Map View", "Map View", ui.div(
            ui.input_select("select_type_map", "Select Type:", ["Soil", "Water"]),
            ui.input_select("select_key_map", "Select Key:", list(water_data.keys())),
            ui.input_select("select_countvar_map", "Select County Variable", ["avg_pop", "percent_black", "poverty_rate", "age_18_24_score", "educational_score_25_over"]),
            ui.output_ui("map_display")
        )),
        # Tab 4: Statistics (Eventually)
        ui.nav("Plot County Trends", "Plot County Trends", ui.div(
            ui.input_select("select_type_trends", "Select Type:", ["Soil", "Water"]),
            ui.input_select("select_key_trends", "Select Key:", list(water_data.keys())),
            ui.input_select("plot_county", "Plot County:", ["avg_pop", "percent_black", "poverty_rate", "age_18_24_score", "educational_score_25_over"]),
            ui.output_ui("stats_display")
        ))
    )
)

# Server logic
def server(input, output, session: Session):

    @output
    @render.ui
    def data_display():
        selected_type = input.select_type()
        selected_key = input.select_key()
        data = soil_data[selected_key] if selected_type == "Soil" else water_data[selected_key]
        return ui.HTML(data.to_html(classes="table table-striped"))

    @output
    @render.ui
    def data_display_agg():
        selected_type = input.select_type_county()
        selected_key = input.select_key_county()
        data = soil_data[selected_key] if selected_type == "Soil" else water_data[selected_key]

        merge1 = pd.merge(left = data, right = joining_table)[["County", "counts"]]

        merge1_agg = merge1.groupby("County").agg("sum").reset_index()

        return_data = pd.merge(merge1_agg, summary_stats_2022[["Geography","population_category", "black_percentile_category", "poor_percentile_category", "age_18_24_percentile_category", "educational_score_25_over_percentile_category"]], left_on = "County", right_on = "Geography").drop(["Geography"], axis = 1).sort_values(by = "counts", ascending= False)

        if input.filter_bool() == "Yes":
            selected_col = input.filterby()
            level = input.filterbylevel()

            return_data = return_data.loc[return_data[selected_col] == level ,:]
                
        return ui.HTML(return_data.to_html(classes="table table-striped"))

    @output
    @render.ui
    def map_display():
        selected_type = input.select_type_map()
        selected_key = input.select_key_map()
        selected_county_var = input.select_countvar_map()
        data = soil_data[selected_key] if selected_type == "Soil" else water_data[selected_key]

        fig = plot_feature(data, selected_key, selected_county_var, selected_type)

        plot_html = to_html(fig, full_html=False, include_plotlyjs='cdn')
        return ui.HTML(plot_html)

    @output
    @render.ui
    def stats_display():
        selected_type = input.select_type_trends()
        selected_key = input.select_key_trends()
        data = soil_data[selected_key] if selected_type == "Soil" else water_data[selected_key]

        merge1 = pd.merge(left = data, right = joining_table)[["County", "counts"]]

        merge1_agg = merge1.groupby("County").agg("sum").reset_index()

        return_data = pd.merge(merge1_agg, summary_stats_2022[["Geography","avg_pop", "percent_black", "poverty_rate", "age_18_24_score", "educational_score_25_over"]], left_on = "County", right_on = "Geography").drop(["Geography"], axis = 1).sort_values(by = "counts", ascending= False)

        plotthis = input.plot_county()

        fig = px.scatter(return_data, x = plotthis, y = "counts", hover_data = ["County"])

        plot_html = to_html(fig, full_html=False, include_plotlyjs='cdn')

        return ui.HTML(plot_html)

app = App(app_ui, server)

if __name__ == "__main__":
    app.run()