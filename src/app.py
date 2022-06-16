from dash import Dash, html, dash_table
import dash_bootstrap_components as dbc
import pandas as pd

app = Dash(name=__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

df = pd.read_csv("https://git.io/Juf1t")
table = dash_table.DataTable(
    id= "id-table",
    data=df.to_dict("records"), 
    columns=[{"id": col, "name": col} for col in df.columns],
    row_selectable="single",
    )


add_button = dbc.Button(id="id-add-button", children="Add", color="success")
update_button = dbc.Button(id="id-update-button", children="Update", color="warning")
remove_button = dbc.Button(id="id-remove-button", children="Remove", color="danger")



def generate_card_form(title, inputs):

    html_cardbody = [
        html.H4(
            id=f"id-{title}",
            children=title, 
            className="card-title"
        )
    ]

    cardbody_buttons = [
        html.Div(
            children=[
                dbc.Button("Cancel", color="danger"),
                dbc.Button("Confirm")
                ],
            className="d-flex justify-content-between"
            )
        ]

    cardbody_inputs = [
        dbc.Input(
            id=input.get("id"), 
            placeholder=input.get("placeholder"),
            value=input.get("value"),
            type=input.get("type")
            )
            
            for input in inputs
        ]

    children_cardbody = cardbody_inputs + cardbody_buttons

    cardbody_inputs_buttons = html.Div(
        children=children_cardbody,
        className="d-flex flex-column", 
        style={"gap": "0.5rem"}
    )

    html_cardbody.append(cardbody_inputs_buttons)

    return \
        dbc.Card(
            id="id-card-form",
            children=dbc.CardBody(
                html_cardbody
            ),
            class_name="d-flex w-50"
        )


_inputs = [
    {"id": "id-state", "placeholder": "State" ,"value": "Teste", "type": "Text"},
    {"id": "id-number-plants", "placeholder": "Number of Solar Plants", "type": "Number"},
    {"id": "id-installed", "placeholder": "Installed Capacity (MW)","type": "Number"},
    {"id": "id-average", "placeholder": "Average MW Per Plant","type": "Number"},
    {"id": "id-generation", "placeholder": "Generation (GWh)","value": 2,"type": "Number"},
]

add_card = generate_card_form(title="Update", inputs=_inputs)


form_collapse = dbc.Collapse(
    id="id-form-collapse",
    children=add_card,
    is_open=True,
    class_name="d-flex flex-fill"

)


div_buttons = html.Div(
    id="id-div-buttons", 
    children=[add_button, update_button, remove_button],
    className="d-flex justify-content-between p-2"
    )

div_table = html.Div(
    id="id-div-table", 
    children=table, 
    # className="d-flex justify-content-center"
    )

div_forms = html.Div(
    id="id-div-forms", 
    children=form_collapse,
    className="d-flex justify-content-between p-2"
    )

app_layout = dbc.Container(
    fluid=True, 
    children=[div_buttons,div_forms,div_table],
    className="d-flex flex-column justify-content-center"
    ) 

app.layout = app_layout

if __name__ == "__main__":
    app.run(debug=True)