import pandas as pd

data_av_week = pd.read_csv("data_av_week.csv")
supermarkt_urls = pd.read_csv("supermarkt_urls.csv")
s_details = pd.read_csv("notebooksdetailed_supermarkt_python_mined.csv", header= None)
migros_details = pd.read_csv("notebooksdetailed_Migros_python_mined.csv", header= None)
coop_details = pd.read_csv("notebooksdetailed_Coop_python_mined.csv", header= None)

data_av_week = data_av_week.drop(["Unnamed: 0"], axis=1)
data_av_week = data_av_week.rename({'url':'urls'}, axis=1)

head = ["name_supermarkt", "address", "lat", "long", "key_words", "codes", "postal_code", "address2", "url2"]
s_details.columns = head
s_details = s_details.drop(columns=['address2'])
migros_details.columns = head
migros_details = migros_details.drop(columns=['address2'])
coop_details.columns = head
coop_details = coop_details.drop(columns=['address2'])

# merge the supermarkt data
supermarkt_details = pd.merge(s_details, migros_details, how="outer")
supermarkt_details = pd.merge(supermarkt_details, coop_details, how="outer")

data_week_urls = pd.merge(supermarkt_urls, data_av_week, how="outer", on="urls")

data_names_week_all = pd.merge(supermarkt_details, data_week_urls, how="outer", on="codes")

data_names_week_all.to_csv("all_data_per_week.csv", index=False)

# Per day
data_av_day = pd.read_csv("data_av_day.csv")

data_av_day = data_av_day.drop(["Unnamed: 0"], axis=1)
data_av_day = data_av_day.rename({'url':'urls'}, axis=1)
data_days_urls = pd.merge(supermarkt_urls, data_av_day, how="outer", on="urls")

data_names_days_all = pd.merge(supermarkt_details, data_days_urls, how="outer", on="codes")
data_names_days_all.to_csv("all_data_per_day.csv", index=False)