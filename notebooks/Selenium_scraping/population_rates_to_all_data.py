import pandas as pd

data_av_week = pd.read_csv("data_av_week.csv")
supermarkt_urls = pd.read_csv("supermarkt_urls.csv")
supermarkt_details = pd.read_csv("notebooksdetailed_supermarkt_python_mined.csv", header= None)

data_av_week = data_av_week.drop(["Unnamed: 0"], axis=1)
data_av_week = data_av_week.rename({'url':'urls'}, axis=1)

head = ["name_supermarkt", "address", "lat", "long", "key_words", "codes", "postal_code", "address2", "url2"]
supermarkt_details.columns = head
supermarkt_details = supermarkt_details.drop(columns=['address2'])

data_week_urls = pd.merge(supermarkt_urls, data_av_week, how="left", on="urls")

data_names_week_all = pd.merge(supermarkt_details, data_week_urls, how="left", on="codes")

data_names_week_all.to_csv("all_data_per_week.csv", index=False)

# Per day
data_av_day = pd.read_csv("data_av_day.csv")

data_av_day = data_av_day.drop(["Unnamed: 0"], axis=1)
data_av_day = data_av_day.rename({'url':'urls'}, axis=1)
data_days_urls = pd.merge(supermarkt_urls, data_av_day, how="left", on="urls")

data_names_days_all = pd.merge(supermarkt_details, data_days_urls, how="left", on="codes")
data_names_days_all.to_csv("all_data_per_day.csv", index=False)