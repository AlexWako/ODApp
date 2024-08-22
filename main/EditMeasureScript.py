import requests
import re
import shopify
from bs4 import BeautifulSoup

#　Get product data from typed product name
def get_product(product, headers):

    edit_product = product.replace('"', "'")

    query = '''
        query($productName: String!) {
            products(query: $productName, first: 10) {
                edges {
                    node {
                        id
                        descriptionHtml
                    }
                }
            }
        }
    '''

    variables = {
        'productName': edit_product
    }

    data = {
        'query': query,
        'variables': variables
    }


    response = requests.post(
        "https://okayamadenim.myshopify.com/admin/api/2023-04/graphql.json",
        json = data,
        headers = headers
    ).json()

    # If the product does not exist return None
    if response['data']['products']['edges'] == []:
        return False

    index = 0

    # Matches the product with ID number since request is inconsistent
    for id in response['data']['products']['edges']:
        if shopify.Product.find(re.search(r'\d+', str(id['node']['id'])).group()).title == product:
            break
        index += 1

    # Returns the product ID and the HTML body
    return (re.search(r'\d+', response['data']['products']['edges'][index]['node']['id']).group(), response['data']['products']['edges'][index]['node']['descriptionHtml'])

# Get the description of the body
def get_table(html_body):

    # Return the table part of the description
    soup = BeautifulSoup(html_body, 'html.parser')
    return soup.find_all('table')

# Get original sizing of the object
def get_og_cm_data(html_body):

    measurements = []

    table = get_table(html_body)

    if len(table) == 4:
        
        measure_row = [[], []]

        cm_rows_raw = table[0].find_all('tr')
        cm_rows_ow = table[2].find_all('tr')

        for row in cm_rows_raw:

            cells = row.find_all('td')

            # Extract the content of each row
            data = [cell.get_text(strip=True) for cell in cells]

            # Add the data into the measure_row if
            if cm_rows_raw.index(row) != 0:

                measure_row[0].append(data)

            else:

                measurements.append(data)

        for row in cm_rows_ow:

            cells = row.find_all('td')

            # Extract the content of each row
            data = [cell.get_text(strip=True) for cell in cells]

            # Add the data into the measure_row if
            if cm_rows_ow.index(row) != 0:

                measure_row[1].append(data)

            else:

                measurements.append(data)

    else:

        measure_row = []

        cm_rows = table[0].find_all('tr')

        for row in cm_rows:

            cells = row.find_all('td')

            # Extract the content of each row
            data = [cell.get_text(strip=True) for cell in cells]

            # Add the data into the measure_row if
            if cm_rows.index(row) != 0:

                measure_row.append(data)

            else:

                measurements = data

    # Iterates through the strings of html code in the table

    return (measurements, measure_row)

def edit_table(og_html, table_data):

    soup = BeautifulSoup(og_html, 'html.parser')

    tables = soup.find_all('table')

    new_tables = tables

    if len(new_tables) == 4:
        
        for table in new_tables:
            rows = table.find_all('tr')
            table_data_raw = table_data[:len(rows)]
            table_data_ow = table_data[len(rows):]
            if "CM" in str(rows):
                if "Raw" in str(rows):
                    for i, row in enumerate(rows):
                        cells = row.find_all('td')
                        if i != 0:
                            for j, cell in enumerate(cells):
                                if j != 0:
                                    cell.clear()
                                    cell.append(str(table_data_raw[i - 1][j - 1]))
                elif "One Wash" in str(rows):
                    for i, row in enumerate(rows):
                        cells = row.find_all('td')
                        if i != 0:
                            for j, cell in enumerate(cells):
                                if j != 0:
                                    cell.clear()
                                    print(len(cell), len(str(table_data_ow[i - 1][j - 1])))
                                    cell.append(str(table_data_ow[i - 1][j - 1]))
            elif "Inches" in str(rows):
                if "Raw" in str(rows):
                    for i, row in enumerate(rows):
                        cells = row.find_all('td')
                        if i != 0:
                            for j, cell in enumerate(cells):
                                if j != 0:
                                    cell.clear()
                                    cell.append(str(round((float(table_data_raw[i - 1][j - 1])/2.54), 1)))
                elif "One Wash" in str(rows):
                    for i, row in enumerate(rows):
                        cells = row.find_all('td')
                        if i != 0:
                            for j, cell in enumerate(cells):
                                if j != 0:
                                    cell.clear()
                                    cell.append(str(round((float(table_data_ow[i - 1][j - 1])/2.54), 1)))
    
    else:

        for table in new_tables:
            rows = table.find_all('tr')
            if "CM" in str(rows):
                for i, row in enumerate(rows):
                        cells = row.find_all('td')
                        if i != 0:
                            for j, cell in enumerate(cells):
                                if j != 0:
                                    cell.clear()
                                    cell.append(str(table_data[i - 1][j - 1]))
            elif "Inches" in str(rows):
                for i, row in enumerate(rows):
                    cells = row.find_all('td')
                    if i != 0:
                        for j, cell in enumerate(cells):
                            if j != 0:
                                cell.clear()
                                cell.append(str(round((float(table_data[i - 1][j - 1])/2.54), 1)))

    for table, new_table in zip(tables, new_tables):

        table.replace_with(new_table)

    return str(soup)

def update_measure_table(product_id, html_code, headers):
    data = {
        'product': {
            'id': int(product_id),
            'body_html': html_code
        }
    }

    response = requests.put(
        f"https://okayamadenim.myshopify.com/admin/api/2023-04/products/{product_id}.json",
        json = data,
        headers = headers
    )

    # Check the response
    if response.status_code == 200:
        return "Complete"
