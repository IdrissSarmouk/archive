import pandas as pd
import numpy as np



tb = pd.read_csv("bank_marketing.csv")

client = tb[["client_id", "age", "job", "marital", 
                    "education", "credit_default", "mortgage"]]
campaign = tb[["client_id", "number_contacts", "month", "day", 
               "contact_duration", "previous_campaign_contacts", "previous_outcome", "campaign_outcome"]]
economics = tb[["client_id", "cons_price_idx", "euribor_three_months"]]




client["education"] = client["education"].str.replace(".", "_")
client["education"] = client["education"].replace("unknown", np.NaN)

client["job"] = client["job"].str.replace(".", "")

for i in ["credit_default", "mortgage"]:
    client[i] = client[i].astype(bool)

campaign["campaign_outcome"] = campaign["campaign_outcome"].map({"yes": 1, 
                                                                 "no": 0})

campaign["previous_outcome"] = campaign["previous_outcome"].map({"success": 1, 
                                                                 "failure": 0,
                                                                 "nonexistent": 0})

campaign["month"] = campaign["month"].str.capitalize()

campaign["year"] = "2022"

campaign["day"] = campaign["day"].astype(str)

campaign["last_contact_date"] = campaign["year"] + "-" + campaign["month"] + "-" + campaign["day"]

campaign["last_contact_date"] = pd.to_datetime(campaign["last_contact_date"], 
                                               format="%Y-%b-%d")

for i in ["campaign_outcome", "previous_outcome"]:
    campaign[i] = campaign[col].astype(bool)

campaign.drop(columns=["month", "day", "year"], inplace=True)



client.to_csv("client.csv", index=False)
campaign.to_csv("campaign.csv", index=False)
economics.to_csv("economics.csv", index=False)
