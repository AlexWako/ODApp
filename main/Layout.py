import PySimpleGUI as psg

# Login Screen
def get_login_layout():

    layout = [
        [psg.Text("API Token:"), psg.InputText()],
        [psg.Button("Submit")]
    ]

    return layout

# Start Screen
def get_start_layout():

    button_layout = [
        [psg.Button('Fulfill Order')],
        [psg.Button('Edit Measurement')],
        [psg.Button('Competitor Changes')],
        [psg.Button('Add Jeans')],
        [psg.Button('Exit')]
    ]

    layout = [
        [psg.Column(button_layout)]
    ]

    return layout

#####################################

# Layout when user presses send email
def get_email_layout():
    email_template = [
        [psg.Text('Select an option:')],
        [psg.Combo(['Option 1', 'Option 2', 'Option 3'], default_value = 'Option 1', key = '-COMBO-', size = (20, 1))],
        [psg.Button('Submit')]
    ]
    return email_template

def get_fulfill_layout():
    layout = [
        [psg.Text('Select a CSV file:')],
        [psg.Input(key = '-FILE-', enable_events = True), psg.FileBrowse()],
        [psg.Button("Go Back", pad = ((0, 235), 0)), psg.Button('Submit')]
    ]
    return layout

def get_fulfill_output_layout(output):
    layout = [
                [psg.Text(output)],
                [psg.Button("Home", pad = ((0, 200), 0)), psg.Button("Exit")]
    ]
    return layout

#####################################

def get_edit_measurement_layout():
    layout = [
        [psg.Text('Enter product name:')],
        [psg.Input(key='-INPUT-')],
        [psg.Button("Go Back", pad = ((0, 235), 0)), psg.Button('Submit')]
    ]
    return layout

def get_input_table_layout(data):
    if len(data[0]) == 2:
        rows = len(data[1][0])
        input_layout = [[psg.Multiline(size=(25, 10), key='-DATA-')]]
        og_data_layout = [
            [psg.Table(values = data[1][0], headings = data[0][0], num_rows = rows, key = '-OUTPUT TABLE RAW-')],
            [psg.Table(values = data[1][1], headings = data[0][1], num_rows = rows, key = '-OUTPUT TABLE OW-')]
        ]
        button_layout = [
            [psg.Button("Submit")],
            [psg.Button("Go Back")]
        ]
        return [
            [psg.Frame('Original Table', og_data_layout), psg.VSeperator(), psg.Column(input_layout), psg.Column(button_layout)]
        ]

    else:
        rows = len(data[1])
        input_layout = [[psg.Multiline(size=(25, 10), key='-DATA-')]]
        og_data_layout = [
            [psg.Table(values = data[1], headings = data[0], num_rows = rows, key = '-OUTPUT TABLE-')]
        ]
        button_layout = [
            [psg.Button("Submit")],
            [psg.Button("Go Back")]
        ]
        return [
            [psg.Frame('Original Table', og_data_layout), psg.VSeperator(), psg.Column(input_layout), psg.Column(button_layout)]
        ]


def get_measurement_output_layout():
    layout = [
        [psg.Text("Complete", justification = 'center')],
        [psg.Button("Home", pad = ((0, 200), 0)), psg.Button("Exit")]
    ]
    return layout

#####################################

def get_brand_input_layout():
    layout = [
        [psg.Text('Enter brand name:')],
        [psg.Input(key='-INPUT-')],
        [psg.Button("Go Back", pad = ((0, 235), 0)), psg.Button('Submit')]
    ]
    return layout

def get_diagnostic_table_layout(data):
    table_layout = [
        [psg.Table(values = data["Changes"], headings = ['name', 'price change'])],
        [psg.Table(values = data["New products"], headings = ['name', 'price'])]
    ]
    change_layout = [
        [psg.Column([table_layout[0]])]
    ]
    new_layout = [
        [psg.Column([table_layout[1]])]
    ]
    button_layout = [
        [psg.Button("Finish")],
        [psg.Button("Go Back")]
    ]
    layout = [
        [psg.Frame('Price Changes', change_layout), psg.VSeparator(), psg.Frame('New Products', new_layout), psg.Column(button_layout)]
    ]
    return layout

def get_diagnostic_output_layout():
    layout = [
        [psg.Text("Data has been updated", justification = 'center')],
        [psg.Button("Home", pad = ((0, 200), 0)), psg.Button("Exit")]
    ]
    return layout

def get_diagnostic_no_output_layout():
    layout = [
        [psg.Text("No Changes", justification = "center")],
        [psg.Button("Home", pad = ((0, 200), 0)), psg.Button("Exit")]
    ]
    return layout

##########

def get_update_data_layout():
    layout = [
        [psg.Text('Product name:')],
        [psg.Input(key='-NAME-')],
        [psg.Text('Product Url')],
        [psg.Input(key='-URL-')],
        [psg.Text('Product Type')],
        [psg.Combo(['Raw', 'One Wash', 'Both'], size = (25, 100), key='-TYPE-')],
        [psg.Text('Select an Original CSV file:')],
        [psg.Input(key = '-OGFILE-', enable_events = True), psg.FileBrowse()],
        [psg.Text('Select a Inputting CSV file:')],
        [psg.Input(key = '-FILE-', enable_events = True), psg.FileBrowse()],
        [psg.Button("Go Back", pad = ((0, 235), 0)), psg.Button('Submit')]
    ]
    return layout

def get_finish_update_layout():
    layout = [
        [psg.Text("Success", justification = 'center')],
        [psg.Button("Home", pad = ((0, 200), 0)), psg.Button("Exit")]
    ]
    return layout

##########

def error_layout():
    layout = [
        
    ]