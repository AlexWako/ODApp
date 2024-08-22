import requests
from pathlib import Path
from bs4 import BeautifulSoup

brands = {
    "big john": "big_john",
    "burgus plus": "burgus_plus",
    "full count": "full_count",
    "japan blue": "japan_blue",
    "kamikaze attack": "kamikaze_attack",
    "momotaro jeans": "momotaro_jeans",
    "pure blue japan": "pure_blue_japan",
    "samurai jeans": "samurai_jeans",
    "stevenson overall": "stevenson_overall",
    "studio d'artisan": "studio_d_artisan",
    "tcb": "tcb",
    "urvin": "urvin"
}

def get_denimio(input):

    response = requests.get(f"https://www.denimio.com/brand/{brands.get(input)}?product_list_limit=all")
    soup = BeautifulSoup(response.content, 'html.parser')

    match = {}

    products = soup.find_all(class_= "product-item-name")
    prices = soup.find_all(class_= "price")

    for product, price in zip(reversed(products), reversed(prices)):
        try:
            for name, hyperlink in zip(product.find('a', href = True), product.find_all('a', href = True)):
                    match[name.replace('\n', '')] = (hyperlink['href'], price.text.strip().replace('JP¥', ''))
        except:
            break

    return match

def pd_txt_file(brand, data = None):

    file_path = f"./resource/diagnostic/{brands.get(brand)}.txt"

    if data == None:
        if Path(file_path).is_file():
            with open(file_path, "r") as file:
                den_old_data = file.read()
        else:
            return None

    else:
        with open(file_path, "w") as file:
            file.write(str(data))
            return "Done"

    return den_old_data

def diagnostic(old, new):

    data = {
        "Changes": [],
        "New products": []
    }

    if old != None:
        old_set = set(old)
        new_set = set(new)

        # Finds old products with price changes
        for product in old_set.intersection(new_set):
            for old_value, new_value in zip(old.get(product)[1], new.get(product)[1]):
                if old_value != new_value:
                    data["Changes"].append([product, new_value - old_value])
                else:
                    continue

    # Finds new products in the store
    for product in new_set.difference(old_set):
        data["New products"].append([product, new.get(product)[1]])

    return data


