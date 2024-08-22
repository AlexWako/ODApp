import re

def remove_space(string):
    string = string.replace(' ','')
    return string

def get_int(string):
    return ''.join(re.findall(r'\d+', string))

def list_to_int(data):
    temp = []
    for i in range(len(data)):
        temp.append(int(data[i]))
    return temp
        
# Not used
def list_to_html(data):
    html_code = "<table width='100%'>\n"
    for row in data:
        html_code += "<tr>\n"
        for cell in row:
            html_code += f"<td>{cell}</td>\n"
        html_code += "</tr>\n"
    html_code += "</table>"
    return html_code
