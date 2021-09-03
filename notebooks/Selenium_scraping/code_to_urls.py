import json
import requests
import pandas as pd


def main(csv_file_name):
    key_dict = {"key": "AIzaSyAJ97RuEMWKQnXxVQLPhu0OaljMVu76bfI"}
    with open("credentials_juan.json", "w") as output:
        json.dump(key_dict, output)

    key_json = json.load(open("credentials_juan.json"))
    # key_json["key"]
    gmaps_key = key_json["key"]
    # gmaps_key

    # text string on which to search
    # Put always the csv in the same folder
    head_names = ["names", "address", "lat", "long", "types", "codes"]
    df1 = pd.read_csv(csv_file_name, names=head_names)
    urls_list = []


    for i in range(0, len(df1["names"])):

        id = "{0}".format(df1["codes"][i])

        # actual api key
        api_key = gmaps_key

        # get method of requests module, return response object
        url = ("https://maps.googleapis.com/maps/api/place/details/json?placeid=" + id + "&key=" + api_key)
        # get method of requests module, return response object
        req = requests.get(url)

        # json method of response object: json format data -> python format data
        places_json = req.json()

        my_result = places_json["result"]
        # now result contains list of nested dictionaries
        urls_list.append(my_result["url"])



    urls_df = pd.DataFrame({"urls": urls_list})

    urls_df.to_csv(df1["names"][1].replace(" ", "_") + "_urls.csv", index=False)

main("notebooksMigros_python_mined.csv")
