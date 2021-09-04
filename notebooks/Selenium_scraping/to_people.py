import json
import requests
import pandas as pd

# take the csv with urls and codes, extract the url code and use it to select and
# join the porcentage of people's csv

def main(csv_urls):

    # text string on which to search
    # Put always the csv in the same folder
    df1 = pd.read_csv(csv_urls)

    data_raw = pd.DataFrame(columns=["place","url","scrape_time", "day_of_week", "hour_of_day", "popularity_percent_normal", "popularity_percent_current"])
    for i in range(0, len(df1)):
        cid = df1["urls"][i].split("=")[1] # split the url and keep the second part
        try:
            df_ind = pd.read_csv("data/_cid=" + cid + ".20210903_204156.csv")
        except:
            pass

        data_raw = pd.concat([data_raw, df_ind], ignore_index=True)

    return data_raw


def average_day(data):
    # delete rows empties "popularity_percent_normal"
    data_no_null = data[data["popularity_percent_normal"] != ""]
    data_av_day = data_no_null.groupby(["url", "place","day_of_week"])["popularity_percent_normal"].mean().reset_index()
    data_av_week = data_no_null.groupby(["url", "place"])["popularity_percent_normal"].mean().reset_index()

    data_av_day.to_csv("data_av_day.csv")
    data_av_week.to_csv("data_av_week.csv")




data_raw_mult = main("supermarkt_urls.csv")
data_raw_mult.to_csv("raw_data_people.csv")
average_day(data_raw_mult)