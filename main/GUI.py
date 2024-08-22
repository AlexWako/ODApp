from ShopifyApp import *
from ScanForFile import *
from FulfillScript import *
from EditMeasureScript import *
from CompetitorScript import *
from JeansMeasureEdit import *
from UpdateJeans import *
from Layout import *

headers = None

def login_screen(headers):
    window = psg.Window('Login', get_login_layout())
    while True:
        event, values = window.read()
        if event == psg.WINDOW_CLOSED:
            break
        if event == 'Submit':
            headers = activate_session(values[0])
            if headers == None:
                window.close()
                psg.popup("Wrong API Token", title = "Error")
                window = psg.Window('Login', get_login_layout())
                continue
            else:
                break
    window.close()
    return headers

def fulfill_order(window):
    while True:
        event, values = window.read()
        if event == psg.WINDOW_CLOSED:
            return "Exit"
        if event == "Go Back":
            window.close()
            return "Go Back"
        if event == "Submit":
            file_path = values["-FILE-"]
            # Creates a new window with the output of the script
            if file_path:
                # Runs the script first
                output = update_fulfillment(file_path, headers = headers)
                window.close()
                window = psg.Window("Required Fulfillments", get_fulfill_output_layout(output))
                event, values = window.read()
                while True:
                    if event == psg.WINDOW_CLOSED or event == "Exit":
                        return "Exit"
                    if event == "Home":
                        window.close()
                        return "Go Back"
            else:
                window.close()
                return "Go Back"

def update_jeans(window):
    while True:
        event, values = window.read()
        if event == psg.WIN_CLOSED:
            return "Exit"
        if event == "Go Back":
            window.close()
            return "Go Back"
        

def edit_measure(window):
    while True:
        event, values = window.read()
        if event == psg.WIN_CLOSED:
            return "Exit"
        if event == "Go Back":
            window.close()
            return "Go Back"
        if event == "Submit":
            product_name = values['-INPUT-']
            try:
                product_id = get_product(product_name, headers = headers)[0]
                html_code = get_product(product_name, headers = headers)[1]
            except:
                window.close()
                psg.popup("Unknown Product", title = "Error")
                return "Go Back"
            if html_code:
                cm_data = get_og_cm_data(html_code)
                window.close()
                window = psg.Window('Input Table', get_input_table_layout(cm_data))
                event, values = window.read()
                if event == psg.WINDOW_CLOSED:
                    return "Exit"
                if event == "Go Back":
                    window.close()
                    window = psg.Window('Input Window', get_edit_measurement_layout())
                    continue
                if event == "Submit":
                    table_data = values["-DATA-"].split("\n")
                    for i, row in enumerate(table_data):
                        table_data[i] = row.split("\t")
                    status = update_measure_table(product_id, edit_table(html_code, table_data), headers)
                    if status == "Complete":
                        window.close()
                        window = psg.Window('', get_measurement_output_layout())
                        event, values = window.read()
                        if event == psg.WINDOW_CLOSED or event == "Exit":
                            return "Exit"
                        if event == "Home":
                            window.close()
                            return "Go Back"
                    window.close()
                    psg.popup("Failed", title = "Error")
                    return "Go Back"

def competitor_price(window):
    while True:
        event, values = window.read()
        if event == psg.WIN_CLOSED:
            return "Exit"
        if event == "Go Back":
            window.close()
            return "Go Back"
        if event == "Submit":
            brand = values['-INPUT-'].lower()
            if brand in brands:
                new_data = get_denimio(brand)
                txt_old_data = pd_txt_file(brand)
                if txt_old_data == None:
                    status = pd_txt_file(brand, new_data)
                    if status == "Done":
                        window.close()
                        window = psg.Window('', get_diagnostic_output_layout())
                        event, values = window.read()
                        if event == psg.WINDOW_CLOSED or event == "Exit":
                            return "Exit"
                        if event == "Home":
                            window.close()
                            return "Go Back"
                else:
                    old_data = eval(txt_old_data)
                    return_data = diagnostic(old_data, new_data)
                    window.close()
                    if return_data['Changes'] == [] and return_data['New products'] == []:
                        status = pd_txt_file(brand, new_data)
                        if status == "Done":
                                window.close()
                                window = psg.Window('', get_diagnostic_no_output_layout())
                                event, values = window.read()
                                if event == psg.WINDOW_CLOSED or event == "Exit":
                                    return "Exit"
                                if event == "Home":
                                    window.close()
                                    return "Go Back"
                    else:
                        window = psg.Window('Diagnostic', get_diagnostic_table_layout(return_data))
                        event, values = window.read()
                        if event == psg.WINDOW_CLOSED:
                            return "Exit"
                        if event == "Go Back":
                            window.close()
                            window = psg.Window('Input Window', get_brand_input_layout())
                            continue
                        if event == "Finish":
                            status = pd_txt_file(brand, new_data)
                            if status == "Done":
                                window.close()
                                window = psg.Window('', get_diagnostic_output_layout())
                                event, values = window.read()
                                if event == psg.WINDOW_CLOSED or event == "Exit":
                                    return "Exit"
                                if event == "Home":
                                    window.close()
                                    return "Go Back"

def add_jeans(window):
    while True:
        event, values = window.read()
        if event == psg.WIN_CLOSED:
            return "Exit"
        if event == "Go Back":
            window.close()
            return "Go Back"
        if event == 'Submit':
            name = values['-NAME-']
            url = values['-URL-']
            jean_type = values['-TYPE-']
            og_file_path = values['-OGFILE-']
            file_path = values['-FILE-']
            if name and url and jean_type and file_path:
                df = pd.read_csv(file_path)
                new_df = jeans_measure_edit(df, url, jean_type)
                result = update_csv(new_df, name, og_file_path)
                print(result)
                if result:
                    window.close()
                    window = psg.Window('', get_finish_update_layout())
                    event, values = window.read()
                    if event == psg.WINDOW_CLOSED or event == "Exit":
                        return "Exit"
                    if event == "Home":
                        window.close()
                        return "Go Back"
                else:
                    window.close()
                    psg.popup("Failed")
                    return "Go Back"
            else:
                window.close()
                return "Go Back"

###############################


if check_resource_path() == "Complete":

    headers = login_screen(headers)

    if headers != None:

        window = psg.Window('OD App', get_start_layout())

        while True:

            event, values = window.read()

            if event == psg.WINDOW_CLOSED or event == "Exit":
                break

            # Fulfill Order Window
            if event == "Fulfill Order":
                window.close()
                window = psg.Window("Fulfill Orders", get_fulfill_layout())
                status = fulfill_order(window)
                if status == "Go Back":
                    window = psg.Window('OD App', get_start_layout())
                    continue
                if status == "Exit":
                    break

            # Edit Measurement Window
            if event == "Edit Measurement":
                window.close()
                window = psg.Window('Input Window', get_edit_measurement_layout())
                status = edit_measure(window)
                if status == "Go Back":
                    window = psg.Window('OD App', get_start_layout())
                    continue
                if status == "Exit":
                    break

            # Competitor Price Window
            if event == "Competitor Changes":
                if check_diagnostic_path():
                    window.close()
                    window = psg.Window('Input Window', get_brand_input_layout())
                    status = competitor_price(window)
                    if status == "Go Back":
                        window = psg.Window('OD App', get_start_layout())
                        continue
                    if status == "Exit":
                        break
            
            # Edit Jean Data Frame Window
            if event == "Add Jeans":
                window.close()
                window = psg.Window('Edit Data', get_update_data_layout())
                status = add_jeans(window)
                if status == "Go Back":
                    window = psg.Window('OD App', get_start_layout())
                    continue
                if status == "Exit":
                    break

        window.close()

close_session()
