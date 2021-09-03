import json
import requests
import pandas as pd

key_dict = {"key": "AIzaSyAJ97RuEMWKQnXxVQLPhu0OaljMVu76bfI"}
with open("credentials_juan.json", "w") as output:
    json.dump(key_dict, output)
key_json = json.load(open("credentials_juan.json"))
# key_json["key"]
gmaps_key = key_json["key"]
# gmaps_key

url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

# text string on which to search
head_names = ["names", "address", "lat", "long", "types", "codes"]
df1 = pd.read_csv("notebooksMigros_python_mined.csv", names=head_names)
urls_list = []

for i in range(0,len(df1["names"])):

    id = "{0}".format(df1["codes"][i])

    # actual api key
    api_key = gmaps_key

    # get method of requests module, return response object
    url2 = ("https://maps.googleapis.com/maps/api/place/details/json?placeid="+ id + "&key="+ api_key)
    print(url2)
    # get method of requests module, return response object
    req = requests.get(url2)

    # json method of response object: json format data -> python format data
    places_json = req.json()

    my_result = places_json["result"]
    # now result contains list of nested dictionaries
    urls_list.append(my_result["url"])

urls_df = pd.DataFrame({"urls": urls_list})

urls_df.to_csv("migros_urls.csv", index=False)
