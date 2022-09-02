import csv
import json

DATA_ADS = 'data/ads.csv'
JSON_ADS = "ads.json"
DATA_CATEGORIES = "data/categories.csv"
JSON_CATEGORIES = "categories.json"


def converter(csv_name, model_name, json_name):
    result = []
    with open(csv_name, encoding='utf-8') as csvf:
        for row in csv.DictReader(csvf):
            to_add = {'model': model_name, "pk": int(row["Id"] if "Id" in row else row['id'])}
            if 'Id' in row:
                del row["Id"]
            else:
                del row["id"]
            if "is_published" in row:
                if row["is_published"] == "TRUE":
                    row['is_published'] = True
                else:
                    row['is_published'] = False
            if "price" in row:
                row['price'] = int(row['price'])
            to_add["fields"] = row
            result.append(to_add)

        with open(json_name, 'w', encoding="utf-8") as jsf:
            jsf.write(json.dumps(result, ensure_ascii=False))


# converter(DATA_ADS, "ads.ad", JSON_ADS)
converter(DATA_CATEGORIES, "ads.category", JSON_CATEGORIES)
