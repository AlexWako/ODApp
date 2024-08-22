import pandas as pd
from EditMeasureScript import *

def jeans_measure_edit(df, url, jean_type):
    df = df.loc[:, ['Handle', 'Title', 'Body (HTML)', 'Option1 Value', 'Option2 Value', 'Variant Price', 'Image Src']]
    products = df.groupby(['Handle'])['Option1 Value'].agg(list).reset_index()
    products2 = df.groupby(['Handle'])['Option2 Value'].agg(list).reset_index()
    df = df.dropna(subset = ['Title'])
    df.loc[:, 'Option1 Value'] = products.loc[:, 'Option1 Value']
    df.loc[:, 'Option2 Value'] = products2.loc[:, 'Option2 Value']

    measurements = []
    for row in df.itertuples():
        try:
            measurements.append([row[2], row[6], row[7], list(get_og_cm_data(row[3]))])
        except:
            continue

    for i in range(len(measurements)):
        if len(measurements[i][3][0]) == 2:
            for j in range(2):
                if "raw" in measurements[i][3][0][j][0].lower():
                    measurements[i][3][0][j] = 'Raw'
                if "one wash" in measurements[i][3][0][j][0].lower() or "ow" in measurements[i][3][0][j][0].lower():
                    measurements[i][3][0][j] = 'One Wash'
        else:
            measurements[i][3][0] = jean_type

    data_list = []
    for measure in measurements:
        name = measure[0]
        price = measure[1]
        image = measure[2]
        try:
            if type(measure[3][0]) == list:
                for i in range(2):
                    for size in measure[3][1][i]:
                        data_list.append({
                            'Name': name, 
                            'Price': price,
                            'Image': image,
                            'URL': url,
                            'Type': measure[3][0][i],
                            'Size': size[0],
                            'Waist': round(float(size[1])/2.54, 2),
                            'Front Rise': round(float(size[2])/2.54, 2),
                            'Back Rise': round(float(size[3])/2.54, 2),
                            'Upper Thigh': round(float(size[4])/2.54, 2),
                            'Knee': round(float(size[5])/2.54, 2),
                            'Leg Opening': round(float(size[6])/2.54, 2),
                            'Inseam': round(float(size[7])/2.54, 2)
                        })
            else:
                for size in measure[3][1]:
                    data_list.append({
                        'Name': name, 
                        'Price': price,
                        'Image': image,
                        'URL': url,
                        'Type': jean_type,
                        'Size': size[0],
                        'Waist': round(float(size[1])/2.54, 2),
                        'Front Rise': round(float(size[2])/2.54, 2),
                        'Back Rise': round(float(size[3])/2.54, 2),
                        'Upper Thigh': round(float(size[4])/2.54, 2),
                        'Knee': round(float(size[5])/2.54, 2),
                        'Leg Opening': round(float(size[6])/2.54, 2),
                        'Inseam': round(float(size[7])/2.54, 2)
                    })
        except:
            continue

    return pd.DataFrame(data_list)